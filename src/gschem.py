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

import pyparsing as pp


class GSCHEM_Base(object):
    attr_list = []
    string_attrs = ('basename',)
    list_attrs = ('children',)
    int_attrs = ('version', 'fileversion', 
                 'x1', 'y1', 'x2', 'y2', 'color', 'width', 'capstyle',
                 'dashstyle', 'dashlength', 'dashspace',
                 'x', 'y', 'linewidth', 
                 'filltype', 'fillwidth', 
                 'angle1', 'pitch1', 'angle2', 'pitch2',
                 'startangle', 'sweepangle', 
                 'size', 'visibility', 'show_name_value',
                 'angle', 'alignment', 'num_lines',
                 'ripperdir',
                 'pintype', 'whichend',
                 'selectable', 'angle', 'mirror',
                 'graphical')
   
    def __init__(self, data):
        #print data
        for a in self.attr_list:
            self.set_and_convert_attr(a, data)

    def set_and_convert_attr(self, a, data):
        if a in self.string_attrs:
            setattr(self, a, data.get(a, ''))
        elif a in self.int_attrs:
            setattr(self, a, int(data.get(a, 0)))
        elif a in self.list_attrs:
            v = data.get(a, [])
            if len(v) == 1 and (isinstance(v[0], list) or 
                                isinstance(v[0], pp.ParseResults)):
                v = v[0]
            setattr(self, a, v)
        elif a == 'attrib':
            v = data.get(a, [])
            if len(v) == 1 and (isinstance(v[0], list) or 
                                isinstance(v[0], pp.ParseResults)):
                v = v[0]
            self.children = []
            self.attrib = {}
            self.attrib_data = {}
            for e in v:
                ass = e.children[0]
                if ass.find('=') > 0:
                    ass = ass.split('=', 1)
                    self.attrib[ass[0]] = ass[1]
                    self.attrib_data[ass[0]] = GschemText(e.asDict())
                    self.attrib_data[ass[0]].children = []
        else:
            setattr(self, a, data.get(a, None))


    def asDict(self):
        ret = {}
        for a in self.attr_list:
            ret[a] = getattr(self, a)
        return ret

    def attrib_str(self):
        if len(self.children) or len(self.attrib):
            c = self.children[:]
            for k in sorted(self.attrib.keys()):
                self.attrib_data[k].children = ['%s=%s' % (k, self.attrib[k])]
                c.append(self.attrib_data[k])
            return '\n{\n' + '\n'.join(map(str, c)) + '\n}'
        else:
            return ''

class GschemVersion(GSCHEM_Base):
    attr_list = ('version', 'fileversion')

    def __str__(self):
        return 'v %d %d' % (self.version, self.fileversion)


class GschemLine(GSCHEM_Base):
    attr_list = ('x1', 'y1', 'x2', 'y2', 'color', 'linewidth', 'capstyle',
                 'dashstyle', 'dashlength', 'dashspace',
                 'attrib')
    

class GschemBox(GSCHEM_Base):
    attr_list = ('x', 'y', 'width', 'height', 'color', 'linewidth', 'capstyle',
                 'dashstyle', 'dashlength', 'dashspace',
                 'filltype', 'fillwidth', 
                 'angle1', 'pitch1', 'angle2', 'pitch2',
                 'attrib')
    

class GschemCircle(GSCHEM_Base):
    attr_list = ('x', 'y', 'radius', 'color', 'linewidth', 'capstyle',
                 'dashstyle', 'dashlength', 'dashspace',
                 'filltype', 'fillwidth', 
                 'angle1', 'pitch1', 'angle2', 'pitch2',
                 'attrib')

class GschemArc(GSCHEM_Base):
    attr_list = ('x', 'y', 'radius', 'startangle', 'sweepangle',
                 'color', 'linewidth', 'capstyle',
                 'dashstyle', 'dashlength', 'dashspace',
                 'attrib')

class GschemText(GSCHEM_Base):
    attr_list = ('x', 'y', 'color', 'size', 'visibility', 'show_name_value',
                 'angle', 'alignment', 'num_lines', 'children')

    def __str__(self):
        ret = 'T %d %d %d %d %d %d %d %d %d\n' % (self.x, self.y,
                                                  self.color,
                                                  self.size,
                                                  self.visibility,
                                                  self.show_name_value,
                                                  self.angle, 
                                                  self.alignment,
                                                  len(self.children))
        ret += '\n'.join(map(str, self.children))
        return ret
                                                  

class GschemNet(GSCHEM_Base):
    attr_list = ('x1', 'y1', 'x2', 'y2', 'color', 'attrib')

    def __str__(self):
        ret = 'N %d %d %d %d %d' % (self.x1, self.y1, self.x2, self.y2,
                                    self.color)
        ret += self.attrib_str()
        return ret


class GschemBus(GSCHEM_Base):
    attr_list = ('x1', 'y1', 'x2', 'y2', 'color', 'ripperdir',
                 'attrib')


class GschemPin(GSCHEM_Base):
    attr_list = ('x1', 'y1', 'x2', 'y2', 'color', 'pintype', 'whichend',
                 'attrib')

class GschemLine(GSCHEM_Base):
    attr_list = ('x1', 'y1', 'x2', 'y2', 'color', 'width', 'capstyle', 
                 'dashstyle', 'dashlength', 'dashspace')

class GschemBox(GSCHEM_Base):
    attr_list = ('x', 'y', 'width', 'height', 'color', 'width', 'capstyle', 
                 'dashstyle', 'dashlength', 'dashspace', 'filltype',
                 'fillwidth', 'angle1', 'pitch1', 'angle2', 'pitch2')

class GschemCircle(GSCHEM_Base):
    attr_list = ('x', 'y', 'radius', 'color', 'width', 'capstyle', 
                 'dashstyle', 'dashlength', 'dashspace', 'filltype',
                 'fillwidth', 'angle1', 'pitch1', 'angle2', 'pitch2')


class GschemComponent(GSCHEM_Base):
    attr_list = ('x', 'y', 'selectable', 'angle', 'mirror', 'basename',
                 'attrib')
    
    def __str__(self):
        ret = 'C %d %d %d %d %d %s' % (self.x, self.y, self.selectable,
                                       self.angle, self.mirror, self.basename)
        ret += self.attrib_str()
        return ret


class GschemFile(GSCHEM_Base):
    attr_list = ('ver', 'children')
    
    def __str__(self):
        ret = str(self.ver)
        
        ret += '\n' + '\n'.join(map(str, self.children))
        return ret
    

class GschemSymbol(GSCHEM_Base):
    attr_list = ('device', 'graphical', 'description',
                 'author', 'comment', 'numslots',
                 'slotdef', 'footprint', 'documentation',
                 'refdes', 'slot', 'value', 'symversion',
                 'dist-license', 'use-license')

    def __init__(self, gsh_file):
        for c in gsh_file.children:
            if isinstance(c, GschemText):
                for c2 in c.children:
                    if c2.find('=') > 0:
                        k,v = c2.split('=', 1)
                        if k in self.attr_list:
                            self.set_and_convert_attr(k, {k : v})
        #print self.__dict__
        


