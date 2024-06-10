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

# http://www.on-shore.com/wp-content/uploads/2018/04/302-SXX1.pdf - 404, try this one:
# https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6025/302-S.pdf

def make_connector(n_pins):
    g = FootprintGen('CONN%d_254_DUAL' % n_pins)
    
    p = 2.54
    x = 0
    y = 0
    dia = 1.02
    od = dia * 1.75
    g.pinat(0, y + p, dia, od,  1, {'square' : 1})
    g.pinat(0, y, dia, od,  2)
    x += p
    for i in range(3, n_pins + 1, 2):
        g.pinat(x, y + p, dia, od,  i)
        g.pinat(x, y, dia, od,  i + 1)
        x += p
    
    p_len = (n_pins / 2.0 - 1) * p
    C = p_len + (58.4 - 48.26)
    oy = (9.05 - p) / 2.0
    ox = (C - p_len) / 2.0
    
    ox1 = -ox
    oy1 = -oy
    ox2 = p_len + ox
    oy2 = p + oy
    
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
    g.write()

for i in range(2,41):
    if i % 2 == 0:
        make_connector(i)


