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

g = FootprintGen("DFN8_25x25_PAD")

w = 0.25
h = 0.7
px = 0.5

y = 0.0
x = 0.0
for i in range(1,5):
    g.rect_padat(x, y, w, h, str(i))
    x += px

y = -2.5
x = 3 * px
for i in range(5,9):
    g.rect_padat(x, y, w, h, str(i))
    x -= px

g.rect_padat(1.5*px, -2.5/2, 1.8, 1.1, '0')
g.outline(1.5*px -2.5/2, -2.5, 1.5*px-2.5/2, 0.0,0.1)
g.outline(1.5*px +2.5/2, -2.5, 1.5*px+2.5/2, 0.0,0.1)
g.outline(1.5*px-2.5/2, 0.4, 1.5*px-2.5/2, 0.4, 0.3)
g.write()
