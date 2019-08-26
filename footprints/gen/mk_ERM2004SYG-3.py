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

g = FootprintGen('ERM2004SYG-3')

part_w = 77
part_h = 47

d_hole = 1
d_ann = 1.8

x = 0
y = 0

for i in range(1, 17):
    opts = {}
    if i == 1:
        opts = {'square' : 1 }
    g.pinat(x, y, d_hole, d_ann, i, opts)
    x += 2.54

ox1 = -10
oy1 = -2.5
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

hole_dia = 3.5
hole_ann = 5.5

hole_x_from_edge = ((77-70)/2.0)
hole_y_from_edge = ((47-40)/2.0)

hole_x = ox1 + hole_x_from_edge
hole_y = oy1 + hole_y_from_edge
g.pinat(hole_x, hole_y, hole_dia, hole_ann, '0')
hole_x = ox2 - hole_x_from_edge
hole_y = oy1 + hole_y_from_edge
g.pinat(hole_x, hole_y, hole_dia, hole_ann, '0')

hole_x = ox1 + hole_x_from_edge
hole_y = oy2 - hole_y_from_edge
g.pinat(hole_x, hole_y, hole_dia, hole_ann, '0')
hole_x = ox2 - hole_x_from_edge
hole_y = oy2 - hole_y_from_edge
g.pinat(hole_x, hole_y, hole_dia, hole_ann, '0')

g.write()
