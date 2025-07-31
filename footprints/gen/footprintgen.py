# Python-EDA
# Copyright (C) 2018-2019 David Austin
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

import math
from pcbutil import *

class FootprintGen(object):

    FG_DEFAULTS = {
        'clearance' : 0.16 #mm
    }
    

    def __init__(self, name):
        self.name = name
        self.lines = []

    def write(self, fn=None):
        if fn is None:
            fn = self.name + '.fp'

        f = open(fn, 'w')
        #f.write('Element[0x0 "" "" "" %d %d -4000 -20000 0 100 ""]\n' \
        f.write('Element[0x0 "" "" "" %d %d 0 0 0 100 ""]\n' \
                % (frommm(0),
                   frommm(0)))
        f.write('(\n')

        f.write('\t' + '\n\t'.join(self.lines) + '\n')
        f.write(')\n')
        self.lines = []
        
    def pinat(self, x, y, d_hole, d_ann, name, opts={}):
        clearance = self.FG_DEFAULTS['clearance']
        opts_str = make_flags_str(opts)
        (x, y, d_hole, d_ann) = map(frommm, (x, y, d_hole, d_ann))
        self.lines.append(
            'Pin[%d %d %d %d %d %d "" "%s" "%s"]' %
            (x, y, d_ann, frommm(clearance), 
             d_ann + frommm(clearance), d_hole, name,
             opts_str))

    def viaat(self, x, y, d_hole, d_ann, name):
        clearance = self.FG_DEFAULTS['clearance']
        (x, y, d_hole, d_ann) = map(frommm, (x, y, d_hole, d_ann))
        self.lines.append('Pin[%d %d %d %d %d %d "" "%s" 0x00]' %
                          (x, y, d_ann, frommm(clearance), 
                           frommm(0.0), d_hole, name))

    def holeat(self, x, y, d_hole):
        clearance = self.FG_DEFAULTS['clearance']
        (x, y, d_hole) = map(frommm, (x, y, d_hole))
        self.lines.append('Pin[%d %d %d %d %d %d "-" "-" "hole"]' %
                          (x, y, d_hole + frommm(clearance), 
                           frommm(clearance), 
                           d_hole + frommm(clearance), d_hole))
         
    def rect_padat(self, x, y, w, h, name, opts={}):
        clearance = self.FG_DEFAULTS['clearance']
        opts['square'] = 1
        opts_str = make_flags_str(opts)
        if h > w:
            width = frommm(w)
            x1 = x2 = frommm(x)
            y1 = frommm(y - h/2.0)
            y2 = frommm(y + h/2.0)
            y1 += width / 2
            y2 -= width / 2
            self.lines.append('Pad[%d %d %d %d %d 2000 %d "" "%s" "%s"]' %
                    (x1, y1, x2, y2, width, width + frommm(clearance),
                     name, opts_str))
        else:
            height = frommm(h)
            x1 = frommm(x - w/2.0)
            x2 = frommm(x + w/2.0)
            y1 = y2 = frommm(y)
            x1 += height / 2
            x2 -= height / 2
            self.lines.append('Pad[%d %d %d %d %d 2000 %d "" "%s" "%s"]' %
                              (x1, y1, x2, y2, height,
                               height + frommm(clearance),
                               name, opts_str))

    def padat(self, x, y, w, h, name, opts={}):
        clearance = self.FG_DEFAULTS['clearance']
        opts_str = make_flags_str(opts)
        if h > w:
            width = frommm(w)
            x1 = x2 = frommm(x)
            y1 = frommm(y - h/2.0)
            y2 = frommm(y + h/2.0)
            y1 += width / 2
            y2 -= width / 2
            self.lines.append('Pad[%d %d %d %d %d 2000 %d "" "%s" "%s"]' %
                              (x1, y1, x2, y2, width,
                               width + frommm(clearance),
                               name, opts_str))
        else:
            height = frommm(h)
            x1 = frommm(x - w/2.0)
            x2 = frommm(x + w/2.0)
            y1 = y2 = frommm(y)
            x1 += height / 2
            x2 -= height / 2
            self.lines.append('Pad[%d %d %d %d %d 2000 %d "" "%s" "%s"]' %
                    (x1, y1, x2, y2, height, height + frommm(clearance),
                     name, opts_str))

    def round_pad_at(self, x, y, r, name, opts={}):
        self.padat(x,y,r,r,name,opts)
        
    def one_rounded_padat(self, x, y, w, h, name, opts={}):
        d = opts['dir']
        del opts['dir']
        self.padat(x, y, w, h, name, opts)
        opts['square'] = 1
        r = (math.fabs(d[1] * w) + math.fabs(d[0] * h))/2.0
        self.padat(x-d[0]*r, y-d[1]*r, 
              w-math.fabs(d[0])*2.0*r, h-math.fabs(d[1])*2.0*r, name, opts)


    def chamfered_rect_padat(self, x, y, w, h, name, opts={}):
        chamfer = opts.get('chamfer', w/2)
        chamfer_corner = opts.get('chamfer-corner', 'top-left')

        if chamfer_corner == 'top-left':
            cx = -1
            cy = -1
        elif chamfer_corner == 'top-right':
            cx = 1
            cy = -1
        elif chamfer_corner == 'bottom-left':
            cx = -1
            cy = 1 
        elif chamfer_corner == 'bottom-right':
            cx = 1
            cy = 1
        else:
            raise RuntimeError

        pads = []

        full_length_pad_width = w - chamfer
        full_length_pad = (x - cx * (w/2 - full_length_pad_width/2),
                            y, full_length_pad_width,
                           h)
        pads.append(full_length_pad)
        short_pad = (x + cx * (w/2 - chamfer/2), y - cy * (chamfer/2),
                     chamfer, h - chamfer)
        pads.append(short_pad)

        patch_size = min(w - chamfer, h - chamfer)
        n = int(math.ceil(chamfer / patch_size))
        step = chamfer / n
        #print n
        xx = x + cx * (w/2 - step/2)
        for i in range(n):
            yy = y + cy * (h/2 + step/2 - step * n)
            for j in range(i):
                pads.append((xx,
                             yy,
                             step,
                             step))
                yy += cy * step    
            xx -= cx * step

        for px,py,pw,ph in pads:
            self.rect_padat(px, py, pw, ph, name)

        sqrt2 = math.sqrt(2.0)
        diag_width = step / sqrt2
        popts = {'square' : 1}
        opts_str = make_flags_str(popts)
        xx = x + cx * w/2
        yy = y + cy * (h/2 - step * n)
        for i in range(n):
            x1, y1 = xx-cx*diag_width/sqrt2, yy
            x2, y2 = x1-cx*step/2, yy+cy*step/2
            x1, y1, x2, y2 = map(frommm, (x1, y1, x2, y2))
            self.lines.append(
                'Pad[%d %d %d %d %d 2000 %d "" "%s" "%s"]' %
                (x1, y1, x2, y2, frommm(diag_width), frommm(diag_width + 0.1),
                     name, opts_str))
            yy += cy * step    
            xx -= cx * step



    def arc_pad_at(self, x, y, r1, r2, a1, a2, name, nsteps=180):
        a = math.radians(a1)
        r = (r1 + r2)/2
        popts = {'square' : 1}
        opts_str = make_flags_str(popts)
        l = 2*math.pi*r2 / nsteps + 0.01
        w = r2 - r1
        #print 'want l,w', l,w
        if l > w:
            l = l - w
            radial = False
        else:
            radial = True
            l,w = (w - l, l)
            
        #print 'using l,w', l, w, radial
        all_a = [a]
        while a < math.radians(a2):
            all_a.append(a)
            a += math.radians(360)/nsteps
        all_a.append(math.radians(a2))
        #all_a = all_a[0:1]
        for a in all_a:
            px = x + r * math.cos(a)
            py = y + r * math.sin(a)
            #print px, py, math.degrees(a), l
            tx = -math.sin(a)/2
            ty = math.cos(a)/2

            if not radial:
                self.lines.append(
                    'Pad[%d %d %d %d %d 2000 %d "" "%s" "%s"]' %
                    (frommm(px + tx*l), frommm(py + ty*l),
                     frommm(px - tx*l), frommm(py - ty*l),
                     frommm(w), frommm(w+ 0.1),
                     name, opts_str))
            else:
                self.lines.append(
                    'Pad[%d %d %d %d %d 2000 %d "" "%s" "%s"]' %
                    (frommm(px + ty*l), frommm(py - tx*l),
                     frommm(px - ty*l), frommm(py + tx*l),
                     frommm(w), frommm(w+ 0.1),
                     name, opts_str))
                
        
        

    def outline(self, x1, y1, x2, y2, w=0.1):
        self.lines.append(
            'ElementLine [%d %d %d %d %d]' % (frommm(x1), frommm(y1),
                                              frommm(x2), frommm(y2),
                                              frommm(w)))


    def outlinerect(self, ox1, oy1, ox2, oy2, w=0.1):
        self.outline(ox1, oy1, ox2, oy1, w)
        self.outline(ox1, oy2, ox2, oy2, w)
        self.outline(ox1, oy1, ox1, oy2, w)
        self.outline(ox2, oy1, ox2, oy2, w)


    def outlinecirc(self, x, y, r, w=0.1, opts={}):
        start_ang = opts.get('start_angle', 0)
        arc_ang = opts.get('arc_angle', 360)

        self.lines.append(
            'ElementArc [%d %d %d %d %d %d %d]' % (frommm(x), frommm(y),
                                                   frommm(r), frommm(r),
                                                   start_ang, arc_ang,
                                                   frommm(w)))

    def outlineplus(self, x, y, size=0.5):
        ox1 = x - size
        oy1 = y
        ox2 = x + size
        oy2 = y
        self.outline(ox1, oy1, ox2, oy2)
        
        ox1 = x
        oy1 = y - size
        ox2 = x
        oy2 = y + size
        self.outline(ox1, oy1, ox2, oy2)

