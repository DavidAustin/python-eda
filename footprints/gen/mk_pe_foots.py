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

def make_fp(k, data, pol = False):
    a, b, c, d = data
    # width, gap, pad_w, pad_h

    if pol:
        g = FootprintGen('pei%s_pol' % k)
    else:
        g = FootprintGen('pei%s' % k)

    g.rect_padat(0, 0, c, d, '1')
    
    g.rect_padat(c + b, 0, c, d, '2')

    cx = (c + b) / 2
    cy = 0
    oo = 0.25

    csx = 1.0
    csy = 1.1
    
    g.outlinerect(cx - a / 2 * csx - oo, cy - d / 2 * csy - oo, 
                  cx + a / 2 * csx + oo, cy + d / 2 * csy + oo, 0.15)

    if pol:

        ox1 = -c - 0.25
        oy1 = oo
        ox2 = -c - 0.25
        oy2 = -oo        
        g.outline(ox1, oy1, ox2, oy2)

        ox1 = -c - 0.25 - oo
        oy1 = 0
        ox2 = -c - 0.25 + oo
        oy2 = 0
        g.outline(ox1, oy1, ox2, oy2)
        
    g.write()

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

# e.g. 1uF 50V tan T491C105M050AT - https://content.kemet.com/datasheets/KEM_T2005_T491.pdf
# e.g. 1206 LEDs - https://www.sunledusa.com/products/spec/XZMDKCBD55W-4.pdf
# e.g. 0603 LEDs - https://www.we-online.de/katalog/datasheet/150060RS75000.pdf
# e.g. 0402 cap (case K) - https://www.vishay.com/docs/40065/298d298w.pdf
data_pol = {
    '2312' : [6.0, 3.2, 1.4, 2.4],
    '1206' : [4.2, 2.2, 1.0, 1.5],
    '0603' : [2.6, 0.8, 0.9, 0.8],
    '0402' : [1.5, 0.5, 0.5, 0.6],
}

for k in data.keys():
    make_fp(k, data[k])

for k in data_pol.keys():
    make_fp(k, data_pol[k], True)
