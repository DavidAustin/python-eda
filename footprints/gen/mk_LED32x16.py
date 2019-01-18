# Python-EDA
# Copyright (C) 2018 Luke Cole (ported), David Austin (original author)
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

g = FootprintGen('LED32x16')

#For leds, 1 is anode/positive

w = 1.75
h = 1.5

g.rect_padat(0, 0, w, h, '1')
g.rect_padat(2 + w, 0, w, h, '2')

oo = 0.2
ox1 = -w / 2 - oo
ox2 = w + 2 + w / 2 + oo
oy1 = -h / 2 - oo
oy2 = h / 2 + oo

g.outlinerect(ox1, oy1, ox2, oy2)

ox3 = ox2 + 0.1

g.outline(ox3, oy1, ox3, oy2)

g.write()
