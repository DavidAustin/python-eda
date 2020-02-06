# Python-EDA
# Copyright (C) 2018-2020 Luke Cole
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

g = FootprintGen('EC2-3NU')

d_hole = 1
d_ann = 2

py = 5.08

# https://content.kemet.com/datasheets/KEM_R700

g.pinat(0.0, 0.0, d_hole, d_ann, "1")
g.pinat(0.0, py, d_hole, d_ann, "12")

g.pinat(5.08, 0.0, d_hole, d_ann, "3")
g.pinat(5.08 + 2.54, 0.0, d_hole, d_ann, "4")
g.pinat(5.08 + 2.54 * 2, 0.0, d_hole, d_ann, "5")

g.pinat(5.08, py, d_hole, d_ann, "10")
g.pinat(5.08 + 2.54, py, d_hole, d_ann, "9")
g.pinat(5.08 + 2.54 * 2, py, d_hole, d_ann, "8")

part_w = 7.3
part_l = 15

ox1 = -1.05
oy1 = -1.11

ox2 = ox1 + part_l
oy2 = oy1 + part_w

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
