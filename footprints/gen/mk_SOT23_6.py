# Python-EDA
# Copyright (C) 2018 Luke Cole (ported), David Austin (original author)
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

g = FootprintGen('SOT23_6')

p = 0.95
w = 0.6
h = 1.2
py = 2.9

x = 0.0
y = 0.0
for i in range(1,4):
    g.rect_padat(x, y, w, h, '%d' % i)
    x += p

x = 2 * p
y = -py
for i in range(4,7):
    g.rect_padat(x, y, w, h, '%d' % i)
    x -= p

ox1 = p - 3.0/2
oy1 = -0.7
ox2 = ox1 + 3.0
oy2 = -py + 0.7

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
