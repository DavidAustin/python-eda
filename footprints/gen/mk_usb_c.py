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

# based on https://www.digikey.com/en/products/detail/gct/USB4056-03-A/14638038

g = FootprintGen('usb_c')

h = 0.9
w = 0.3

px = 0.5
py = -(6.65 - 5.64 - h / 2.0)

g.rect_padat(-px / 2.0 - px * 5, py, w, h, 'A1')
g.rect_padat(-px / 2.0 - px * 4, py, w, h, 'A2')
g.rect_padat(-px / 2.0 - px * 3, py, w, h, 'A3')
g.rect_padat(-px / 2.0 - px * 2, py, w, h, 'A4')
g.rect_padat(-px / 2.0 - px * 1, py, w, h, 'A5')
g.rect_padat(-px / 2.0, py, w, h, 'A6')
g.rect_padat(px / 2.0, py, w, h, 'A7')
g.rect_padat(px / 2.0 + px * 1, py, w, h, 'A8')
g.rect_padat(px / 2.0 + px * 2, py, w, h, 'A9')
g.rect_padat(px / 2.0 + px * 3, py, w, h, 'A10')
g.rect_padat(px / 2.0 + px * 4, py, w, h, 'A11')
g.rect_padat(px / 2.0 + px * 5, py, w, h, 'A12')

px = 0.8
py = 5.64 - 4.29 - 0.7
d = 0.4
a = 0.706

g.pinat(-px / 2.0 - px * 3, py, d, a, 'B12')
g.pinat(-px / 2.0 - px * 1, py, d, a, 'B9')
g.pinat(-px / 2.0, py, d, a, 'B7')
g.pinat(px / 2.0, py, d, a, 'B6')
g.pinat(px / 2.0 + px * 1, py, d, a, 'B4')
g.pinat(px / 2.0 + px * 3, py, d, a, 'B1')

px = 0.8
py += 0.7
d = 0.4
a = 0.706

g.pinat(-px * 3, py, d, a, 'B11')
g.pinat(-px * 2, py, d, a, 'B10')
g.pinat(-px * 1, py, d, a, 'B8')
g.pinat(px * 1, py, d, a, 'B5')
g.pinat(px * 2, py, d, a, 'B3')
g.pinat(px * 3, py, d, a, 'B2')

# alignment holes

p = 7.2
d = 0.65
a = 0.96

g.pinat(p / 2.0, 0, d, a, '0')
g.pinat(-p / 2.0, 0, d, a, '0')

# ground pins

p = 8.26
y = 5.64 - 4.4
d = 1.1
a = 1.7

g.pinat(-p / 2.0, y, d, a, '0')
g.pinat(p / 2.0, y, d, a, '0')

p = 8.98
y = 5.64

g.pinat(-p / 2.0, y, d, a, '0')
g.pinat(p / 2.0, y, d, a, '0')

# outline

w = 9.85
h = 9.87

ox1 = -w / 2.0
oy1 = -(9.87 - 5.64 - 2.53)
ox2 = ox1 + w
oy2 = oy1 + h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.write()

