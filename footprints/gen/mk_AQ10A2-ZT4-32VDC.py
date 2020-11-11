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

# https://www.digikey.com/en/products/detail/panasonic-electric-works/AQ10A2-ZT4-32VDC/3992067

g = FootprintGen('AQ10A2-ZT4-32VDC')

d_hole = 1.2
d_ann = d_hole * 1.75

p = 2.54

px = 0
py = 0

g.pinat(px, py, d_hole, d_ann, "1")
px += p * 3
g.pinat(px, py, d_hole, d_ann, "2")
px += p * 5
g.pinat(px, py, d_hole, d_ann, "3")
px += p * 3
g.pinat(px, py, d_hole, d_ann, "4")

d_hole = 3.5
d_ann = d_hole * 1.75

py = -9.1

g.pinat(px / 2.0 - 20.0, py, d_hole, d_ann, "0")
g.pinat(px / 2.0 + 20.0, py, d_hole, d_ann, "0")

# main part

part_w = 33.0
part_h = 12.0

ox1 = px / 2.0 - part_w / 2.0
oy1 = -6.9

ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

# main part heatshink mounting plate

part_w = 54.0
part_h = 2.0

ox1 = px / 2.0 - part_w / 2.0
oy1 = - 6.9

ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

# heatshink

part_w = 58.0
part_h = 30.0

ox1 = px / 2.0 - part_w / 2.0
oy1 = -6.9

ox2 = ox1 + part_w
oy2 = oy1 - part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
