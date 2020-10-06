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

g = FootprintGen('LGA14')

part_w = 3.0
part_h = 2.5

p = 0.5

pad_w = 0.475
pad_h = 0.25

center_x = part_w - 0.1 * 2.0 - pad_w
center_y = part_h - 0.1 * 2.0 - pad_h

x = 0
y = 0
for i in range(1, 5):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    y += p

x = (part_w - 0.1 * 2.0 - pad_w) / 2.0 - p
y = p * 1.5 + (part_h - 0.1 * 2.0 - pad_h) / 2.0
for i in range(5, 8):
    g.rect_padat(x, y, pad_h, pad_w, '%d' % i)
    x += p

x = part_w - 0.1 * 2.0 - pad_w
y = p * 3.0
for i in range(8, 12):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    y -= p

x = (part_w - 0.1 * 2.0 - pad_w) / 2.0 + p
y = p * 1.5 - (part_h - 0.1 * 2.0 - pad_h) / 2.0
for i in range(12, 15):
    g.rect_padat(x, y, pad_h, pad_w, '%d' % i)
    x -= p

ox1 = (part_w - (part_w - 0.1 * 2.0 - pad_w)) / 2.0
oy1 = (part_h - p * 3) / 2.0

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outlinecirc(-ox1 - 0.3, -oy1 - 0.3, 0.05, 0.2)

g.write()
