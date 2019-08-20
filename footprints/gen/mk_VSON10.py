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

g = FootprintGen('VSON10')

part_w = 3
part_h = 3

pin_count_side = 5

w = 0.6
h = 0.24

px = 2.8 # distance between centers
py = 0.5 # distance between centers

for i in range(0, pin_count_side):
    g.rect_padat(0.0, py * i, w, h, i + 1)
for i in range(0, pin_count_side):
    g.rect_padat(px, py * i, w, h, pin_count_side * 2 - i)

w = 1.65
h = 2.4
padx = px / 2
pady = py * 2
g.rect_padat(padx, pady, w, h, '0')

w = 0.25
h = 3.4
padx = px / 2 + 0.25
pady = py * 2
g.rect_padat(padx, pady, w, h, '0')
padx = px / 2 - 0.25
g.rect_padat(padx, pady, w, h, '0')

ox1 = (part_w - px) / 2
oy1 = (part_h - py * (pin_count_side - 1)) / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

# pin1 dot/marker
g.outlinecirc(-ox1 + 0.3, -oy1 + 0.3, 0.05, 0.2)

# pin1 line/marker (x direction)
#g.outline(-ox1, -oy1 + 1.1, ox2, -oy1 + 1.1)

# pin1 line/marker (y direction)
#g.outline(-ox1 + 1.2, -oy1, -ox1 + 1.2, oy2)

g.write()
