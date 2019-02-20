# Python-EDA
# Copyright (C) 2018-2019 Luke Cole
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

g = FootprintGen('SJ-43515TS')

pin_hole_dia = 1.1
pin_ann = 2

# left side
g.pinat(0, -4.8, pin_hole_dia, pin_ann, '1')
g.pinat(0, 0, pin_hole_dia, pin_ann, '')
g.pinat(0, 4.5, pin_hole_dia, pin_ann, '4')

# center
g.pinat(5, 0, pin_hole_dia, pin_ann, '')
g.pinat(5, 3.6, pin_hole_dia, pin_ann, '2')

# right side
g.pinat(8.1, -1.6, pin_hole_dia, pin_ann, '3')
g.pinat(8.1, 1.6, pin_hole_dia, pin_ann, '5')

oo = 1

g.outlinerect(-2.9, -4.8 - oo, 8.1 + oo, 4.5 + oo)

g.write()
