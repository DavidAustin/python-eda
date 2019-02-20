# Python-EDA
# Copyright (C) 2018-2019 Luke Cole (ported), David Austin (original author)
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

g = FootprintGen('usb_micro_b')

h = 1.35
w = 0.4
py = -3.35 +h/2

g.rect_padat(-2.6/2, py, w, h, '1')
g.rect_padat(-1.3/2, py, w, h, '2')
g.rect_padat(0, py, w, h, '3')
g.rect_padat(1.3/2, py, w, h, '4')
g.rect_padat(2.6/2, py, w, h, '5')

g.pinat(-6.1/2 - 0.5/2, 0, 1.1, 1.6, '0')
g.pinat(6.1/2 + 0.5/2, 0, 1.1, 1.6, '0')

g.rect_padat(-(4.3 + 0.5) / 4.0, 0, (4.3 - 0.5) / 2.0, 1.9, '0')
g.rect_padat((4.3 + 0.5) / 4.0, 0, (4.3 - 0.5) / 2.0, 1.9, '0')

g.rect_padat(-(8 + 4.8) / 4.0, -3.35 +1.35+0.25-1.4/2,(8 - 4.8) / 2.0, 1.4, '0')
g.rect_padat((8 + 4.8) / 4.0, -3.35 +1.35+0.25-1.4/2,(8 - 4.8) / 2.0, 1.4, '0')

#ox1 = px/2 -3.1
#ox2 = ox1 + 6.2
#oy1 = py/2 - 3.1
#oy2 = oy1 + 6.2

#g.outline(ox1, oy1, ox2, oy1)
#g.outline(ox1, oy2, ox2, oy2)

g.write()

