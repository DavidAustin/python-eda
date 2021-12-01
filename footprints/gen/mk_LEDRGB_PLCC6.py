# Python-EDA
# Copyright (C) 2021 Luke Cole
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

g = FootprintGen('LEDRGB_PLCC6')

pad_w = 0.8
pad_h = 0.4

p = 0.68
p_inside = 0.66 + pad_h
p_outside = 0.81
py = 0.8 / 2 + 0.6 / 2

g.rect_padat(0, 0, 0.66, pad_w, '1')
g.rect_padat(p_outside, py, pad_h, pad_w, '2')
g.rect_padat(p_outside + p, py, pad_h, pad_w, '3')
g.rect_padat(p_outside + p + p_inside, py, pad_h, pad_w, '4')
g.rect_padat(p_outside + p * 2 + p_inside, py, pad_h, pad_w, '5')
g.rect_padat(p_outside * 2 + p * 2 + p_inside, 0, 0.66, pad_w, '6')

part_w = 4.7
part_h = 1.5

ox1 = -(part_w - (p_outside * 2 + p * 2 + p_inside)) / 2.0
oy1 = -0.4
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
