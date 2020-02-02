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

g = FootprintGen('GTS447N101HR')

part_w = 16
part_h = 35.1

pin_w = 6.35 # hole should perhaps be 7.35 or 7.4
pin_h = 0.8 # hole should perhaps be 1.8
pin_tol = 0.5 # so hole is 7.35x1.8

p = 15.4

pad_offset = pin_h + pin_tol * 2
g.rect_padat(0, pad_offset, pin_w + pin_tol * 2, pin_h + pin_tol * 2, '1', {'onsolder' : 2})
g.rect_padat(0, pad_offset + p, pin_w + pin_tol * 2, pin_h + pin_tol * 2, '2', {'onsolder' : 2})

ox1 = -pin_w / 2 - pin_tol
oy1 = -pin_h / 2 - pin_tol
ox2 = ox1 + pin_w + pin_tol * 2
oy2 = oy1 + pin_h + pin_tol * 2
g.outlinerect(ox1, oy1, ox2, oy2)

ox1 = -pin_w / 2 - pin_tol
oy1 = -pin_h / 2 + p - pin_tol
ox2 = ox1 + pin_w + pin_tol * 2
oy2 = oy1 + pin_h + pin_tol * 2
g.outlinerect(ox1, oy1, ox2, oy2)

ox1 = -part_w / 2.0
oy1 = -13.1
ox2 = ox1 + part_w
oy2 = oy1 + part_h
g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
