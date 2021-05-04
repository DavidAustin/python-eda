# Python-EDA
# Copyright (C) 2020 David Austin
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

g = FootprintGen('SO8_50x50')

part_w = 5.0
part_h = 5.0

w = 1.8
h = 0.55
px = 7.9
py = 1.27


x = 0
y = 0
for i in range(1,5):
    g.rect_padat(x, y, w, h, str(i))
    y += py

x += px
y -= py
for i in range(5,9):
    g.rect_padat(x, y, w, h, str(i))
    y -= py

ox1 = (part_w - px) / 2
oy1 = (part_h - py * (4 - 1)) / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outlinecirc(0, -oy1 - 0.5, 0.05, 0.5)

g.write()
