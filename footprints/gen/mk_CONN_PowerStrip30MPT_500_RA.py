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

# designed for both Weidmuller and more cost-effective Wurth Elektronik connectors
# e.g.
# https://www.digikey.com/en/products/detail/samtec-inc/MPT-08-01-01-T-RA-SD/10218439
# https://www.digikey.com/en/products/detail/samtec-inc/MPS-08-7-70-01-L-V/2685334
# https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6239/mpsx-mptx.pdf
# https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6129/mpt-xx-01-xx-x-ra-xx-mkt.pdf
# https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6129/mps-xx-x.xx-xx-x-v-xx-mkt.pdf

def make_connector(n_pins):
    g = FootprintGen('CONN%d_PowerStrip30MPT_500_RA' % n_pins)
    
    p = 5.00
    x = p * (n_pins-1)
    y = 0
    id = 0.85
    od = id * 2.0

    pp = 1.88
    
    g.pinat(x - pp / 2, y, id, od, 1, {'square' : 1})
    g.pinat(x + pp / 2, y, id, od, 1, {'square' : 1})

    g.pinat(x - pp / 2, y + 2.54, id, od, 1, {'square' : 1})
    g.pinat(x + pp / 2, y + 2.54, id, od, 1, {'square' : 1})
    
    g.pinat(x - pp / 2, y + 2.54 * 2, id, od, 1, {'square' : 1})
    g.pinat(x + pp / 2, y + 2.54 * 2, id, od, 1, {'square' : 1})

    x -= p
    for i in range(2,n_pins+1):
        g.pinat(x - pp / 2, y, id, od,  i)
        g.pinat(x + pp / 2, y, id, od,  i)
        g.pinat(x - pp / 2, y + 2.54, id, od,  i)
        g.pinat(x + pp / 2, y + 2.54, id, od,  i)
        g.pinat(x - pp / 2, y + 2.54 * 2, id, od,  i)
        g.pinat(x + pp / 2, y + 2.54 * 2, id, od,  i)
        x -= p

    # outline
        
    w = p * (n_pins) + 7.55
    h = 14.81

    ox1 = -(w - p * (n_pins-1)) / 2.0
    oy1 = -1.0
    ox2 = ox1 + w
    oy2 = oy1 + h
    
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

    # cut-in
    
    oy3 = y + 2.54 * 2 + 3.25
    g.outline(ox1, oy3, ox2, oy3, 0.1)

    # holes
    
    P = 6.28 + p * (n_pins)

    id = 3.6
    od = id * 1.1
    g.holeat(ox1 + (w - P) / 2, oy1 + 14.81 - 12.27, id)
    g.holeat(ox2 - (w - P) / 2, oy1 + 14.81 - 12.27, id)
        
    g.write()

for i in range(2,21):
    make_connector(i)


