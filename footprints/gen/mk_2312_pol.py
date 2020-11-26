# Python-EDA
# Copyright (C) 2020 Luke Cole
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

data = {
    '2312' : [6.0, 3.2, 1.4, 2.4]
}

csx = 1.0
csy = 1.1

for k in data.keys():
    
    a, b, c, d = data[k]

    g = FootprintGen('pei%s_pol' % k)

    g.rect_padat(0, 0, c, d, '1')
    
    g.rect_padat(c + b, 0, c, d, '2')

    cx = (c + b) / 2
    cy = 0
    oo = 0.25
    
    g.outlinerect(cx - a / 2 * csx - oo, cy - d / 2 * csy - oo, 
                  cx + a / 2 * csx + oo, cy + d / 2 * csy + oo, 0.15)

    oo = 0.5

    ox = -c - 0.25
    oy = 0
    
    ox1 = ox - oo
    oy1 = oy
    ox2 = ox + oo
    oy2 = oy
    g.outline(ox1, oy1, ox2, oy2)
    
    ox1 = ox
    oy1 = oy - oo
    ox2 = ox
    oy2 = oy + oo
    g.outline(ox1, oy1, ox2, oy2)
    
    g.write()
