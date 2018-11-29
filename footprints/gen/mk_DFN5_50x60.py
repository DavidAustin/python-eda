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

g = FootprintGen("DNF5_50x60")

w = 0.75
h = 1.0
px = 1.27

y = - 1.33 - 0.965 - h/2
x = -1.5 *px
for i in range(4):
    g.rect_padat(x, y, w, h, '2')
    x += px

g.rect_padat(0, -1.33 + (4.53 - 0.475)/2, 4.56, 4.53 - 0.475, '1')
#sides
g.rect_padat(-4.56/2 - .495/2 + 0.1, -0.905/2, .495+0.1, 0.905, '1')
g.rect_padat(4.56/2 + .495/2 - 0.1, -0.905/2, .495+0.1, 0.905, '1')
#bottom
wb = 4.56/2 - 1.53
g.rect_padat(-4.56/2 + wb/2, 3.2-0.475/2-0.1, wb, 0.475+0.1, '1')
g.rect_padat(4.56/2 - wb/2, 3.2-0.475/2-0.1, wb, 0.475+0.1, '1')

g.write()
