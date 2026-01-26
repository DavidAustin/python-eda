# Python-EDA
# Copyright (C) 2026 Luke Cole
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

# http://www.assmann-wsw.com/uploads/datasheets/ASS_4888_CO.pdf

import math
from footprintgen import *

g = FootprintGen('CONN7_SIM-2336582-1')

part_w = 13 - 0.7
part_h = 13.5

pad_x = 0.8
pad_y = 1.14

p = 1.27
x = 0
y = 0

g.rect_padat(x, y, pad_x, pad_y, "4")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "5")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "1")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "6")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "2")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "7")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "3")

x_edge = x

pad_x = 0.7
pad_y = 2.1

x = x_edge - 1.67
y = 2.05 - 1.14 / 2
g.rect_padat(x, y, pad_x, pad_y, "0")
x += 13.0
g.rect_padat(x, y, pad_x, pad_y, "0")

x = x_edge - 1.67
y += 12.0
g.rect_padat(x, y, pad_x, pad_y, "0")
x += 13.0
g.rect_padat(x, y, pad_x, pad_y, "0")

dia = 0.75

x = x_edge - 1.67 + 1.5
y = 2.05 - 1.14 / 2 + 12 - 1.25
g.holeat(x, y, dia)

x += 8.5
g.holeat(x, y, dia)

ox1 = x_edge - 1.67 + 0.7 / 2
ox2 = ox1 + part_w
oy1 = 1.14 / 2
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

g.write()
