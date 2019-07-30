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

g = FootprintGen('SRR6038-100Y')

# settings

# physical part dimensions (not including pins)
part_w = 7.3
part_h = 7.3
two_sides = False # set True for IC
pin_count_yside = 2 # number of pins on left side counting vertically

# pin dimensions
w = 7.5
h = 2.8
px = 0 # distance between centre of pins
py = 4.7 # distance between centre of pins

# pin1 marker settings
pin1_depth = 0.3
pin1_option = 'none'

# shouldn't have to edit below this line

for i in range(0, pin_count_yside):
    g.rect_padat(0.0, py * i, w, h, i + 1)
if two_sides == True:
    for i in range(0, pin_count_yside):
        g.rect_padat(px, py * i, w, h, pin_count_yside * 2 - i)

ox1 = (part_w - px) / 2
oy1 = (part_h - py * (pin_count_yside - 1)) / 2

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

if pin1_option == 'dot':
    g.outlinecirc(-ox1 + pin1_depth, -oy1 + pin1_depth, 0.05, 0.2)
elif pin1_option == 'x_line':
    g.outline(-ox1, -oy1 + pin1_depth, ox2, -oy1 + pin1_depth)
elif pin1_option == 'y_line':
    g.outline(-ox1 + pin1_depth, -oy1, -ox1 + pin1_depth, oy2)

g.write()
