# Python-EDA
# Copyright (C) 2019 Luke Cole
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

def make_connector(n_pins):
    g = FootprintGen('CONN%d_420_DUAL' % n_pins)
    
    p = 4.20
    x = 0
    y = 0
    od = 3.0
    g.pinat(0, y, 1.4, od,  1, {'square' : 1})
    g.pinat(0, y + p, 1.4, od,  2)
    x += p
    for i in range(3, n_pins + 1):
        if i % 2 == 0:
            g.pinat(x, y, 1.4, od,  i)
            g.pinat(x, y + p, 1.4, od,  i + 1)
            i += 2
            x += p

    ow = p * ((n_pins - 1) / 2) + 3.54 * 2 + 0.2
    ox1 = -3.54
    ox2 = ox1 + ow
    oh = 8.6
    oy1 = -3.8
    oy2 = oy1 + p + oh
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
    oy3 = oy2 - 0.3
    g.outline(ox1, oy3, ox2, oy3, 0.1)

    g.write()

for i in range(4,26):
    if i % 2 == 0:
        make_connector(i)


