# Python-EDA
# Copyright (C) 2018 Luke Cole
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

g = FootprintGen('SSOP20-5.3mm')

part_w = 5.3
part_h = 7.2

pin_count_side = 10

w = 1
h = 0.4
px = 7.8 - 0.75
py = 0.65

for i in range(0, pin_count_side):
    g.rect_padat(0.0, py * i, w, h, i + 1)
for i in range(0, pin_count_side):
    g.rect_padat(px, py * i, w, h, pin_count_side * 2 - i)

ox1 = (part_w - px) / 2
oy1 = (part_h - py * (pin_count_side - 1)) / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outlinecirc(-ox1 + 0.3, -oy1 + 0.3, 0.05, 0.2)

g.write()
