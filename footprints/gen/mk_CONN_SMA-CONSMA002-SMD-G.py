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

# https://linxtechnologies.com/wp/wp-content/uploads/consma002-smd-g-t-ds.pdf

import math
from footprintgen import *

g = FootprintGen('CONN_SMA-CONSMA002-SMD-G')

part_w = 7.76
part_h = 7.76

pad_x = 2.44 - (4.56 - 2.88) / 2.0
pad_y = 7.76

p = 4.56 + (7.76 - 4.56) / 2.0

g.rect_padat(0, 0, pad_x, pad_y, "1")
g.rect_padat(p, 0, pad_x, pad_y, "2")
g.round_pad_at(p / 2.0, 0, 2.05, "3")

ox1 = -(part_w - p) / 2.0
oy1 = -pad_y / 2.0
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

g.write()
