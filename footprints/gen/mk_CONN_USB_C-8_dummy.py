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

# based on https://www.digikey.com/en/products/detail/gct/USB4110-GF-A/10384547

g = FootprintGen('CONN_USB_C-8_dummy')

h = 1.15 - 0.3
w = 0.3

px = 0.5
px1 = 0.65
px2 = 0.8
py = -0.5 - 1.15 / 2.0

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

# alignment holes

p = 5.79
d = 0.65
a = 1.0524

g.pinat(p / 2.0, 0, d, a, '0')
g.pinat(-p / 2.0, 0, d, a, '0')

# ground pads

p = 10.22
y = -0.5
w = 2.18
h = 2

g.rect_padat(-p / 2.0, y, w, h, '0')
g.rect_padat(p / 2.0, y, w, h, '0')

y += 3.93

g.rect_padat(-p / 2.0, y, w, h, '0')
g.rect_padat(p / 2.0, y, w, h, '0')

# outline

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

