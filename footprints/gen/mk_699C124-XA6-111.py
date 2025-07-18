# Python-EDA
# Copyright (C) 2025 Luke Cole
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

# settings for array of pins
spacing = 0.01
d = 0.3
a = 0.4

px = 0.5
py = -1.5/2

y = py

x = -px / 2.0 - px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A1')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A2')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A3')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A4')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A5')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A6')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A7')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A8')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A9')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A10')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A11')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h / 2, a, h * 2, 'A12')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

px = 0.5
py = 1.5/2

y = py

x = -px / 2.0 - px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B12')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B11')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B10')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B9')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0 - px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B8')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = -px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B7')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B6')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 1
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B5')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 2
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B4')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 3
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B3')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 4
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B2')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

x = px / 2.0 + px * 5
ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h / 2, a, h * 2, 'B1')
xx = (ox2 - ox1) / 2 + ox1
current_y = oy1
index = 0
while current_y <= oy2:
    g.pinat(xx, current_y, d, a, f'{index}')
    current_y += spacing
    index += 1

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
