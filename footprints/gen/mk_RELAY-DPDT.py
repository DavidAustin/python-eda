# Python-EDA
# Copyright (C) 2018 Luke Cole
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

g = FootprintGen('RELAY-DPDT')

d_hole = 1.3
d_ann = 2.5

py = 7.5

g.pinat(0.0, 0.0, d_hole, d_ann, "1")
g.pinat(0.0, py, d_hole, d_ann, "2")

g.pinat(20.3, 0.0, d_hole, d_ann, "3")
g.pinat(20.3 - 5.04, 0.0, d_hole, d_ann, "4")
g.pinat(20.3 + 5.04, 0.0, d_hole, d_ann, "5")

g.pinat(20.3, py, d_hole, d_ann, "3")
g.pinat(20.3 - 5.04, py, d_hole, d_ann, "4")
g.pinat(20.3 + 5.04, py, d_hole, d_ann, "5")

part_w = 12.7
part_l = 29

ox1 = 22.65 - 20.3
oy1 = (part_w - py) / 2

ox2 = part_l - ox1
oy2 = part_w - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.write()
