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

g = FootprintGen('usb_c')

h = 1.15
w = 0.3

px = 0.5
px1 = 0.65
px2 = 0.8
py = -0.5 - h / 2.0

# A row
g.rect_padat(-px / 2.0 - px * 3 - px1 - px2, py, w * 2, h, '1')
g.rect_padat(-px / 2.0 - px * 3 - px1, py, w * 2, h, '2')
g.rect_padat(-px / 2.0 - px * 3, py, w, h, '3')
g.rect_padat(-px / 2.0 - px * 2, py, w, h, '4')
g.rect_padat(-px / 2.0 - px * 1, py, w, h, '5')
g.rect_padat(-px / 2.0, py, w, h, '6')
g.rect_padat(px / 2.0, py, w, h, '7')
g.rect_padat(px / 2.0 + px * 1, py, w, h, '8')
g.rect_padat(px / 2.0 + px * 2, py, w, h, '9')
g.rect_padat(px / 2.0 + px * 3, py, w, h, '10')
g.rect_padat(px / 2.0 + px * 3 + px1, py, w * 2, h, '11')
g.rect_padat(px / 2.0 + px * 3 + px1 + px2, py, w * 2, h, '12')

# B row
g.rect_padat(-px / 2.0 - px * 3 - px1 - px2, py, w * 2, h, '13')
g.rect_padat(-px / 2.0 - px * 3 - px1, py, w * 2, h, '14')
g.rect_padat(-px / 2.0 - px * 3, py, w, h, '15')
g.rect_padat(-px / 2.0 - px * 2, py, w, h, '16')
g.rect_padat(-px / 2.0 - px * 1, py, w, h, '17')
g.rect_padat(-px / 2.0, py, w, h, '18')
g.rect_padat(px / 2.0, py, w, h, '19')
g.rect_padat(px / 2.0 + px * 1, py, w, h, '20')
g.rect_padat(px / 2.0 + px * 2, py, w, h, '21')
g.rect_padat(px / 2.0 + px * 3, py, w, h, '22')
g.rect_padat(px / 2.0 + px * 3 + px1, py, w * 2, h, '23')
g.rect_padat(px / 2.0 + px * 3 + px1 + px2, py, w * 2, h, '24')

x = 2.98
d = 0.65
a = 0.9

g.pinat(x, 0, d, a, '0')
g.pinat(-x, 0, d, a, '0')

h = 2
w = 2.18
x = 5.11
y = -0.5

g.rect_padat(-x, y, w, h, '0')
g.rect_padat(x, y, w, h, '0')

y += 3.93

g.rect_padat(-x, y, w, h, '0')
g.rect_padat(x, y, w, h, '0')

w = 8.34
h = 2.85 + 3.93 + 1.15 / 2.0

ox1 = -w / 2.0
ox2 = ox1 + w
oy1 = -0.5 - 1.15 / 2.0
oy2 = oy1 + h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.write()

