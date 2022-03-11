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

# HHXD500ARA150MF80G from
# https://www.chemi-con.co.jp/products/relatedfiles/capacitor/catalog/HXDRA-e.PDF

import math
from footprintgen import *

g = FootprintGen('HHXD500ARA150MF80G')

part_w = 6.3
part_h = 6.3

w = 1.0
h = (7.2 - 1.9) / 2.0
px = 0
py = 1.9 + h

g.rect_padat(0.0, 0.0, w, h, '1') # +
g.rect_padat(0.0, py, w, h, '2')

ox1 = (part_w - px) / 2.0
oy1 = -(part_h - py) / 2.0

ox2 = ox1 - part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.outline(0.0, -2.0, 0.0, -2.0, 0.4)

g.write()


