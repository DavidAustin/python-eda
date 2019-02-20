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

g = FootprintGen('SSOP5')

part_w = 2.9
part_h = 1.6

w = 0.6
h = 1
px = 0.95
py = 2.4

g.rect_padat(0.0, 0.0, w, h, "1")
g.rect_padat(px, 0, w, h, "2")
g.rect_padat(px * 2, 0, w, h, "3")

g.rect_padat(px * 2, -py, w, h, "4")
g.rect_padat(0.0, -py, w, h, "5")

ox1 = -(part_w - px * 2) / 2
oy1 = (part_h - py) / 2

ox2 = part_w + ox1
oy2 = - part_h + oy1

g.outlinerect(ox1, oy1, ox2, oy2)

g.outlinecirc(ox1 + 0.3, oy1 - 0.3, 0.05, 0.2)

g.write()
