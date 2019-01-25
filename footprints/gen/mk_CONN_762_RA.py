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


def make_connector(n_pins):
    g = FootprintGen('CONN%d_762_RA' % n_pins)

    
    p = 7.62
    x = p * (n_pins-1)
    y = 0
    od = 5.0
    g.pinat(x, y, 1.6, od,  1, {'square' : 1})
    g.pinat(x, y - p, 1.6, od,  1, {'square' : 1})
    x -= p
    for i in range(2,n_pins+1):
        g.pinat(x, y, 1.6, od,  i)
        g.pinat(x, y - p, 1.6, od,  i)
        x -= p


    ow = p * (n_pins-1) + 3.81 * 2 + 0.2
    ox1 = -3.81
    ox2 = ox1 + ow
    oh = 29.0
    oy1 = 2
    oy2 = oy1 - oh
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

    g.write()

for i in range(2,21):
    make_connector(i)


