# Python-EDA
# Copyright (C) 2017-2022 Luke Cole
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

g = FootprintGen('CONN30_GEN4LCD')

# physical part dimensions (not including pins)
part_w = 4.4
part_h = 20.93
two_sides = False # set True for IC
pin_count_yside = 30 # number of pins on left side counting vertically

# pin dimensions
w = 3.5
h = 0.35
px = 0 # distance between centre of pins
py = 0.5 # distance between centre of pins

# pin1 marker settings
pin1_depth = 0.3
pin1_option = 'dot'

# shouldn't have to edit below this line

for i in range(0, pin_count_yside):
    g.rect_padat(0.0, py * i, w, h, i + 1)
if two_sides == True:
    for i in range(0, pin_count_yside):
        g.rect_padat(px, py * i, w, h, pin_count_yside * 2 - i)

big_pad_w = 3.1
big_pad_h = 2.3
    
g.rect_padat(0.0, -1.67, big_pad_w, big_pad_h, '0')
g.rect_padat(0.0, py * (pin_count_yside - 1) + 1.67, big_pad_w, big_pad_h, '0')
    
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
