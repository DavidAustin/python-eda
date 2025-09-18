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

import math

from footprintgen import *

g = FootprintGen("DLW21SZ900HQ2L")

# https://www.murata.com/en-us/products/productdata/8796760113182/QFLC9115.pdf

part_w = 2.0
part_h = 1.2

pad_w = 0.9
pad_h = 0.35

px = 1.7
py = 0.85

g.rect_padat(0.0, -py / 2, pad_w, pad_h, "1")
g.rect_padat(px, -py / 2, pad_w, pad_h, "2")

g.rect_padat(0.0, py / 2, pad_w, pad_h, "4")
g.rect_padat(px, py / 2, pad_w, pad_h, "3")

cx = px / 2.0
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

g.outlinecirc(0, -part_h / 2 - 0.3, 0.05, 0.2)

g.write()
