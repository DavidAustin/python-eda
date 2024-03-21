# Python-EDA
# Copyright (C) 2024 Luke Cole
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
from footprintgen import *

class footprintradial:

    def __init__(self, name):
        self.g = FootprintGen(name)
    
    def make_radial(self, d, p, pad_w, pad_h):

        self.g.rect_padat(-p / 2.0, 0, pad_w, pad_h, 1, {'square' : 1})
        self.g.rect_padat(p / 2.0, 0, pad_w, pad_h, 2)

        self.g.outlinecirc(0, 0, d / 2.0)

        oo = 0.5

        ox = -p / 2.0
        oy = d / 2.0 + oo
        
        ox1 = ox - oo
        oy1 = oy
        ox2 = ox + oo
        oy2 = oy
        self.g.outline(ox1, oy1, ox2, oy2)

        ox1 = ox
        oy1 = oy - oo
        ox2 = ox
        oy2 = oy + oo
        self.g.outline(ox1, oy1, ox2, oy2)

    def write(self):
        self.g.write()

clearance = 0.3

data = {
    '39uF 63V A780KN396M1JLAS040' : [8.0, 3.1 + 4.2, 4.2, 2.2] # https://connect.kemet.com:7667/gateway/IntelliData-ComponentDocumentation/1.0/download/datasheet/A780KN396M1JLAS040
}

# TODO: more port such as mk_HHXD500ARA150MF80G.py

for v in data.values():
    d_ann = v[2] * 1.75
    r = footprintradial('RADIAL_SMT-%.2f-%.2f-%.2f-%.2f' % (v[0], v[1], v[2], d_ann))
    r.make_radial(v[0], v[1], v[2], d_ann)
    r.write()
