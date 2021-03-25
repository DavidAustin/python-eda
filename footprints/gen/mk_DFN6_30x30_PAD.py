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

g = FootprintGen("DFN6_30x30_PAD")

w = 0.45
h = 0.75
px = 0.95
py = 3.1 - 2*0.5 + h
y = 0.0
x = 0.0
for i in range(1,4):
    g.rect_padat(x, y, w, h, str(i))
    x += px

y = -py
x = 2 * px
for i in range(4,7):
    g.rect_padat(x, y, w, h, str(i))
    x -= px

g.rect_padat(1.0*px, -py/2, 2.5, 1.75, '0')
g.outline(1.0*px -3.0/2, -py/2-3.0/2, 1.0*px-3.0/2,  -py/2+3.0/2, 0.1)
g.outline(1.0*px +3.0/2,  -py/2-3.0/2, 1.0*px+3.0/2, -py/2+3.0/2, 0.1)
g.outline(1.0*px-3.0/2, 0.6, 1.0*px-3.0/2, 0.6, 0.4)
g.write()
