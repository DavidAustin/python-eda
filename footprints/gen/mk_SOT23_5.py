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

g = FootprintGen('SOT23_SC74_5')

# http://ww1.microchip.com/downloads/en/DeviceDoc/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf

part_w = 2.9
part_h = 1.6

px = 0.95
w = 0.6
h = 1.1
py = 2.8

x = 0.0
y = 0.0
for i in range(1,4):
    g.rect_padat(x, y, w, h, '%d' % i)
    x += px

x = 2 * px
y = -py

i = 4
g.rect_padat(x, y, w, h, '%d' % i)
i += 1
x -= px * 2
g.rect_padat(x, y, w, h, '%d' % i)

ox1 = px - part_w / 2.0
oy1 = -part_h / 2.0
ox2 = ox1 + part_w
oy2 = -py + part_h / 2.0

g.outlinerect(ox1, oy1, ox2, oy2)

g.outlinecirc(ox1 + 0.3, oy1 - 0.3, 0.05, 0.2)

g.write()
