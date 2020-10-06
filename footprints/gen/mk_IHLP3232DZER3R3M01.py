# Python-EDA
# Copyright (C) 2020 Luke Cole
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

g = FootprintGen('IHLP3232DZER3R3M01')

part_w = 8.18
part_h = 8.18

pad_w = (9.652 - 4.826) / 2.0
pad_h = 5.334

p = 9.652 - pad_w

g.rect_padat(0, 0, pad_w, pad_h, '1')
g.rect_padat(p, 0, pad_w, pad_h, '2')

ox1 = (part_w - p) / 2
oy1 = part_h / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.write()
