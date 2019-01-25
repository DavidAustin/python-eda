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

g = FootprintGen('LEDRGB_PLCC4')

#For this LED, 4 is anode/positive

pad_w = 0.7
pad_h = 0.86

pad_gap_x = 1.5 # between centers
pad_gap_y = 2.64 # between centers

g.rect_padat(-pad_gap_x / 2, -pad_gap_y / 2, pad_w, pad_h, '2')
g.rect_padat(-pad_gap_x / 2, pad_gap_y / 2, pad_w, pad_h, '1')

g.rect_padat(pad_gap_x / 2, -pad_gap_y / 2, pad_w, pad_h, '3')
g.rect_padat(pad_gap_x / 2, pad_gap_y / 2, pad_w, pad_h, '4')

oo_x = 0.3
oo_y = 0.1

ox1 = - pad_w / 2 - pad_gap_x / 2 - oo_x
oy1 = - pad_h / 2 - pad_gap_y / 2 - oo_y

ox2 = pad_gap_x / 2 + pad_w / 2 + oo_x
oy2 = pad_gap_y / 2 + pad_h / 2 + oo_y
g.outlinerect(ox1, oy1, ox2, oy2)

oy0 = oy1 - 0.15
g.outline(ox1, oy0, ox2, oy0, 0.2)

oy3 = oy2 + 0.15
g.outline(ox1, oy3, ox2 - ((ox2 - ox1) / 2), oy3, 0.2)

g.write()
