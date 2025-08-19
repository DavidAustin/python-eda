# Python-EDA
# Copyright (C) 2020 David Austin
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

g = FootprintGen("TO252_3")

w = 1.2
h = 2.2

py = 10.6 - 6.4/2 - 2.2/2
px = 5.76 - 1.2

g.rect_padat(0,        0, w, h, 'G')
g.rect_padat(px,       0, w, h, 'S')
g.rect_padat(px/2,   -py, 5.8, 6.4, 'D')

g.write()
