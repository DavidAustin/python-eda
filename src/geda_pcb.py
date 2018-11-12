# Python-EDA
# Copyright (C) 2018 David Austin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import re
import pyparsing as pp
import shapely
import shapely.geometry

def old_pcb_units_to_mm(x):
    return x / 1e5 * 25.4
    
def frommm(m):  #FIXME
    return m / 25.4 * 1e5

def tomm(i):
    return i * 25.4 / 1e5

def miltomm(i):
    return i * 25.4/1000

SHAPELY_BUF_PTS = 10

#NOTE: Stupid over-optimisation and re-use of bits for different
#      meanings!  Also note that new thermal(...) flags CAN'T 
#      be represented this way.
geda_pcb_object_flags = (
    (0x0001, 'pin', ['all'],
     'If set, this object is a pin. PCB internal use only.'),
    (0x0002, 'via', ['all'],
     'If set, this object is a via. PCB internal use only.'),
    (0x0004, 'found', ['all'],
     'If set, this object has been found by FindConnection().'),
    (0x0008, 'hole', ['pin', 'via'],
     'For pins and vias, means is a hole without a copper annulus.'),
    (0x0010, 'rat', ['line'],
     'For a line, indicates that this is a rat line'),
    (0x0010, 'pininpoly', ['pin', 'pad'],
     'For pins and pads, this flag is used internally to indicate that'
     ' the pin or pad overlaps a polygon on some layer.'),    
    (0x0010, 'clearpoly', ['polygon'],
     'For polygons, this flag means that pins and vias will '
     'normally clear these polygons (thus, thermals are required '
     'for electrical connection). When clear, polygons will solidly '
     'connect to pins and vias.'),
    (0x0010, 'hidename',  ['element'],
     'For elements, when set the name of the element is hidden.'),
    (0x0020, 'showname', ['element'],
     'For elements, when set the names of pins are shown.'),
    (0x0020, 'clearline', ['line', 'arc'],
     'For lines and arcs, the line/arc will clear polygons instead '
     'of connecting to them.'),
    (0x0020, 'fullpoly', ['polygon'],
     'For polygons, the full polygon is drawn (i.e. all parts instead '
     'of only the biggest one).'),
    (0x0040, 'selected', ['all'],
     'Set when the object is selected.'),
    (0x0080, 'onsolder', ['element', 'pad'],
     'For elements and pads, indicates that they are on the solder side.'),
    (0x0080, 'auto', ['line', 'via'],
     'For lines and vias, indicates that these were created by the '
     'autorouter.'),
    (0x0100, 'square', ['pin', 'pad'],
     'For pins and pads, indicates a square (vs round) pin/pad.'),
    (0x0200, 'rubberend', ['line'],
     'For lines, used internally for rubber band moves.'),
    (0x0200, 'warn', ['pin', 'via', 'pad'],
     'For pins, vias, and pads, set to indicate a warning.'),
    (0x0400, 'usetherm', ['pin', 'via'],
     'Obsolete, indicates that pins/vias should be drawn with '
     'thermal fingers.'),
    (0x0400, 'drawonsilk', ['line'],
     'Obsolete, old files used this to indicate lines drawn on silk.'),
    (0x0800, 'octagon', ['pin', 'pad'], 'Draw pins and vias as octagons.'),
    (0x1000, 'drc', ['all'], 'Set for objects that fail DRC.'),
    (0x2000, 'lock', ['all'], 'Set for locked objects.'),
    (0x4000, 'edge2', ['pad', 'pin'],
     'For pads, indicates that the second point is closer to the '
     'edge. For pins, indicates that the pin is closer to a '
     'horizontal edge and thus pinout text should be vertical.'),
    (0x8000, 'marker', ['all'], 'Marker used internally to avoid '
     'revisiting an object.'),
    (0x10000, 'nopaste', ['pad'],
     'For pads, set to prevent a solderpaste stencil opening for '
     'the pad. Primarily used for pads used as fiducials.')
)



