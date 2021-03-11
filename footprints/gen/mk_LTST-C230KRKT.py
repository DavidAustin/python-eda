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

g = FootprintGen('LTST-C230KRKT')

part_w = 1.6
part_h = 3.2

w = 1.6 + 0.2
h = (part_h - 1.49) / 2.0 + 0.2

px = 0
py = h + 1.49

g.rect_padat(-px / 2.0, py / 2.0, w, h, '1')
g.rect_padat(px / 2.0, -py / 2.0, w, h, '2')

ox1 = -(part_w - px) / 2.0 - px / 2.0
ox2 = ox1 + part_w
oy1 = -(part_h - py) / 2.0 - py / 2.0
oy2 = oy1 + part_h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox1, oy2, ox2, oy2)

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

oo = 0.1

ox1 = part_w / 2.0 + 0.5 - oo
oy1 = -part_h / 2.0
ox2 = part_w / 2.0 + 0.5 + oo
oy2 = oy1
g.outline(ox1, oy1, ox2, oy2)

ox1 = part_w / 2.0 + 0.5
oy1 = -part_h / 2.0 + oo
ox2 = ox1
oy2 = -part_h / 2.0 - oo
g.outline(ox1, oy1, ox2, oy2)

g.write()
