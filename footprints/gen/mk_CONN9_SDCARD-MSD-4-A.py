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

# https://www.sameskydevices.com/product/resource/msd-4-a.pdf

import math
from footprintgen import *

g = FootprintGen('CONN9_SDCARD-MSD-4-A')

part_w = 14.75
part_h = 14.5

pad_x = 0.7
pad_y = 1.6

p = 1.1
x = 0
y = 0

g.rect_padat(x, y, pad_x, pad_y, "1")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "2")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "3")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "4")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "5")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "6")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "7")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "8")
x -= p
g.rect_padat(x, y, pad_x, pad_y, "9")

pad_x = 1.2
pad_y = 1.8

x = x - 0.6 - pad_x / 2
y = 1.6 / 2 + 10.2 - 8.8 - 1.8 / 2
g.rect_padat(x, y, pad_x, pad_y, "0")

y = 1.6 / 2 + 10.2 + 0.7 - 2.2 / 2
g.rect_padat(x, y, pad_x, pad_y, "0")

x = x + 14.3 + 1.2
g.rect_padat(x, y, pad_x, pad_y, "0")

center_x = -8 * 1.1 + 6.55

pad_x = 1.6
pad_y = 1.5
x = center_x - 4.95 + 8 + 3 + 1.6 / 2
y = 1.6 / 2 + 10.2 - 9.2 - 1.5
g.rect_padat(x, y, pad_x, pad_y, "0")

dia = 1.0
x = center_x - 4.95
y = 1.6 / 2 + 10.2
g.holeat(x, y, dia)

x += 8
y = 1.6 / 2 + 10.2
g.holeat(x, y, dia)

ox1 = center_x - part_w / 2
oy1 = -1.6 / 2
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

g.write()
