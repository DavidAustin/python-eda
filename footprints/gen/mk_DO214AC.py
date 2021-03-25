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

g = FootprintGen('DO214AC')


g.rect_padat(0.0, 0.0, 1.68, 1.52, "1")
g.rect_padat(0.0, -5.28+1.52, 1.68, 1.52, "2")


my = (-5.28+1.52)/2
g.outline(-1.4, my-2, -1.4, my+2, 0.15)
g.outline(1.4, my-2, 1.4, my+2, 0.15)

g.outline(1.4, my-2, 1.0, my-2, 0.15)
g.outline(1.4, my-2.1, 1.0, my-2.1, 0.15)
g.outline(-1.4, my-2, -1.0, my-2, 0.15)
g.outline(-1.4, my-2.1, -1.0, my-2.1, 0.15)

g.write()
