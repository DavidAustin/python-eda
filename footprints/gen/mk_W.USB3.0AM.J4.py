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
a = d * 1.5

px = 2.0
py = -1.58/2

# SuperSpeed data transmission (USB3.0)
g.pinat(-px / 2 - px, py, d, a, '1')
g.pinat(-px / 2, py, d, a, '2')
g.pinat(px / 2, py, d, a, '3')
g.pinat(px / 2 + px, py, d, a, '4')

px = 2.0
py = 1.58/2

#  USB 2.0 interface
g.pinat(-px * 2, py, d, a, '5')
g.pinat(-px, py, d, a, '6')
g.pinat(0, py, d, a, '7')
g.pinat(px, py, d, a, '8')
g.pinat(px * 2, py, d, a, '9')

# alignment holes (ground pins)

p = 12.0

d = 1.4
a = d * 1.4
y = 4.5/2 - 0.5 - 1.4/2 #+ (1.07/2+1.15) - (1.35/2+0.7)
g.pinat(p / 2.0, y, d, a, '0')
g.pinat(-p / 2.0, y, d, a, '0')

d = 0.9
a = d * 1.5
y = 4.5/2 - 0.5 - 1.4 - 0.8 - 0.9/2 #+ (1.07/2+1.15) - (1.35/2+0.7)
g.pinat(p / 2.0, y, d, a, '0')
g.pinat(-p / 2.0, y, d, a, '0')

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
