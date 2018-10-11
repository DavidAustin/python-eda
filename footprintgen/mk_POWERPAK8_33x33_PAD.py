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

g = FootprintGen("POWERPAK8_33x33_PAD")

w = 0.99
h = 0.405

py = 0.66
px = 3.86 - w

g.rect_padat(0,     0, w, h, 'S')
g.rect_padat(0,   py, w, h, 'S')
g.rect_padat(0, 2*py, w, h, 'S')
g.rect_padat(0, 3*py, w, h, 'G')

g.rect_padat(px,     0, w, h, 'D')
g.rect_padat(px,   py, w, h, 'D')
g.rect_padat(px, 2*py, w, h, 'D')
g.rect_padat(px, 3*py, w, h, 'D')

g.rect_padat(w/2 + 0.635 + 1.725/2, 1.5 * py, 1.725, 2.235, 'D')

g.write()