geda_pcb_flags = (
    (0x00000001, 'shownumber',
     'Pinout displays pin numbers instead of pin names.'),
    (0x00000002, 'localref',
     'Use local reference for moves, by setting the mark at the '
     'beginning of each move.'),
    (0x00000004, 'checkplanes', 'When set, only polygons and their '
     'clearances are drawn, to see if polygons have isolated regions.'),
    (0x00000008, 'showdrc', 'Display DRC region on crosshair.'),
    (0x00000010, 'rubberband', 'Do all move, mirror, rotate with '
     'rubberband connections.'),
    (0x00000020, 'description',
     'Display descriptions of elements, instead of refdes.'),
    (0x00000040, 'nameonpcb',
     'Display names of elements, instead of refdes.'),
    (0x00000080, 'autodrc',
     "Auto-DRC flag. When set, PCB doesn't let you place copper "
     "that violates DRC."),
    (0x00000100, 'alldirection', "Enable 'all-direction' lines."),
    (0x00000200, 'swapstartdir', 'Switch starting angle after each click.'),
    (0x00000400, 'uniquename', 'Force unique names on board.'),
    (0x00000800, 'clearnew', 'New lines/arc clear polygons.'),
    (0x00001000, 'snappin', 'Crosshair snaps to pins and pads.'),
    (0x00002000, 'showmask', 'Show the solder mask layer.'),
    (0x00004000, 'thindraw', 'Draw with thin lines.'),
    (0x00008000, 'orthomove', 'Move items orthogonally.'),
    (0x00010000, 'liveroute', 'Draw autoroute paths real-time.'),
    (0x00020000, 'thindrawpoly', 'Draw polygons with thin lines?'),
    (0x00040000, 'locknames', 'Lock names?'),
    (0x00080000, 'onlynames', '???'),
    (0x00100000, 'newfullpoly', 'New polygons are full ones.'),
    (0x00200000, 'hidenames', 'Hide names?')
    )






class GEDAPCBBase(object):
    string_attrs = ('fileversion', 'pcbname', 
                    'pcbflags', 'groups_str', 'styles_str',
                    'name', 'children', 'desc', 'value', 'number', 'style',
                    'refdes', 'points', 'holes')
    pcb_units_attrs = ('sizex', 'sizey', 
                       'gridoffx', 'gridoffy',
                       'cursorx', 'cursory', 
                       'drcbloat', 'drcshrink', 'drcline',
                       'drcsilk', 'drcdrill', 'drcring', 'step',
                       'mx', 'my', 'tx', 'ty',
                       'x1', 'y1', 'x2', 'y2', 'thickness',
                       'clearance', 'x', 'y', 'hole_dia')
    pcb_units_float_attrs = ('step')
    float_attrs = ('thermalscale', 'zoom', 'minpolyarea')
    int_attrs = ('tdir', 'tscale', 'start_angle', 'delta_angle', 
                 'group1', 'group2', 'layer_num')
    def __init__(self, attr_list, data):
        #print self.type
        for a in attr_list:
            if a in self.string_attrs:
                setattr(self, a, data.get(a, ''))
            elif a in ('flags', 'tflags'):
                flags = data.get(a, '')
                if not isinstance(flags, dict):
                    if not isinstance(flags, list):
                        flags = self.parse_flags(flags)
                #print 'pcb_base:flags', self.type, flags, data.get(a, ''), a
                    nflags = {}
                    for flag in flags:
                        nflags[flag] = True
                    flags = nflags
                setattr(self, a, flags)
            elif a in self.int_attrs:
                setattr(self, a, int(data.get(a, 0)))
            elif a in self.pcb_units_attrs:
                setattr(self, a, float(data.get(a, 0)))
            #elif a in self.pcb_units_float_attrs:
            #    setattr(self, a, float(data.get(a, 0)))
            elif a in self.float_attrs:
                setattr(self, a, float(data.get(a, 0.0)))
            else:
                setattr(self, a, int(data.get(a, 0)))
            #print a, '->', str(getattr(self,a))

    def asDict(self):
        ret = {}
        for a in self.attr_list:
            ret[a] = getattr(self, a)
        return ret

    def parse_flags(self, f):
        if isinstance(f, str):
            try:
                f = int(f, 16)
            except:
                if f.find('thermal') < 0:                    
                    f = f.split(',')
                else:
                    f2 = []
                    bu = None
                    for e in f.split(','):
                        if bu != None:
                            if e.find(')') >= 0:
                                bu.append(e)
                                f2.append(','.join(bu))
                                bu = None
                            else:
                                bu.append(e)
                        else:
                            if e.find('thermal(') >= 0 and e.find(')') < 0:
                                bu = [e]
                            else:
                                f2.append(e)
                    f = f2
                    
                return f

        ret = []
        if isinstance(f, int): 
            for mask, flagstr, objs, desc in geda_pcb_object_flags:
                if f & mask != 0 and (self.type in objs or 'all' in objs):
                    ret.append(flagstr)
        return ret


    def str_flags(self, flags = None):
        if flags == None:
            flags = self.flags
        f2 = {}
        f2.update(flags)
        ret = []
        for i in range(32):
            m = 1 << i
            for mask, flagstr, objs, desc in geda_pcb_object_flags:
                #print flagstr, f2
                if flagstr in f2 and f2[flagstr]:
                    ret.append(flagstr)
                    del f2[flagstr]

        for (k, v) in f2.items():
            #print k,v
            if v:
                ret.append(k)
        return ','.join(ret)

