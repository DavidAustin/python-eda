# Python-EDA
# Copyright (C) 2025 Luke Cole
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

# https://content.u-blox.com/sites/default/files/NEO-M8-FW3_DataSheet_UBX-15031086.pdf

import math
from footprintgen import *

part_w = 12.2
part_h = 16.0
px = 1.1
py = 12.2 + 0.9 / 2.0
pad_w = 0.8
pad_h = 0.9

g = FootprintGen('NEO-M8N')

x = 0
for i in range(1, 8):
    g.rect_padat(x, 0, pad_w, pad_h, i)
    x += px

x = x - px + 3.0
for i in range(8, 13):
    g.rect_padat(x, 0, pad_w, pad_h, i)
    x += px

x -= px
for i in range(13, 18):
    g.rect_padat(x, -py, pad_w, pad_h, i)
    x -= px

x = x + px - 3.0
for i in range(18, 25):
    g.rect_padat(x, -py, pad_w, pad_h, i)
    x -= px
    
ox1 = -1.0
oy1 = -(part_w + py) / 2.0

ox2 = ox1 + part_h
oy2 = oy1 + part_w

g.outlinerect(ox1, oy1, ox2, oy2)

g.outlinecirc(ox1 - 0.3, oy2 + 0.3, 0.05, 0.2)

g.write()
