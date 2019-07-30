# Python-EDA
# Copyright (C) 2019 Luke Cole
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

g = FootprintGen('LED_XZMRVG67WTR')

w = 4
h = 4

pad_w = 1.7
pad_h = 4

g.rect_padat(-(4.2-1.7)/2, 0, pad_w, pad_h, '1')
g.rect_padat((4.2-1.7)/2, 0, pad_w, pad_h, '2')

ox1 = -w / 2
oy1 = -h / 2

ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)

g.outlinecirc(ox1 + 0.3, oy1 - 0.3, 0.05, 0.2)

g.write()
