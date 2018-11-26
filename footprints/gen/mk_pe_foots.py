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

data = {
    '0201' : [0.75, 0.30, 0.30, 0.30, 0.20, 1.10, 0.50],
    '0402' : [1.50, 0.50, 0.50, 0.60, 0.10, 1.90, 1.00],
    '0603' : [2.10, 0.90, 0.60, 0.90, 0.50, 2.35, 1.45],
    '0805' : [2.60, 1.20, 0.70, 1.30, 0.75, 2.85, 1.90],
    '1206' : [3.80, 2.00, 0.90, 1.60, 1.60, 4.05, 2.25],
    '1218' : [3.80, 2.00, 0.90, 4.80, 1.40, 4.20, 5.50],
    '2010' : [5.60, 3.80, 0.90, 2.80, 3.40, 5.85, 3.15],
    '2512' : [7.00, 3.80, 1.60, 3.50, 3.40, 7.25, 3.85]
}

data = {
    '0100' : [0.48, 0.12, 0.18, 0.2],
    '0201' : [1.0, 0.3, 0.35, 0.4],
    '0402' : [1.5, 0.5, 0.5, 0.6],
    '0603' : [2.6, 0.8, 0.9, 0.8],
    '0805' : [3.0, 1.2, 0.9, 1.2], 
    '1206' : [4.2, 2.2, 1.0, 1.5],
    '1210' : [4.2, 2.2, 1.0, 2.4],
    '1218' : [4.2, 2.2, 1.0, 4.8],
    '2010' : [6.1, 3.3, 1.4, 2.4],
    '2512' : [8.0, 4.4, 1.8, 3.0]
}

csx = 1.0
csy = 1.1

for k in data.keys():
    
    a, b, c, d = data[k]

    g = FootprintGen('pei%s' % k)

    g.rect_padat(0, 0, c, d, '1')
    
    g.rect_padat(c + b, 0, c, d, '2')

    cx = (c + b) / 2
    cy = 0
    oo = 0.25
    
    g.outlinerect(cx - a / 2 * csx - oo, cy - d / 2 * csy - oo, 
                  cx + a / 2 * csx + oo, cy + d / 2 * csy + oo, 0.15)
    
    g.write()
