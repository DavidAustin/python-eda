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

# settings

fp_name = 'SOD123'
# https://www.taiwansemi.com/assets/uploads/datasheet/1N4148W-G_D1601.pdf

# physical part dimensions (not including pins)
part_w = 1.6
part_h = 2.7
two_sides = False
pin_count_yside = 2 # number of pins on vertical side

# pin dimensions
w = 0.95
h = 0.9
px = 0 # distance between centre of pins
py = 4.05 - h # distance between centre of pins

# pin1 marker settings
pin1_depth = 0.3
pin1_option = 'x_line'

# shouldn't have to edit below this line

g = FootprintGen(fp_name)

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
elif pin2_option == 'y_line':
    g.outline(-ox1 + pin1_depth, -oy1, -ox1 + pin1_depth, oy2)

g.write()
