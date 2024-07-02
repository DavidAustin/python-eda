# Python-EDA
# Copyright (C) 2024 Luke Cole
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

g = FootprintGen("SDER041H-2R2MS")

# https://www.cyntec.com/upfile/products/download/SDER041H-000%20(B3).pdf

part_w = 4.0
part_h = 4.0

pad_w = (4.1 - 1.8) / 2.0
pad_h = 3.6

p = 1.8 + pad_w

g.rect_padat(0.0, 0.0, pad_w, pad_h, "1")
g.rect_padat(p, 0.0, pad_w, pad_h, "2")

cx = p / 2.0
cy = 0

ox1 = cx - part_w / 2.0
oy1 = cy - part_h / 2.0
ox2 = ox1
oy2 = oy1 + part_h
g.outline(ox1, oy1, ox2, oy2)

ox1 = cx + part_w / 2.0
ox2 = ox1
g.outline(ox1, oy1, ox2, oy2)

ox1 = cx - part_w / 2.0
oy1 = cy - part_h / 2.0
ox2 = ox1 + part_w
oy2 = oy1
g.outline(ox1, oy1, ox2, oy2)

oy1 = cy + part_h / 2.0
oy2 = oy1
g.outline(ox1, oy1, ox2, oy2)

g.write()
