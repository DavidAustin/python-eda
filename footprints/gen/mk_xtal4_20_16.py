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

manual_soldering_ext = 0.75

g = FootprintGen('XTAL4_20_16')

w = 1
h = 0.9
px = 0.75 + 0.6 + (w - 0.75)
py = 0.7 + 0.3 + (h - 0.7)
g.rect_padat(0.0, 0.0, w, h, "1")
g.rect_padat(px, 0.0, w, h, "3")
g.rect_padat(0.0, -py, w, h, "3")
g.rect_padat(px, -py, w, h, "2")

oo = 0.07
ox1 = 0.0 - 1.7 / 2
oy1 = 0.0 - 3.2 / 2
ox2 = 2.0 + 1.7
oy2 = oy1 + 3.2

#g.outlinerect(ox1 - oo, oy1 - oo, ox2 + oo, oy2 + oo)

g.outline(-0.8, 0.0,  -0.8, 0.0, 0.3)

g.write()
