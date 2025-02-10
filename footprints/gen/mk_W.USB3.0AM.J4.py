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

# based on https://www.taobao.com/list/item/661747754877.htm

g = FootprintGen('W.USB3.0AM.J4')

px = 2.0
px2 = 2.5

py = -1.23/2

w = 0.9 + 0.1 * 2
h = 0.3 + 0.1 * 2

pin_w = 0.3 + 0.1 * 2
pin_l = 0.9 + 0.1 * 2

x = -px2 / 2 - px2
y = py

# SuperSpeed data transmission (USB3.0) - slot top

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, '1')

x = -px2 / 2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, '2')

x = px2 / 2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, '3')

x = px2 / 2 + px2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - h, w, h, '4')

py = 1.23/2

#  USB 2.0 interface - slot bottom
# NOTE: should be px (2.0) below as per datasheet/3D model, however real part is px2 (2.5)

x = -px2 * 2
y = py

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, '5')

x = -px2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, '6')

x = 0

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, '7')

x = px2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, '8')

x = px2 * 2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + h, w, h, '9')

# large alignment holes (ground pins) - slot right then left

p = 11.7

x = p / 2.0
y = 4.5/2 - 0.5 - 1.4/2 #+ (1.07/2+1.15) - (1.35/2+0.7)

w = 0.3 + 0.1 * 2
h = 1.4 + 0.1 * 2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x + w, y, w, h, '0')

x = -p / 2.0

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x - w, y, w, h, '0')

# smaller alignment holes (ground pins) - slot right then left

x = p / 2.0
y = 4.5/2 - 0.5 - 1.4 - 0.8 - 0.9/2 #+ (1.07/2+1.15) - (1.35/2+0.7)

w = 0.3 + 0.1 * 2
h = 0.9 + 0.1 * 2

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x + w, y, w, h, '0')

x = -p / 2.0

ox1 = x - w / 2.0
oy1 = y - h / 2.0
ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x - w, y, w, h, '0')

# outline

w = 12.0
h = 4.5

ox1 = -w / 2.0
oy1 = -h/2
ox2 = ox1 + w
oy2 = oy1 + h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.write()
