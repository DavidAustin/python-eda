# Python-EDA
# Copyright (C) 2021 Luke Cole
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

g = FootprintGen('SOT23_GSD')

dx = (1.341 + 2.459) / 2.0
dy = (1.245 + 2.692) / 2.0
px = 1.0
py = 1.2
g.rect_padat(0, 0, px, py, "G")
g.rect_padat(dx, 0, px, py, "S")
g.rect_padat(dx / 2.0, -dy, px, py, "D")

oo = 0.07
#g.outlinerect(-px/2, -py/2 - oo, dx + px/2, -dy + py/2 + oo)
oy = 0.5
g.outlinerect(dx / 2.0 - 3.1/2, -dy/2 + oy/2, dx/2.0 + 3.1/2, -dy/2 - oy/2)

g.write()
