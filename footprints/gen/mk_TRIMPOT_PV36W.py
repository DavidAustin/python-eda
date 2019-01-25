# Python-EDA
# Copyright (C) 2019 David Austin
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

g = FootprintGen('TRIMPOT_PV36W')

p = 2.54
py = 2.9

x = 0.0
y = 0.0
for i in range(1,4):
    g.pinat(x, y, 0.6, 1.0, '%d' % i)
    x += p

ox1 = -2.22
oy1 = -2.41
ox2 = ox1 + 9.53
oy2 = oy1 + 4.83

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
