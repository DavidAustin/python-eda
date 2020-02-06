# Python-EDA
# Copyright (C) 2020 Luke Cole
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

g = FootprintGen('VQFN24_PAD')

p = 0.4
p1 = 0.5
w = 0.25
w1 = 0.45
h = 0.25
padw = 1.9
padh = 1.9

cx = p + p1
cy = p * 2 + p1

g.rect_padat(cx, cy, padw, padh, '0')

# top
g.rect_padat(-p, 0, w, h, '24')
g.rect_padat(0, 0, w, h, '1')
g.rect_padat(p, 0, w, h, '2')
g.rect_padat(p + p1, 0, w1, h, '3')
g.rect_padat(p + p1 * 2, 0, w, h, '4')
g.rect_padat(p * 2 + p1 * 2, 0, w, h, '5')
g.rect_padat(p * 3 + p1 * 2, 0, w, h, '6')

# bottom
y = p * 4 + p1 * 2
g.rect_padat(-p, y, w, h, '18')
g.rect_padat(0, y, w, h, '17')
g.rect_padat(p, y, w, h, '16')
g.rect_padat(p + p1, y, w1, h, '15')
g.rect_padat(p + p1 * 2, y, w, h, '14')
g.rect_padat(p * 2 + p1 * 2, y, w, h, '13')
g.rect_padat(p * 3 + p1 * 2, y, w, h, '12')

# left
g.rect_padat(-p, p, h, w, '23')
g.rect_padat(-p, p * 2, h, w, '22')
g.rect_padat(-p, p * 2 + p1, h, w1, '21')
g.rect_padat(-p, p * 2 + p1 * 2, h, w, '20')
g.rect_padat(-p, p * 3 + p1 * 2, h, w, '19')

# right
g.rect_padat(p * 3 + p1 * 2, p, h, w, '7')
g.rect_padat(p * 3 + p1 * 2, p * 2, h, w, '8')
g.rect_padat(p * 3 + p1 * 2, p * 2 + p1, h, w1, '9')
g.rect_padat(p * 3 + p1 * 2, p * 2 + p1 * 2, h, w, '10')
g.rect_padat(p * 3 + p1 * 2, p * 3 + p1 * 2, h, w, '11')

ow = 3.15
oh = 3.15

ox1 = - (ow / 2.0 - (p + p1))
oy1 = - (oh - y) / 2.0
ox2 = ox1 + ow
oy2 = oy1 + oh

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

# pin 1 marker

size = 0.25
g.outline(ox1 + size, oy1, ox1, oy1 + size)

g.write()
