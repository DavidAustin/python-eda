# Python-EDA
# Copyright (C) 2021 David Austin
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

g = FootprintGen('LGA12_20x20')

part_w = 2.0
part_h = 2.0

p = 0.5
off_y = 0.5125

pad_w = 0.25
pad_h = 0.275

x = 0.0
y = 0.0
for i in range(1, 5):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    x += p

x = p * 3
y = -off_y
for i in range(5, 7):
    g.rect_padat(x, y, pad_h, pad_w, '%d' % i)
    y -= p

y = -(off_y + p + off_y)
for i in range(7, 11):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    x -= p

x = 0
y = -off_y - p
for i in range(11, 13):
    g.rect_padat(x, y, pad_h, pad_w, '%d' % i)
    y += p

ox1 = 1.5 * p - part_w/2
oy1 = -off_y - p/2 + part_h/2

ox2 = ox1 + part_w
oy2 = oy1 - part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.outlinecirc(ox1 - 0.3, oy1 - 0.3, 0.05, 0.2)

g.write()
