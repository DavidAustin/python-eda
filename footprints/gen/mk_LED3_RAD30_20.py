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

g = FootprintGen('LED3_RAD30_20')

p = 2.0
x = 0.0
ind = 0.8
od = 1.3
g.pinat(0.0, 0.0, ind, od,  1, {'square' : 1})
g.pinat(p, 0.0, ind, od,  2)
g.pinat(2*p, 0.0, ind, od,  3)

g.write()


