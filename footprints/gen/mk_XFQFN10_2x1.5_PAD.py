# Python-EDA
# Copyright (C) 2020 Luke Cole
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

g = FootprintGen('XFQFN10_2x1.5_PAD')

part_w = 2.0
part_h = 1.5

p = 0.5

pad_w = 0.30
pad_h = 0.58

x = 0
y = 0
for i in range(1, 5):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    x += p

x = p * 3
y = 1.85 - pad_h
for i in range(6, 10):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    x -= p

pad_w = 0.35
pad_h = 0.63
    
x = p * 3.0 + (2.35 - 1.5) / 2.0 - pad_h / 2.0
y = (1.85 - pad_h) / 2.0
g.rect_padat(x, y, pad_h, pad_w, '5')
    
x = -((2.35 - 1.5) / 2.0 - pad_h / 2.0)
y = (1.85 - pad_h) / 2.0
g.rect_padat(x, y, pad_h, pad_w, '10')
    
ox1 = (part_w - p * 3) / 2.0
oy1 = (part_h - (1.85 - 0.58)) / 2.0

ox2 = part_w - ox1
oy2 = part_h - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outlinecirc(-ox1 - 0.3, -oy1 - 0.3, 0.05, 0.2)

g.write()
