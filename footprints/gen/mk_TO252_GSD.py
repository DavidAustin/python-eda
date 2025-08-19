# Python-EDA
# Copyright (C) 2020-2025 Luke Cole
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

g = FootprintGen('TO252_GSD')

w = 6.22+1.27
h = 6.73

pad_w = 3
pad_h = 1.6

g.rect_padat(0, 0, 6.2, 5.8, 'D')

g.rect_padat(6.2/2+2.58+3/2, (6.17-1.6)/2, pad_w, pad_h, 'G')
g.rect_padat(6.2/2+2.58+3/2, -(6.17-1.6)/2, pad_w, pad_h, 'S')

ox1 = -w / 2
oy1 = -h / 2

ox2 = ox1 + w
oy2 = oy1 + h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
