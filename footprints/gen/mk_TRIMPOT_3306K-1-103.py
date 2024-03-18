# Python-EDA
# Copyright (C) 2024 Luke Cole
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

g = FootprintGen('TRIMPOT_3306K-1-103')

x = 0.0
y = 0.0

g.pinat(0.0, 0.0, 1.0, 2.0, 1)
g.pinat(2.5, -2.5, 1.0, 2.0, 2)
g.pinat(5.0, 0, 1.0, 2.0, 3)

pw = 6.81

ox1 = 2.5 - pw / 2.0
ox2 = 2.5 + pw / 2.0
oy1 = 0.0
oy2 = 4.5

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
