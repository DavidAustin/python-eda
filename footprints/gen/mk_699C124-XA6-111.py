# Python-EDA
# Copyright (C) 2024 Luke Cole
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

# based on https://www.digikey.co.uk/en/products/detail/edac-inc/699C124-2A6-111/17186511

g = FootprintGen('699C124-2A6-111')

h = 0.9
w = 0.3

px = 0.5
py = -1.5/2

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

px = 0.5
py = 1.5/2

g.rect_padat(-px / 2.0 - px * 5, py, w, h, 'B1')
g.rect_padat(-px / 2.0 - px * 4, py, w, h, 'B2')
g.rect_padat(-px / 2.0 - px * 3, py, w, h, 'B3')
g.rect_padat(-px / 2.0 - px * 2, py, w, h, 'B4')
g.rect_padat(-px / 2.0 - px * 1, py, w, h, 'B5')
g.rect_padat(-px / 2.0, py, w, h, 'B6')
g.rect_padat(px / 2.0, py, w, h, 'B7')
g.rect_padat(px / 2.0 + px * 1, py, w, h, 'B8')
g.rect_padat(px / 2.0 + px * 2, py, w, h, 'B9')
g.rect_padat(px / 2.0 + px * 3, py, w, h, 'B10')
g.rect_padat(px / 2.0 + px * 4, py, w, h, 'B11')
g.rect_padat(px / 2.0 + px * 5, py, w, h, 'B12')

# alignment holes (ground pins)

p = 7.1
d = 1.07
#d = 0.8
d = 0.9
a = d * 1.2

y = -1.5/2 + (1.07/2+1.15) - (1.35/2+0.7)
g.pinat(p / 2.0, y, d, a, '0')
g.pinat(-p / 2.0, y, d, a, '0')

y = 1.5/2 - ((1.07/2+1.15) - (1.35/2+0.7))
g.pinat(p / 2.0, y, d, a, '0')
g.pinat(-p / 2.0, y, d, a, '0')

# outline

w = 8.25
h = 3.5

ox1 = -w / 2.0
oy1 = -h/2
ox2 = ox1 + w
oy2 = oy1 + h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.write()
