# Python-EDA
# Copyright (C) 2018-2020 Luke Cole (ported), David Austin (original author)
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

g = FootprintGen('XDFN3')

C = 0.7
X = 0.7
X1 = 0.25
Y = 0.4
Y2 = 1.1 - 0.3 - Y
cy = (X1-X)/2.0

g.rect_padat(0, 0, Y, X1, "S")
g.rect_padat(0, X1-X, Y, X1, "G")

g.rect_padat(C, cy, Y2, X, "D")

ow = 1 + 0.3
oh = 0.6

ox1 = -ow / 2.0 + C/2.0
oy1 = oh / 2.0+cy
ox2 = ox1 + ow
oy2 = oy1 - oh

oo = 0.07

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

dy = 0.2

g.outline(ox1, oy1 + dy, ox1, oy1 + dy)
            
g.write()
