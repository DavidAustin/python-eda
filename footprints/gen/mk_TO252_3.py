# Python-EDA
# Copyright (C) 2022 Luke Cole
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

# http://www.smc-diodes.com/propdf/SBRD10200%20N1314%20REV.A.pdf

import math
from footprintgen import *

g = FootprintGen("TO252_3") # aka TO252-3, DPAK (2 Leads + Tab), JEDEC SC-63

w = 1.6
h = 3.5

py = 10.05 - 2.9/2.0 - 6.1/2.0
px = 4.572

g.rect_padat(0,        0, w, h, '1')
g.rect_padat(px/2,   -py, 6.5, 6.1, '2')
g.rect_padat(px,       0, w, h, '3')

g.write()
