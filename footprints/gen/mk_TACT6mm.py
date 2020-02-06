# Python-EDA
# Copyright (C) 2017-2020 Luke Cole (ported), David Austin (original author)
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

g = FootprintGen('TACT6mm')

x1 = 9.5
x2 = 6.4
w = (x1 - x2) / 2.0
px = (x1 + x2) / 2.0
y1 = 5.8
y2 = 3.2
h = (y1 - y2) / 2.0
py = (y1 + y2) / 2.0

g.rect_padat(0, 0, w, h, '1')
g.rect_padat(px, 0, w, h, '1')

g.rect_padat(0, py, w, h, '2')
g.rect_padat(px, py, w, h, '2')

ox1 = px/2 -3.1
ox2 = ox1 + 6.2
oy1 = py/2 - 3.1
oy2 = oy1 + 6.2

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.write()