class GEDAPCBCoord(GEDAPCBBase):
    attr_list = ('x', 'y')
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
        else:
            self.x = args[0]
            self.y = args[1]
            

class GEDAPCBPad(GEDAPCBBase):
    type = 'pad'
    attr_list = ('name', 'x1', 'y1', 'x2', 'y2', 'thickness', 'clearance',
                 'mask', 'flags', 'number')
    
    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Pad[%.6fmm %.6fmm %.6fmm %6fmm %.6fmm %.6fmm %d "%s" "%s" "%s"]' % \
                        (self.x1, self.y1, self.x2, self.y2,
                        self.thickness, self.clearance, 
                        self.mask,
                        self.name, self.number, self.str_flags())

    def transform(self, x, y, r):
        return GEDAPCBPad({'name' : self.name, 
                           'x1' : self.x1 + x, 
                           'y1' : self.y1 + y, 
                           'x2' : self.x2 + x, 
                           'y2' : self.y2 + y, 
                           'thickness' : self.thickness, 
                           'clearance' : self.clearance,
                           'mask' : self.mask, 
                           'flags' : self.flags, 
                           'number' : self.number})

    def make_shape(self):
        if 'square' in self.flags:
            x1 = self.x1 - self.thickness/2.0
            y1 = self.y1 - self.thickness/2.0
            x2 = self.x2 + self.thickness/2.0
            y2 = self.y2 + self.thickness/2.0

            self.shape = shapely.geometry.Polygon([(x1, y1), (x2, y1), (x2, y2),
                                                   (x1, y2)])
        else:
            line = shapely.geometry.LineString([(self.x1, self.y1), 
                                                (self.x2, self.y2)])
            self.shape = line.buffer(self.thickness/2.0, SHAPELY_BUF_PTS)



class GEDAPCBPin(GEDAPCBBase):
    type = 'pin'
    attr_list = ('name', 'x', 'y', 'thickness', 'mask', 'clearance', 'hole_dia',
                 'flags', 'number')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Pin[%d %d %d %d %d %d "%s" "%s" "%s"]' % \
                        (self.x, self.y, self.thickness, self.clearance,
                         self.mask, self.hole_dia, 
                         self.name, self.number, self.str_flags())

    def transform(self, x, y, r):
        return GEDAPCBPin({'name' : self.name, 
                           'x' : self.x + x, 
                           'y' : self.y + y, 
                           'hole_dia' : self.hole_dia, 
                           'thickness' : self.thickness,
                           'clearance' : self.clearance,
                           'mask' : self.mask, 
                           'flags' : self.flags, 
                           'number' : self.number})

    def make_shape(self):
        point = shapely.geometry.Point(self.x, self.y)
        self.shape = point.buffer(self.thickness / 2.0, buf_pts)



