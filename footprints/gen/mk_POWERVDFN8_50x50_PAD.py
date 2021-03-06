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

g = FootprintGen("POWERVDFN8_50x50_PAD")

w = 1.0
h = 0.5

py = 1.27
px = 5.5

#123 S  4G


g.rect_padat(0,     0, w, h, 'S')
g.rect_padat(0,   py, w, h, 'S')
g.rect_padat(0, 2*py, w, h, 'S')
g.rect_padat(0, 3*py, w, h, 'G')

g.rect_padat(px,     0, w, h, 'D')
g.rect_padat(px,   py, w, h, 'D')
g.rect_padat(px, 2*py, w, h, 'D')
g.rect_padat(px, 3*py, w, h, 'D')

g.rect_padat(px - w/2 - 3.5/2 + 0.1, 1.5 * py, 3.5, 4.25, 'D')

oy = 5.0
ox = 5.0

g.outline(px/2 - ox/2, py * 1.5 - oy/2, px/2 + ox/2, py * 1.5 - oy/2)
g.outline(px/2 - ox/2, py * 1.5 + oy/2, px/2 + ox/2, py * 1.5 + oy/2)
g.write()
