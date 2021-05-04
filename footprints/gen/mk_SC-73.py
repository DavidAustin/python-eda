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

g = FootprintGen("SC-73")

w = 1.2
h = 1.2

py = 6.1
px = 2.3

g.rect_padat(0,        0, w, h, 'B')
g.rect_padat(px,       0, w, h, 'C')
g.rect_padat(2 * px,   0, w, h, 'E')
g.rect_padat(px,     -py, 6.7, 1.9, 'C')

g.write()
