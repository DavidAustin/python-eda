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

g = FootprintGen('CD-1206-SMT')

# physical part dimensions (not including pins)
part_dia = 12
pin_count_side = 4 # number of pins on left side counting vertically

# pin dimensions
w = 3.0
h = 3.0

g.rect_padat(0.0, 0.0, w, h, '1')
g.rect_padat(0.0, 14, w, h, '2')

g.outlinecirc(0.0, part_dia / 2 + 1, part_dia / 2)

#g.outline(-3.5, -0.75, -3.5, 0.75)
#g.outline(-3.5, -0.75, -2, -0.75)
#g.outline(-3.5, 0.75, -2, 0.75)

g.write()
