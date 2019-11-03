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

g = FootprintGen('B953AS-2R7N-P3')

w = 12.8
h = 12.8

pad_w = 2.6
pad_h = 3.6

g.rect_padat(-(13.1-pad_w)/2, 0, pad_w, pad_h, '1')
g.rect_padat((13.1-pad_w)/2, 0, pad_w, pad_h, '2')

ox1 = -w / 2
oy1 = -h / 2

ox2 = ox1 + w
oy2 = oy1 + h
g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
