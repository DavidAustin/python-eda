# Python-EDA
# Copyright (C) 2018 Luke Cole (ported), David Austin (original author)
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

values = {
    '0201' : {'a' : 0.75, 'b' : 0.3, 'c' : 0.3, 'd' : 0.3, 'e' : 0.2, 'f' : 1.1, 'g' : 0.5},
    '0402' : {'a' : 1.5, 'b' : 0.5, 'c' : 0.5, 'd' : 0.6, 'e' : 0.1, 'f' : 1.9, 'g' : 1.0},
    '0603' : {'a' : 2.1, 'b' : 0.9, 'c' : 0.6, 'd' : 0.9, 'e' : 0.5, 'f' : 2.35, 'g' : 1.3},
    '0805' : {'a' : 2.6, 'b' : 1.2, 'c' : 0.7, 'd' : 1.3, 'e' : 0.75, 'f' : 2.85, 'g' : 1.9},
    '1206' : {'a' : 3.8, 'b' : 2.0, 'c' : 0.8, 'd' : 1.6, 'e' : 1.6, 'f' : 4.05, 'g' : 2.25},
    '1210' : {'a' : 3.8, 'b' : 2.0, 'c' : 0.9, 'd' : 2.5, 'e' : 3.0, 'f' : 4.05, 'g' : 2.25},
    '2010' : {'a' : 5.6, 'b' : 3.8, 'c' : 0.9, 'd' : 2.8, 'e' : 3.4, 'f' : 5.85, 'g' : 3.15},
    '2016' : {'a' : 5.6, 'b' : 3.8, 'c' : 0.9, 'd' : 4.5, 'e' : 3.4, 'f' : 5.85, 'g' : 5.05},
}

for n in values.keys():
    
    g = FootprintGen('peci%s' % n)

    v = values[n]
    g.rect_padat(0, 0, v['c'], v['d'], '1')

    g.rect_padat(v['c'] + v['b'], 0, v['c'], v['d'], '2')

    oo = 0.05
    cx = (v['c'] + v['b'])/2.0
    cy = 0
    
    ox1 = cx - v['f'] / 2.0 + oo
    ox2 = cx + v['f'] / 2.0 - oo
    oy1 = cy - v['g'] / 2.0 + oo
    oy2 = cy + v['g'] / 2.0 - oo
    
    g.outlinerect(ox1, oy1, ox2, oy2)

    g.write()
