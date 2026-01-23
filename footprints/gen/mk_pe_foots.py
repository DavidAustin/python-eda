# Python-EDA
# Copyright (C) 2018-2014 Luke Cole (ported), David Austin (original author)
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
    # part_length, pad_gap, pad_w, pad_h
    # NOTES:
    # * part_width is defined automatically based on pad_h
    # * pitch/p = pad_gap + pad_w

    print (k, a, b, c, d)
    
    if pol:
        g = FootprintGen('pei%s_pol' % k)
    else:
        g = FootprintGen('pei%s' % k)

    g.rect_padat(0, 0, c, d, '1')
    
    g.rect_padat(c + b, 0.0, c, d, '2')

    cx = (c + b) / 2
    cy = 0
    oo = 0.25

    csx = 1.0
    csy = 1.1
    
    g.outlinerect(cx - a / 2 * csx - oo, cy - d / 2 * csy - oo, 
                  cx + a / 2 * csx + oo, cy + d / 2 * csy + oo, 0.15)

    if pol:

        g.outlineplus(cx - a / 2 * csx - oo - 0.7, 0)
        
    g.write()

# mostly sized by DA using unknown doc
# 2220 - 10uF 100V https://datasheets.kyocera-avx.com/X7RDielectric.pdf
# 1008 - 1uF 3.3A https://www.murata.com/~/media/webrenewal/products/inductor/chip/tokoproducts/wirewoundmetalalloychiptype/m_dfe252012f.ashx
data = {
    '0100' : [0.48, 0.12, 0.18, 0.2],
    '0201' : [1.0, 0.3, 0.35, 0.4],
    '0402' : [1.5, 0.5, 0.5, 0.6],
    '0603' : [2.6, 0.8, 0.9, 0.8],
    '0805' : [3.0, 1.2, 0.9, 1.2], 
    '1008' : [2.5, 1.2, 0.8, 2.0], 
    '1206' : [4.2, 2.2, 1.0, 1.5],
    '1210' : [4.2, 2.2, 1.0, 2.4],
    '1218' : [4.2, 2.2, 1.0, 4.8],
    '1812' : [4.55, 3.45, 1.78, 3.15],
    '2010' : [6.1, 3.3, 1.4, 2.4],
    '2220' : [5.7, 5.0, 1.4, 5.0],
    '2512' : [8.0, 4.4, 1.8, 3.0]
}

# e.g. 2917 150uF 16V tan cap 293D157X9016D2TE3 - https://www.vishay.com/docs/40002/293d.pdf
# e.g. 2312 1uF 50V tan cap T491C105M050AT - https://content.kemet.com/datasheets/KEM_T2005_T491.pdf
# e.g. 1206 LEDs - https://www.sunledusa.com/products/spec/XZMDKCBD55W-4.pdf
# e.g. 0603 LEDs - https://www.we-online.de/katalog/datasheet/150060RS75000.pdf
# e.g. 0402 cap (case K) - https://www.vishay.com/docs/40065/298d298w.pdf
data_pol = {
    '2917' : [7.3, 3.0, 2.5, 4.0],
    '2312' : [6.0, 3.2, 1.4, 2.4],
    '1206' : [4.2, 2.2, 1.0, 1.5],
    '0603' : [2.6, 0.8, 0.9, 0.8],
    '0402' : [1.5, 0.5, 0.5, 0.6],
}

for k in data.keys():
    make_fp(k, data[k])

for k in data_pol.keys():
    make_fp(k, data_pol[k], True)
