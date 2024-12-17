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

d = 1.0
a = d * 1.2

px = 2.0
px2 = 2.5

py = -1.23/2

w = d
h = d

pin_w = 0.3 + 0.1 * 2
pin_l = 0.9 + 0.1 * 2

x = -px / 2 - px2
y = py

# SuperSpeed data transmission (USB3.0) - slot top

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - pin_w, w, pin_w, '1')
#g.pinat(-px / 2 - px2, py, d, a, '1')

x = -px / 2

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - pin_w, w, pin_w, '2')
#g.pinat(-px / 2, py, d, a, '2')

x = px / 2

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - pin_w, w, pin_w, '3')
#g.pinat(px / 2, py, d, a, '3')

x = px / 2 + px2

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y - pin_w, w, pin_w, '4')
#g.pinat(px / 2 + px2, py, d, a, '4')

py = 1.23/2

#  USB 2.0 interface - slot bottom

x = -px * 2
y = py

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + pin_w, w, pin_w, '5')
#g.pinat(-px * 2, py, d, a, '5')

x = -px

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + pin_w, w, pin_w, '6')
#g.pinat(-px, py, d, a, '6')

x = 0

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + pin_w, w, pin_w, '7')
#g.pinat(0, py, d, a, '7')

x = px

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + pin_w, w, pin_w, '8')
#g.pinat(px, py, d, a, '8')

x = px * 2

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x, y + pin_w, w, pin_w, '9')
#g.pinat(px * 2, py, d, a, '9')

# large alignment holes (ground pins) - slot right then left

p = 11.7

d = 1.4
a = d * 1.4
y = 4.5/2 - 0.5 - 1.4/2 #+ (1.07/2+1.15) - (1.35/2+0.7)

x = p / 2.0
h = a
pin_l = 0.3 + 0.1 * 2
pin_w = 1.4 + 0.1 * 2

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x + pin_l, y, pin_l, h, '0')
#g.pinat(p / 2.0, y, d, a, '0')

x = -p / 2.0

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x - pin_l, y, pin_l, h, '0')
#g.pinat(-p / 2.0, y, d, a, '0')

# smaller alignment holes (ground pins) - slot right then left

d = 0.9
a = d * 1.5
y = 4.5/2 - 0.5 - 1.4 - 0.8 - 0.9/2 #+ (1.07/2+1.15) - (1.35/2+0.7)

x = p / 2.0
h = a
pin_l = 0.3 + 0.1 * 2
pin_w = 0.9 + 0.1 * 2

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x + pin_l, y, pin_l, h, '0')
#g.pinat(p / 2.0, y, d, a, '0')

x = -p / 2.0

ox1 = x - pin_l / 2.0
oy1 = y - pin_w / 2.0
ox2 = ox1 + pin_l
oy2 = oy1 + pin_w
g.outlinerect(ox1, oy1, ox2, oy2)
g.rect_padat(x - pin_l, y, pin_l, h, '0')
#g.pinat(-p / 2.0, y, d, a, '0')

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
