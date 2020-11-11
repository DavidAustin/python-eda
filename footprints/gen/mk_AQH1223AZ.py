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

# https://www.digikey.com/en/products/detail/panasonic-electric-works/AQH1223AZ/8549294

n_pins = 8

part_w = 6.4
part_h = 9.78

px = 2.54
py = 8.3

pad_w = 1.5
pad_h = 1.9
    
g = FootprintGen('AQH1223AZ')

x = 0
for i in range(1, n_pins // 2 + 1):
    g.rect_padat(x, 0, pad_w, pad_h, i)
    x += px

j = i
x = px * (n_pins / 2.0 - 1)
for i in range(1, n_pins // 2 + 1):
    if j + i != 7:
        g.rect_padat(x, -py, pad_w, pad_h, j + i)
    x -= px

ox1 = (part_h - px * (n_pins / 2.0 - 1)) / 2.0
oy1 = (part_w + py) / 2.0

ox2 = part_h - ox1
oy2 = part_w - oy1

g.outlinerect(-ox1, -oy1, ox2, oy2)

g.outlinecirc(-ox1 + 0.3, oy1 - py - 0.3, 0.05, 0.2)

g.write()
