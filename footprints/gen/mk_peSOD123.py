# Python-EDA
# Copyright (C) 2018 Luke Cole (ported), David Austin (original author)
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

# https://www.taiwansemi.com/assets/uploads/datasheet/1N4148W-G_D1601.pdf
# https://assets.nexperia.com/documents/data-sheet/PDZ-GW_SER.pdf

part_w = 1.6
part_h = 2.69

w = 0.91
h = 1.22
px = 0 # distance between centre of pins
py = 3.27 # distance between centre of pins

g = FootprintGen('peSOD123')

# NOTE: this order is based on gschem built-in diodes symbols
g.rect_padat(0.0, 0.0, w, h, 2)
g.rect_padat(0.0, py, w, h, 1)

ox1 = (part_w - px) / 2
oy1 = (part_h - py * 1) / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outline(-ox1, -oy1 + 0.5, ox2, -oy1 + 0.5)

g.write()
