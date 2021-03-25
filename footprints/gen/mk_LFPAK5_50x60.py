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

g = FootprintGen("LFPAK5_50x60")

w = 0.7
h = 1.15

px = 1.27


y = (3.3 + 2.15)/2
g.rect_padat(-1.5*px, y, w, h, 'S')
g.rect_padat(-0.5*px, y, w, h, 'S')
g.rect_padat( 0.5*px, y, w, h, 'S')
g.rect_padat( 1.5*px, y, w, h, 'G')


g.rect_padat(0, -(1.6-1.1), 4.2, 3.2, 'D')

g.rect_padat(0, -2 - 0.75, 4.7, 1.5, 'D')


oy = 5.0
ox = 5.0

#g.outline(px/2 - ox/2, py * 1.5 - oy/2, px/2 + ox/2, py * 1.5 - oy/2)
#g.outline(px/2 - ox/2, py * 1.5 + oy/2, px/2 + ox/2, py * 1.5 + oy/2)
g.write()
