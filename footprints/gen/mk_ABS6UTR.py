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

g = FootprintGen('ABS6UTR')

part_w = (5.3 - 4.8) / 2.0 + 4.8
part_h = (4.6 - 4.2) / 2.0 + 4.2

w = 1.0
h = 1.5
px = 4
py = 6.4 - h

g.rect_padat(0.0, 0.0, w, h, '1')
g.rect_padat(-px, 0.0, w, h, '2')

g.rect_padat(-px, py, w, h, '3')
g.rect_padat(0, py, w, h, '4')

ox1 = (part_w - px) / 2.0
oy1 = -(part_h - py) / 2.0

ox2 = ox1 - part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.outline(1.0, 0.0, 1.0, 0.0, 0.4)

g.write()


