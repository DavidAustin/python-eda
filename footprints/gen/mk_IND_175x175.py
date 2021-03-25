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

g = FootprintGen("IND_175x175")


g.rect_padat(0.0, 0.0, 12.5, 3.15, "1")
g.rect_padat(0.0, -12.2-3.15, 12.5, 3.15, "2")


ow = 17.5
oh = 17.5
oy1 = 2.15/2
g.outline(-ow/2, oy1, -ow/2, oy1 - oh, 0.15)
g.outline(ow/2, oy1, ow/2, oy1 - oh, 0.15)

g.write()
