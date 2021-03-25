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

g = FootprintGen('LED4_27x32')

w = 1.0
h = 1.5
px = h + 0.4
py = 5 - w
g.rect_padat(0.0, 0.0, w, h, '1')
g.rect_padat(px, 0.0, w, h, '2')
g.rect_padat(0.0, -py, w, h, '3')
g.rect_padat(px, -py, w, h, '4')
g.outline(-1.0, 0.0, -1.0, 0.0, 0.4)

g.write()


