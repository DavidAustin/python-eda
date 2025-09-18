# Python-EDA
# Copyright (C) 2025 Luke Cole
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

# https://www.diodes.com/assets/Package-Files/SOT323.pdf

import math
from footprintgen import *

g = FootprintGen('SOT323') # aka SOT323/SC70

part_w = 2.2
part_h = 1.35

w = 0.47
h = 0.6

px = 0.65 * 2
py = 2.5 - 0.6

g.rect_padat(0, 0, w, h, 1)
g.rect_padat(-px, 0, w, h, 2)
g.rect_padat(-px / 2.0, py, w, h, 3)

ox1 = part_w - px - (part_w - px) / 2
oy1 = -(part_h - py) / 2.0
ox2 = ox1 - part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
