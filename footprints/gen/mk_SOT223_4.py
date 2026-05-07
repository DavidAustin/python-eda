# Python-EDA
# Copyright (C) 2026 Luke Cole
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

g = FootprintGen('SOT223_4')

# https://www.infineon.com/assets/row/public/documents/24/49/infineon-bsp170p-ds-en.pdf

part_w = 6.5
part_h = 3.5

px = 2.3
w = 1.2
h = 1.4
py = 4.8 + 1.4

x = 0.0
y = 0.0
for i in range(1,4):
    g.rect_padat(x, y, w, h, '%d' % i)
    x += px

x = px
y = -py
w = 3.5
i = 4
g.rect_padat(x, y, w, h, '%d' % i)

ox1 = px - part_w / 2.0
oy1 = -part_h / 2.0
ox2 = ox1 + part_w
oy2 = -py + part_h / 2.0

g.outlinerect(ox1, oy1, ox2, oy2)

g.outlinecirc(ox1 + 0.3, oy1 - 0.3, 0.05, 0.2)

g.write()
