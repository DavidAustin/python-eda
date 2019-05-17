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

g = FootprintGen('1206_3')

w = 1.1
h = 1

g.rect_padat(0, 0, w, h, '1')

w = 1.1
h = 0.8

g.rect_padat(-3.55, 0.55, w, h, '2')
g.rect_padat(-3.55, -0.55, w, h, '3')

ox1 = 0.225
oy1 = 1
ox2 = ox1 - 4
oy2 = -1

g.outlinerect(ox1, oy1, ox2, oy2)
g.outlinecirc(ox1 + 0.3, oy1 - 0.3, 0.05, 0.2)

g.write()
