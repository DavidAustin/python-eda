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

g = FootprintGen('TSSOP24_76_PAD')

part_w = 5.6
part_h = 7.8

pin_count_side = 12

w = 1.0
h = 0.3
px = 7.6
py = 0.65

for i in range(0, pin_count_side):
    g.rect_padat(0.0, py * i, w, h, i + 1)
for i in range(0, pin_count_side):
    g.rect_padat(px, py * i, w, h, pin_count_side * 2 - i)


g.rect_padat(px/2,
             py * (float(pin_count_side - 1)/ 2),
             3.4, 5.0, '0')
             
             
ox1 = (part_w - px) / 2
oy1 = (part_h - py * (pin_count_side - 1)) / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outlinecirc(0.0, -0.7, 0.05, 0.3)

g.write()
