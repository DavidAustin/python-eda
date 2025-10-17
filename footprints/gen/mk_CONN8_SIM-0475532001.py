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

# http://www.assmann-wsw.com/uploads/datasheets/ASS_4888_CO.pdf

import math
from footprintgen import *

g = FootprintGen('CONN8_SIM-0475532001')

part_w = 19.35
part_h = 26.3

pad_x = 1.0
pad_y = 2.3

p = 1.27
x = 0
y = 0

g.rect_padat(x, y, pad_x, pad_y, "1")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "5")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "2")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "6")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "3")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "7")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "4")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "8")

x_edge = x

pad_x = 1.5
pad_y = 2.95

x = x_edge - 4.37
y = 20.7
g.rect_padat(x, y, pad_x, pad_y, "0")
x += 20.55
g.rect_padat(x, y, pad_x, pad_y, "0")

dia = 1.4

x = x_edge - 4.37 + 2.11
y = 21.47
g.holeat(x, y, dia)

x = x_edge - 4.37 + 18.16
y = 11.67
g.holeat(x, y, dia)

ox1 = x_edge - 3.77
oy1 = -2.3 / 2.0 + 0.6
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

g.write()
