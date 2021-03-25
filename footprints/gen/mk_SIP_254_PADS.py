# Python-EDA
# Copyright (C) 2019 David Austin
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
    g = FootprintGen('SIP%d_254_PADS' % n_pins)

    p = 2.54
    x = 0.0
    y = 0
    od = 1.6
    g.rect_padat(x, y, od, od,  1)
    x += p
    for j in range(2,n_pins+1):
        g.padat(x, y, od, od,  j)
        x += p

    ow = n_pins * p
    ox1 = - p/2
    ox2 = ox1 + ow
    oh = p
    oy1 = -p/2
    oy2 = oy1 + oh
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    g.write()


for n in range(2, 21):
    make_it(n)
