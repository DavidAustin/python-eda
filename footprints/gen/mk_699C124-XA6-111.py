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

h = 0.7
w = 0.3

px = 0.5
py = -1.5/2

y = py

x = -px / 2.0 - px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A1')

x = -px / 2.0 - px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A2')

x = -px / 2.0 - px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A3')

x = -px / 2.0 - px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A4')

x = -px / 2.0 - px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A5')

x = -px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A6')

x = px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A7')

x = px / 2.0 + px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A8')

x = px / 2.0 + px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A9')

x = px / 2.0 + px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A10')

x = px / 2.0 + px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A11')

x = px / 2.0 + px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, 'A12')

px = 0.5
py = 1.5/2

y = py

x = -px / 2.0 - px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B1')

x = -px / 2.0 - px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B2')

x = -px / 2.0 - px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B3')

x = -px / 2.0 - px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B4')

x = -px / 2.0 - px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B5')

x = -px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B6')

x = px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B7')

x = px / 2.0 + px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B8')

x = px / 2.0 + px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B9')

x = px / 2.0 + px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B10')

x = px / 2.0 + px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B11')

x = px / 2.0 + px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, 'B12')

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
