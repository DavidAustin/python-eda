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

g = FootprintGen("CDRH2D18LD")

# http://products.sumida.com/products/pdf/CDRH2D18LD.pdf

part_w = 3.0
part_h = 3.0

pad_w = 1.3
pad_h = 1.3

p = 1.7 + 1.3

g.rect_padat(0.0, 0.0, pad_w, pad_h, "1")
g.rect_padat(p, 0.0, pad_w, pad_h, "2")

ox1 = -pad_w / 2.0
oy1 = 0
ox2 = ox1 + part_w * math.cos(math.radians(45))
oy2 = part_w * math.sin(math.radians(45))
g.outline(ox1, oy1, ox2, oy2)
g.outline(ox1, oy1, ox2, -oy2)

ox1 = p + pad_w / 2.0
oy1 = 0
ox2 = ox1 - part_w * math.cos(math.radians(45))
oy2 = part_w * math.sin(math.radians(45))
g.outline(ox1, oy1, ox2, oy2)
g.outline(ox1, oy1, ox2, -oy2)

g.write()
