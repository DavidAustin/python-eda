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

g = FootprintGen('MJ-3536N')

pin_hole_dia = 3
pin_ann = 5

# left side
g.pinat(0, 0, pin_hole_dia, pin_ann, '1')

# center
g.pinat(11.2+2.5, 0, pin_hole_dia, pin_ann, '2')
g.pinat(11.2, 5.2, pin_hole_dia, pin_ann, '3')

g.outlinerect(-(13.5-11.2), -10.0/2.0, 11.2+2.5, 10.2/2.0)

g.write()
