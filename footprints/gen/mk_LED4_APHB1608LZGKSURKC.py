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

import math
from footprintgen import *

g = FootprintGen('LED4_APHB1608LZGKSURKC')

#For this LED, 1 * 3 are anode/positive

pad_w = 0.5
pad_h = 0.4

pad_gap_x = 1.7 - 0.5 # between centers
pad_gap_y = 1.1 - 0.4 # between centers

g.rect_padat(pad_gap_x / 2, pad_gap_y / 2, pad_w, pad_h, '1')
g.rect_padat(pad_gap_x / 2, -pad_gap_y / 2, pad_w, pad_h, '3')

g.rect_padat(-pad_gap_x / 2, -pad_gap_y / 2, pad_w, pad_h, '4')
g.rect_padat(-pad_gap_x / 2, pad_gap_y / 2, pad_w, pad_h, '2')

part_w = 1.6
part_h = 0.8

ox1 = -(part_w) / 2.0
oy1 = -part_h / 2.0
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
