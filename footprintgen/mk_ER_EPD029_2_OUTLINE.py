# Python-EDA
# Copyright (C) 2018 David Austin
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

g = FootprintGen("ER_EPD029_2_OUTLINE")

w = 79.0
h = 36.7


g.outlinerect(0,0,w,h)


g.outline(w, 12.8, w + 14.3 - 7.55, 12.8)

g.outline(w + 14.3 - 7.55, 11.77, w + 14.3-3, 11.77)
g.outline(w + 14.3 - 3, 11.77, w + 14.3-3, 11.77+12.5)
g.outline(w + 14.3 - 3, 11.77+12.5, w + 14.3-7.55, 11.77+12.5)

g.write()
