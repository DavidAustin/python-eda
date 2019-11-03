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

g = FootprintGen('WQFN16_3x3_PAD')

manual_soldering_ext = 0.1

wx = 3.8
wy = 3.8

padw = 0.23
padh = 0.85
pitch = 0.5
M = 0.1
pad_from_cent = wx / 2.0 - M - 0.4/2

g.rect_padat(pitch * 1.5, - pad_from_cent, 1.7, 1.7, 0)

x = 0
y = 0
for i in range(1, 5):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    x += pitch

x = pitch * 1.5 + pad_from_cent
y = -pad_from_cent + pitch * 1.5
for i in range(5, 9):
    g.rect_padat(x, y, padh, padw, '%d' % i)
    y -= pitch

x = pitch * 1.5 + pitch * 1.5
y = - 2 * pad_from_cent
for i in range(9, 13):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    x -= pitch

x = pitch * 1.5 - pad_from_cent
y = -pad_from_cent - pitch * 1.5

for i in range(13, 17):
    g.rect_padat(x, y, padh, padw, '%d' % i)
    y += pitch



ox1 = 1.5 * pitch - wx/2.0
oy1 = -pad_from_cent + wy/2.0
oo = 0.25
ox2 = ox1 + wx
oy2 = oy1 - wy
ood = 0.3

g.outline(ox1, oy1, ox1 + oo, oy1)
g.outline(ox1, oy1, ox1, oy1 - oo)
g.outline(ox2, oy1, ox2 - oo, oy1)
g.outline(ox2, oy1, ox2, oy1 - oo)

g.outline(ox1, oy2, ox1 + oo, oy2)
g.outline(ox1, oy2, ox1, oy2 + oo)
g.outline(ox2, oy2, ox2 - oo, oy2)
g.outline(ox2, oy2, ox2, oy2 + oo)

g.outline(ox1, oy1 + ood, ox1, oy1 + ood, 0.3)

g.write()