class GEDAPCBElementLine(GEDAPCBBase):
    type = 'eltline'
    attr_list = ('name', 'x1', 'y1', 'x2', 'y2', 'thickness')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'ElementLine[%d %d %d %d %d]' % \
            (self.x1, self.y1, self.x2, self.y2, self.thickness)

    def transform(self, x, y, r):
        return GEDAPCBElementLine({'name' : self.name, 
                                   'x1' : self.x1 + x, 
                                   'y1' : self.y1 + y, 
                                   'x2' : self.x2 + x, 
                                   'y2' : self.y2 + y, 
                                   'thickness' : self.thickness})
    def get_bb(self):
        raise NotImplementedError


class GEDAPCBElementArc(GEDAPCBBase):
    type = 'eltarc'

    attr_list = ('name', 'x', 'y', 'width', 'height', 
                 'start_angle', 'delta_angle', 'thickness')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'ElementArc[%d %d %d %d %d %d %d]' % \
            (self.x, self.y, self.width, self.height, self.start_angle, 
            self.delta_angle, self.thickness)

    def transform(self, x, y, r):
        return GEDAPCBElementArc(
            {'name' : self.name, 
             'x' : self.x + x, 
             'y' : self.y + y, 
             'width' : self.width, 
             'height' : self.height, 
             'start_angle' : self.start_angle, 
             'delta_angle' : self.delta_angle, 
             'thickness' : self.thickness})

    def get_bb(self):
        raise NotImplementedError


class GEDAPCBElement(GEDAPCBBase):
    type = 'element'
    attr_list = ('name', 'desc', 'value', 'mx', 'my', 
                 'tx', 'ty', 'tdir', 'tscale', 'tflags', 'flags',
                 'children')
    
    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)
        
    def __str__(self):
        ret = 'Element["%s" "%s" "%s" "%s" %d %d %d %d %d %d "%s"]' % \
            (self.str_flags(), self.desc, self.name, self.value,
             self.mx, self.my, self.tx, self.ty, self.tdir, self.tscale,
             self.str_flags(self.tflags))
        ret += '\n'
        ret += '(\n'
        for c in self.children:
            ret += '\t' + str(c) + '\n'
        ret += '\n\t)\n'

        return ret

    def transform(self, x, y, r):
        nc = [c.transform(0, 0, 0) for c in self.children]
        return GEDAPCBElement({'name' : self.name, 
                               'desc' : self.desc, 
                               'value' : self.value, 
                               'mx' : self.mx + x, 
                               'my' : self.my + y, 
                               'tx' : self.tx, 
                               'ty' : self.ty, 
                               'tdir' : self.tdir, 
                               'tscale' : self.tscale, 
                               'tflags' : self.tflags, 
                               'flags' : self.flags,
                               'children' : nc})

class GEDAPCBRat(GEDAPCBBase):
    type = 'rat'
    attr_list = ('x1', 'y1', 'group1', 'x2', 'y2', 'group2', 'flags')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Rat[%d %d %d %d %d %d "%s"]' % \
            (self.x1, self.y1, self.group1, self.x2, self.y2, self.group2,
             self.str_flags())
    
    def make_shape(self):
        points = shapely.geometry.MultiPoint([(self.x1, self.y1), 
                                              (self.x2, self.y2)])
        self.shape = points.buffer(5, SHAPELY_BUF_PTS)



