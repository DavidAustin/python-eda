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

g = FootprintGen('TACT3.3x2.9mm')

# https://media.digikey.com/pdf/Data%20Sheets/Mitsumi%20Elect/SOU-242HNT_6994_ENG_%2317.pdf

part_w = 3.3
part_h = 2.9

w = (2.0 - 0.4) / 2.0
h = (3.9 - 2.9) / 2.0

px = 2.9 + h
py = 0.4 + w

g.rect_padat(-px / 2.0, -py / 2.0, h, w, '0')
g.rect_padat(-px / 2.0, py / 2.0, h, w, '1')

g.rect_padat(px / 2.0, py / 2.0, h, w, '2')
g.rect_padat(px / 2.0, -py / 2.0, h, w, '2')
g.rect_padat(0, -1.5, w, h, '2')

ox1 = -(part_w - px) / 2.0 - px / 2.0
ox2 = ox1 + part_w
oy1 = -(part_h - py) / 2.0 - py / 2.0
oy2 = oy1 + part_h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.write()

