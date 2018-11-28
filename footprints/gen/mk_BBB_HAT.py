# Python-EDA
# Copyright (C) 2018 Luke Cole
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

# https://www.probotix.com/wiki/images/thumb/9/96/Beaglebone_dimensions.jpg/500px-Beaglebone_dimensions.jpg
# http://www.jechavarria.com/wp-content/uploads/2014/05/BeagleBone_Black_Dimensions_04.png

g = FootprintGen('BBB_HAT')

pin_hole = 1.0
pin_ann = 1.8

p = 2.54 # between pins

rows = 23
cols = 2

# connector 900 pins & outline

pin_name = 0
for y in range(0, rows):
    for x in range(0, cols):
        pin_name = pin_name + 1
        
        if pin_name == 1:
            opts = {'square' : 1 }
        else:
            opts = None
        g.pinat(x * p, y * p, pin_hole, pin_ann, pin_name + 900, opts)
        x = x + 1
    y = y + 1

oo = 1.23
ox1 = - oo
oy1 = - oo
ox2 = p * (cols - 1) + oo
oy2 = p * (rows - 1) + oo
g.outlinerect(ox1, oy1, ox2, oy2)

# connector 800 pins & outline

connector_gap = 45.72 + p
pin_name = 0
for y in range(0, rows):
    for x in range(0, cols):
        pin_name = pin_name + 1
        
        if pin_name == 1:
            opts = {'square' : 1 }
        else:
            opts = None
        g.pinat(connector_gap + x * p, y * p, pin_hole, pin_ann, pin_name + 800, opts)
        x = x + 1
    y = y + 1

oo = 1.23
ox1 = connector_gap - oo
oy1 = - oo
ox2 = connector_gap + p * (cols - 1) + oo
oy2 = p * (rows - 1) + oo
g.outlinerect(ox1, oy1, ox2, oy2)

# board outline

part_width = 54.61
part_height = 86.36
ox1 = - (part_width - connector_gap) / 2 + p / 2
oy1 = -19.685
ox2 = connector_gap + (part_width - connector_gap) / 2 + p / 2
oy2 = part_height - 19.685
g.outlinerect(ox1, oy1, ox2, oy2)

# board mounting

g.pinat(ox1 + 3.18, 14.61 - 19.685, 3.0, 6.0, '0')
g.pinat(ox1 + 6.35, 14.61 - 19.685 + 66.1, 3.0, 6.0, '0')

g.pinat(ox2 - 3.18, 14.61 - 19.685, 3.0, 6.0, '0')
g.pinat(ox2 - 6.35, 14.61 - 19.685 + 66.1, 3.0, 6.0, '0')

g.write()