class GEDAPCBArc(GEDAPCBBase):
    type = 'arc'

    attr_list = ('name', 'x', 'y', 'width', 'height', 'thickness', 'clearance',
                 'start_angle', 'delta_angle', 'flags')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Arc[%d %d %d %d %d %d %d %d "%s"]' % \
            (self.x, self.y, self.width, self.height, self.thickness, self.clearance,
             self.start_angle, self.delta_angle, self.str_flags())

    def transform(self, x, y, r):
        return Arc({'name' : self.name, 
                    'x' : self.x + x, 
                    'y' : self.y + y, 
                    'width' : self.width, 
                    'height' : self.height, 
                    'thickness' : self.thickness,
                    'clearance' : self.clearance,
                    'start_angle' : self.start_angle, 
                    'delta_angle' : self.delta_angle, 
                    'flags' : self.flags})
    
    def get_bb(self):
        raise NotImplementedError

class GEDAPCBText(GEDAPCBBase):
    type = 'text'
    attr_list = ('x', 'y', 'tdir', 'tscale', 'name', 'flags')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Text[%d %d %d %d "%s" "%s"]' % \
            (self.x, self.y, self.tdir, self.tscale, self.name,
             self.str_flags())

    def transform(self, x, y, r):
        return GEDAPCBText({'x' : self.x + x, 
                            'y' : self.y + y, 
                            'tdir' : self.tdir, 
                            'tscale' : self.tscale, 
                            'name' : self.name, 
                            'flags' : self.flags})


class GEDAPCBConnect(GEDAPCBBase):
    type = 'connect'
    attr_list = ('refdes', 'number')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Connect("%s-%s")' % (self.refdes, self.number)


class GEDAPCBNet(GEDAPCBBase):
    type = 'net'
    attr_list = ('name', 'style', 'children')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self, prefix=''):
        ret = '%sNet("%s" "%s")\n' % \
            (prefix, self.name, self.style)
        ret += '%s(\n' % prefix
        for c in self.children:
            ret += ('%s\t' % prefix) + str(c) + '\n'
        ret += '%s)' % prefix

        return ret
    

class GEDAPCBNetList(GEDAPCBBase):
    type = 'net'
    attr_list = ('children',)

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        ret = 'NetList()\n'
        ret += '(\n'
        for c in self.children:
            ret += c.__str__('\t') + '\n'
        ret += ')'

        return ret

class GEDAPCBPolyPoint(GEDAPCBBase):
    type = 'polypoint'
    attr_list = ('x', 'y')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def transform(self, x, y, r):
        return GEDAPCBPolyPoint({'x' : self.x + x,
                          'y' : self.y + y})

class GEDAPCBPolyHole(GEDAPCBBase):
    type = 'polyhole'
    attr_list = ('children',)

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self, prefix='\t'):
        return '%s\tHole (\n%s\t%s\n%s)' % \
            (prefix, prefix,
             ' '.join(["[%d %d]" % (e.x, e.y) for e in self.children]),
             prefix)

    def transform(self, x, y, r):
        ch = [p.transform(x, y, r) for p in self.children]
        return GEDAPCBPolyHole({'children' : ch})

class GEDAPCBPolygon(GEDAPCBBase):
    type = 'polygon'
    attr_list = ('flags', 'points', 'holes')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        ret = 'Polygon("%s")\n\t(\n\t\t%s' % \
            (self.str_flags(),
             ' '.join(["[%d %d]" % (e.x, e.y) for e in self.points]))
        for h in self.holes:
            ret += h.__str__('\t\t')
        ret += '\n\t)'
        return ret

    def transform(self, x, y, r):
        pts = [p.transform(x, y, r) for p in self.points]
        hls = [h.transform(x, y, r) for h in self.holes]
        return GEDAPCBPolygon({'points' : pts,
                               'flags' : self.flags,
                               'holes' : hls})


class GEDAPCBSymbolLine(GEDAPCBBase):
    type = 'symbolline'
    attr_list = ('x1', 'y1', 'x2', 'y2', 'thickness')
            
    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'SymbolLine[%d %d %d %d %d]' % \
            (self.x1, self.y1, self.x2, self.y2, self.thickness)

    
