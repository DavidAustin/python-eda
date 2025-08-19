# Python-EDA
# Copyright (C) 2018-2025 Luke Cole
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

# https://www.diodes.com/assets/Package-Files/SOD123.pdf

import math
from footprintgen import *

g = FootprintGen('DIODE_SOD123')

part_w = 2.65
part_h = 1.55

w = 0.90
h = 0.95

px = 3.15 # distance between centers
g.rect_padat(0.0, 0, w, h, "1")
g.rect_padat(px, 0, w, h, "2")

ox1 = (part_w - px) / 2
oy1 = part_h / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

# pin1 line/marker (y direction)
g.outline(-ox1 + 0.6, -oy1, -ox1 + 0.6, oy2)

g.write()
