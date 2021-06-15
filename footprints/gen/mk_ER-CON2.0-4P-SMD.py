# Python-EDA
# Copyright (C) 2021 Luke Cole
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

g = FootprintGen('ER-CON2.0-4P-SMD')

# https://www.buydisplay.com/download/connector/ER-CON2.0-4P-SMD.pdf

wx = 12.0
wy = 6.0

w = 0.5
h = 2.0

p = 2.0

pin_count = 4

x = 0.0
for i in range(1, pin_count + 1):
    g.rect_padat(x, 0.0, w, h, '%d' % i)
    x += p

ox1 = ((pin_count - 1) * p - wx) / 2.0
oy1 = wy + h / 2.0

ox2 = ox1 + wx
oy2 = oy1 - wy

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
