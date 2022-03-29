# Python-EDA
# Copyright (C) 2022 Luke Cole
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

# designed for the following (not really a dual, but does have dual pins):
# https://www.digikey.com/en/products/detail/samtec-inc/FHP-04-01-T-S/1106020

def make_connector(n_pins):
    g = FootprintGen('CONN%d_396_DUAL' % n_pins)

    px = 3.96
    py = 2.4638
    x = 0
    y = 0
    d = 1.4
    od = 2.4
    g.pinat(0, y, d, od,  1, {'square' : 1})
    g.pinat(0, y + py, d, od, 1, {'square' : 1})
    x += px
    for i in range(2, n_pins + 1):
        g.pinat(x, y, d, od,  i)
        g.pinat(x, y + py, d, od,  i)
        i += 2
        x += px

    ow = px * (n_pins - 1) + 1.9812 * 2 + 0.2
    ox1 = -1.9812
    ox2 = ox1 + ow
    oy1 = -2.54 + py / 2.0
    oy2 = oy1 + 2.54 * 2
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
    g.write()

for i in range(4,26):
    make_connector(i)


