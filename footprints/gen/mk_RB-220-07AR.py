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

g = FootprintGen('RB-220-07A')

pad_w = 1
pad_h = 0.8

hole = 0.9
ann = 1.5

g.viaat(0, 0, hole, ann, '1')
g.viaat(1.6, -1.75, hole, ann, '2')

part_w = 6.5
part_h = 4

ox1 = part_w / 2
oy1 = part_h / 2 + 1.75 / 2
ox2 = part_w / 2
oy2 = part_h / 2 - 1.75 / 2

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.write()
