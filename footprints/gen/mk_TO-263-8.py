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

g = FootprintGen('TO-263-8')

w = 10
h = 9.25

pad_w = 0.8
pad_h = 4.6

p = 0.47 + pad_w

g.rect_padat(0, 0, 10.8, 9.4, '0')

x = -pad_w * 3.5 - 0.47 * 3.0
y = 16.15 - 9.4 / 2.0 - 4.6 / 2.0

for i in range(1, 8):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    x += p

ox1 = -w / 2
oy1 = -h / 2

ox2 = ox1 + w
oy2 = oy1 + h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
