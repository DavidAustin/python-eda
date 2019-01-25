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

g = FootprintGen('VQFN20_PAD')

p = 0.5
w = 0.28
h = 0.85
padw = 3.05
padh = 2.05

cx = 5.3/2.0 - h/2.0
cy = - p * 1.5

g.one_rounded_padat(0, 0, h, w, '1', {'dir' : (1, 0)})
g.one_rounded_padat(0, -3.0*p, h, w, '20', {'dir' : (1, 0)})

x = cx - 3.5 * p
y = cy + 4.3/2.0 - h / 2.0
for i in range(2, 10):
    g.one_rounded_padat(x, y, w, h, '%d' % i, {'dir' : (0, -1)})
    x += p

x = cx + 5.3/2.0 - h / 2.0
g.one_rounded_padat(x, 0, h, w, '10', {'dir' : (-1, 0)})
g.one_rounded_padat(x, -3.0*p, h, w, '11', {'dir' : (-1, 0)})


x = cx + 3.5 * p
y = cy - 4.3/2.0 + h / 2.0
for i in range(12, 20):
    g.one_rounded_padat(x, y, w, h, '%d' % i, {'dir' : (0, 1)})
    x -= p

g.rect_padat(cx, cy, padw, padh, '0')

dh = 0.3
x = dh / 2.0
g.rect_padat(x, -p, h + dh, w, '0')
g.rect_padat(x, -2.0*p, h + dh, w, '0')
x = cx + 5.3/2.0 - h / 2.0 - dh/2.0
g.rect_padat(x, -p, h + dh, w, '0')
g.rect_padat(x, -2.0*p, h + dh, w, '0')

ow = 4.65 + 0.1
oh = 3.65 + 0.1

od = 0.3

ox1 = cx - ow / 2.0
oy1 = cy + oh / 2.0
ox2 = ox1 + ow
oy2 = oy1 - oh

g.outline(ox1, oy1, ox1 + od, oy1)
g.outline(ox1, oy1, ox1, oy1-od)
g.outline(ox1+od, oy1, ox1, oy1-od)

g.outline(ox2, oy1, ox2 - od, oy1)
g.outline(ox2, oy1, ox2, oy1-od)

g.outline(ox1, oy2, ox1 + od, oy2)
g.outline(ox1, oy2, ox1, oy2+od)

g.outline(ox2, oy2, ox2 - od, oy2)
g.outline(ox2, oy2, ox2, oy2+od)

g.write()
