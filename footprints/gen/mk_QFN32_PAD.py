# Python-EDA
# Copyright (C) 2019 Luke Cole (ported), David Austin (original author)
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

manual_soldering_ext = 0.1

g = FootprintGen('QFN32_PAD')

wx = 5.0
wy = 5.0

tpadw = 3.45
tpadh = 3.45

padw = 0.23
padh = 0.8
pitch = 0.5
cx = 3.5 * pitch
cy = padh/2.0 - 5.75/2.0
x = 0
y = 0
for i in range(1, 9):
    g.one_rounded_padat(x, y, padw, padh, '%d' % i, {'dir' : (0, -1)})
    x += pitch

x = cx + 5.75/2.0 - padh/2.0
y = cy + 3.5 * pitch
for i in range(9, 17):
    g.one_rounded_padat(x, y, padh, padw, '%d' % i, {'dir' : (-1, 0)})
    y -= pitch


x = 7 * pitch
y = -(5.75 - padh)
for i in range(17, 25):
    g.one_rounded_padat(x, y, padw, padh, '%d' % i, {'dir' : (0, 1)})
    x -= pitch

x = cx - (5.75/2.0 - padh/2.0)
y = cy - 3.5 * pitch
for i in range(25, 33):
    g.one_rounded_padat(x, y, padh, padw, '%d' % i, {'dir' : (1, 0)})
    y += pitch


g.rect_padat(cx, cy, tpadw, tpadh, '0')

ox1 = cx - wx/2.0
oy1 = cy + wy/2.0
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
