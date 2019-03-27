# Python-EDA
# Copyright (C) 2019 Luke Cole
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

w = 14
h = 50

pad_w = 4
pad_h = 6

g = FootprintGen('batt-14500_outside-top')

g.rect_padat(0, 0, pad_w, pad_h, '1')
g.rect_padat(h + pad_w, 0, pad_w, pad_h, '2')

ox1 = pad_w / 2
oy1 = -w / 2

ox2 = pad_w / 2 + h
oy2 = w / 2

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()

g = FootprintGen('batt-14500_outside-bottom')

g.rect_padat(0, 0, pad_w, pad_h, '1', {'onsolder' : 2})
g.rect_padat(h + pad_w, 0, pad_w, pad_h, '2', {'onsolder' : 2})

ox1 = pad_w / 2
oy1 = -w / 2

ox2 = pad_w / 2 + h
oy2 = w / 2

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()

g = FootprintGen('batt-14500_inside-bottom')

g.rect_padat(0, 0, pad_w, pad_h, '1', {'onsolder' : 2})
g.rect_padat(h - pad_w, 0, pad_w, pad_h, '2', {'onsolder' : 2})

ox1 = -pad_w / 2
oy1 = -w / 2

ox2 = h - pad_w / 2
oy2 = w / 2

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