class GEDAPCBSymbol(GEDAPCBBase):
    type = 'symbol'
    attr_list = ('name', 'width', 'children')
    

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        ret = "Symbol['%s' %d]" % \
            (self.name, self.width)
        ret += '\n'
        ret += '(\n'
        for c in self.children:
            ret += '\t' + str(c) + '\n'
        ret += ')'

        return ret


class GEDAPCBVia(GEDAPCBBase):
    type = 'via'
    attr_list = ('x', 'y', 'thickness', 'clearance', 'mask', 'hole_dia', 'name',
                 'flags')
    
    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Via[%d %d %d %d %d %d "%s" "%s"]' % \
                        (self.x, self.y, self.thickness, self.clearance,
                         self.mask, self.hole_dia, 
                         self.name, self.str_flags())

    def transform(self, x, y, r):
        return GEDAPCBVia({'x' : self.x + x,
                           'y' : self.y + y,
                           'thickness' : self.thickness,
                           'clearance' : self.clearance,
                           'mask' : self.mask,
                           'hole_dia' : self.hole_dia,
                           'name' : self.name,
                           'flags' : self.flags})

    def make_shape(self):
        point = shapely.geometry.Point(self.x, self.y)
        self.shape = point.buffer(self.thickness / 2, SHAPELY_BUF_PTS)

class GEDAPCBLine(GEDAPCBBase):
    type = 'line'
    attr_list = ('x1', 'y1', 'x2', 'y2', 'thickness', 'clearance', 'flags')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Line[%d %d %d %d %d %d "%s"]' % \
            (self.x1, self.y1, self.x2, self.y2, self.thickness, 
             self.clearance, self.str_flags())

    def transform(self, x, y, r):
        return GEDAPCBLine({'x1' : self.x1 + x,
                            'y1' : self.y1 + y,
                            'x2' : self.x2 + x,
                            'y2' : self.y2 + y,
                            'thickness' : self.thickness,
                            'clearance' : self.clearance,
                            'flags' : self.flags})

    def make_shape(self):
        l = shapely.geometry.LineString([(self.x1, self.y1), 
                                         (self.x2, self.y2)])        
        self.shape = l.buffer(self.thickness / 2, SHAPELY_BUF_PTS)


    
class GEDAPCBLayer(GEDAPCBBase):
    type = 'layer'
    attr_list = ('layer_num', 'name', 'children')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)


    def __str__(self):
        ret = 'Layer(%d "%s")' % \
            (self.layer_num, self.name)
        ret += '\n'
        ret += '(\n'
        for c in self.children:
            ret += '\t' + str(c) + '\n'
        ret += ')'

        return ret

    def transform(self, x, y, r):
        return GEDAPCBLayer(
            {'layer_num' : self.layer_num,
             'name' : self.name,
             'children' : [c.transform(x, y, r) for c in self.children]})


class GEDAPCBAttribute(GEDAPCBBase):
    type = 'attribute'
    attr_list = ('name', 'value')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        return 'Attribute("%s" "%s")' % (self.name, self.value)

    def transform(self, x, y, r):
        return self



