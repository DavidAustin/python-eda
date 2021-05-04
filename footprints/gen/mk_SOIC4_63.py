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

g = FootprintGen('SOIC4_63')

part_w = 2.6
part_h = 4.55

w = 0.8
h = 1.2
px = 1.27
py = 6.3


x = 0
y = 0
for i in range(1,3):
    g.rect_padat(x, y, w, h, str(i))
    x += px

y -= py
x -= px
for i in range(3,5):
    g.rect_padat(x, y, w, h, str(i))
    x -= px

ox1 = (-part_w + px) / 2
oy1 = -py / 2 + part_h/2

ox2 = part_w + ox1
oy2 = -part_h + oy1

g.outlinerect(ox1, oy1, ox2, oy2)

g.outline(-0.75, 0.0, -0.75, 0.0, 0.5)

g.write()
