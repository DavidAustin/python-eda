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

g = FootprintGen('LEDRGB_PLCC6')

#For this LED - 4, 5, 6 is anode/positive

pad_w = 1
pad_h = 0.8

pad_gap_x = 2.75 # between centers
pad_gap_y = 1 # between centers

g.rect_padat(0, 0, pad_w, pad_h, '1')
g.rect_padat(0, pad_gap_y, pad_w, pad_h, '2')
g.rect_padat(0, pad_gap_y * 2, pad_w, pad_h, '3')

g.rect_padat(pad_gap_x, 0, pad_w, pad_h, '1')
g.rect_padat(pad_gap_x, pad_gap_y, pad_w, pad_h, '2')
g.rect_padat(pad_gap_x, pad_gap_y * 2, pad_w, pad_h, '3')

part_w = 3.4
part_h = 3.4

ox1 = (part_w - pad_gap_x) / 2
oy1 = (part_h - pad_gap_y * 2) / 2
ox2 = pad_gap_x + ox1
oy2 = pad_gap_y * 2 + oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outlinecirc(-0.5, -0.5, 0.05)

g.write()
