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

def make_it(n_pins):
    g = FootprintGen('CONN%d_330_VERT' % n_pins)

    p = 3.3
    x = 0#p * (n_pins-1)
    y = 0
    od = 1.8
    g.pinat(x, y, 1.0, od,  1, {'square' : 1})
    x += p
    for i in range(2, n_pins+1):
        g.pinat(x, y, 1.0, od,  i)
        x += p


    ow = p * (n_pins-1) + 2.45 * 2 + 0.2
    ox1 = -2.45
    ox2 = ox1 + ow
    oy1 = -2.35
    oy2 = oy1 + 5.75
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    oy3 = oy2 - 0.3
    g.outline(ox1, oy3, ox2, oy3, 0.1)
    #oy4 = oy1 + 15
    #outline(f, ox1, oy4, ox2, oy4, 0.1)

    g.write()

for i in range(2,21):
    make_it(i)


