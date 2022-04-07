# Python-EDA
# Copyright (C) 2022 Luke Cole
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

# https://www.we-online.com/katalog/datasheet/865080142007.pdf

import math
from footprintgen import *

g = FootprintGen('CAP-SMT-865080142007')

part_w = 5.3
part_h = 5.3

pad_x = 3.0
pad_y = 1.6

p = 1.4 + pad_x

g.rect_padat(0, 0, pad_x, pad_y, "1")
g.rect_padat(p, 0, pad_x, pad_y, "2")

ox1 = -(part_w - p) / 2.0
oy1 = -part_h / 2.0
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

g.outlineplus(ox1 - 1.0, -pad_y)

g.write()