class GEDAPCBFile(GEDAPCBBase):
    type = 'pcbfile'
    attr_list = ('fileversion', 'pcbname', 'sizex', 'sizey', 
                 'step', 'gridoffx', 'gridoffy', 'gridvisible',
                 'cursorx', 'cursory', 'zoom',
                 'minpolyarea', 'thermalscale',
                 'drcbloat', 'drcshrink', 'drcline',
                 'drcsilk', 'drcdrill', 'drcring',
                 'pcbflags', 'groups_str', 'styles_str',
                 'children')

    def __init__(self, data):
        GEDAPCBBase.__init__(self, self.attr_list, data)

    def __str__(self):
        ret = 'FileVersion[%s]\n' % (self.fileversion)
        ret += 'PCB["%s" %d %d]\n' % (self.pcbname, self.sizex, self.sizey)
        ret += 'Grid[%f %d %d %d]\n' % (self.step, self.gridoffx, self.gridoffy,
                                        self.gridvisible)
        ret += 'Cursor[%d %d %f]\n' % (self.cursorx, self.cursory, self.zoom)
        ret += 'PolyArea[%f]\n' % (self.minpolyarea)
        ret += 'Thermal[%f]\n' % (self.thermalscale)
        ret += 'DRC[%d %d %d %d %d %d]\n' % (self.drcbloat, self.drcshrink,
                                             self.drcline, self.drcsilk,
                                             self.drcdrill, self.drcring)
        ret += 'Flags("%s")\n' % self.pcbflags
        ret += 'Groups("%s")\n' % self.groups_str
        ret += 'Styles["%s"]\n' % self.styles_str
        ret += '\n'
        i = 1
        order = [Symbol, Attribute, Via, Element]
        written = [0] * len(self.children)
        for o in order:            
            for j in range(len(self.children)):
                c = self.children[j]
                if not written[j] and isinstance(c, o):
                    ret += str(c) + '\n'
                    written[j] = 1

        for j in range(len(self.children)):
            if not written[j]:
                c = self.children[j]
                ret += str(c) + '\n'
                written[j] = 1


        return ret

    def make_hole(self, x, y, dia):
        nc = GEDAPCBPin({'name' : '', 
                         'x' : 0, 
                         'y' : 0, 
                         'hole_dia' : dia, 
                         'thickness' : dia,
                         'clearance' : 0,
                         'mask' : dia, 
                         'flags' : ['hole'], 
                         'number' : '0'})
        n = GEDAPCBElement({'name' : '', 
                            'desc' : 'INSERTED_HOLE', 
                            'value' : '%f' % dia, 
                            'mx' : x, 
                            'my' : y, 
                            'tx' : x, 
                            'ty' : y, 
                            'tdir' : 0, 
                            'tscale' : 100, 
                            'tflags' : [], 
                            'flags' : [],
                            'children' : [nc]})
        self.children.append(n)

    def add_component(self, fn, name, x, y, side='top'):
        elt = load_element_file(fn)
        elt.mx = x
        elt.my = y
        if side != 'top':
            elt.flags['onsolder'] = True
        self.children.append(elt)
        

    def merge_layer(self, layer, layer_number=None, layer_name=None):
        if layer_number == None and layer_name == None:
            layer_number = layer.layer_num

        found = False
        for c in self.children:
            if isinstance(c, GEDAPCBLayer):
                print c.name, c.layer_num
                if (c.layer_num == layer_number) or (c.name == layer_name):
                    c.children += layer.children
                    found = True
                    break
        if not found:
            self.children.append(layer)


    def include_other_pcb(self, pcb, offsetx=0, offsety=0, rotatation=0):
        if not hasattr(self, 'groups_str') or self.groups_str == '':
            self.groups_str = pcb.groups_str
            print 'setting groups_str = "%s"' % pcb.groups_str
        if not hasattr(self, 'styles_str') or self.styles_str == '':
            self.styles_str = pcb.styles_str

        #FIXME to do - check layers, drc settings same.

        symbols_to_merge = []
        layers_to_merge = []
        for c in pcb.children:
            if isinstance(c, GEDAPCBAttribute) or isinstance(c, GEDAPCBNetList):
                continue
            elif isinstance(c, GEDAPCBLayer):
                nc = c.transform(offsetx, offsety, rotatation)
                layers_to_merge.append(nc)
            elif isinstance(c, GEDAPCBSymbol):
                symbols_to_merge.append(c)
            else:
                nc = c.transform(offsetx, offsety, rotatation)
                self.children.append(nc)

        for s in symbols_to_merge:
            found = False
            for c in self.children:
                if isinstance(c, GEDAPCBSymbol):
                    if c.name == s.name:
                        found = True
                        break
            if not found:
                self.children.append(s)

        for l in layers_to_merge:
            found = False
            for c in self.children:
                if isinstance(c, GEDAPCBLayer) and c.layer_num == l.layer_num:
                    c.children += l.children
                    found = True
                    break
            if not found:
                self.children.append(l)

                



