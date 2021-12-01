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

g = FootprintGen('VQFN64_PAD')

manual_soldering_ext = 0.1

wx = 9.0
wy = 9.0

tpadw = 4.25
tpadh = 4.25

padw = 0.24
padh = 0.6
pitch = 0.5

x = 0
y = 0
for i in range(1, 17):
    g.padat(x, y, padh, padw, '%d' % i, {'dir' : (0,-1)} )
    y += pitch

x = (8.8 - 15 * pitch) / 2.0
y = 15 * pitch + (8.8 - 15 * pitch) / 2.0
for i in range(17, 33):
    g.padat(x, y, padw, padh, '%d' % i, {'dir' : (0,-1)} )
    x += pitch

x = 8.8
y = 15 * pitch
for i in range(33, 49):
    g.padat(x, y, padh, padw, '%d' % i, {'dir' : (0,-1)} )
    y -= pitch

x = 15 * pitch + (8.8 - 15 * pitch) / 2.0
y = -(8.8 - 15 * pitch) / 2.0
for i in range(49, 65):
    g.padat(x, y, padw, padh, '%d' % i, {'dir' : (0,-1)} )
    x -= pitch

x = 7.5 * pitch + (8.8 - 15 * pitch) / 2.0
y = 7.5 * pitch
g.rect_padat(x, y, tpadw, tpadh, '0')

(8.8 - 15 * pitch)

ox1 = -(wx - 8.8) / 2.0
oy1 = -(wy - 15 * pitch) / 2.0
oo = 0.25
ox2 = ox1 + wx
oy2 = oy1 + wy

g.outlinerect(ox1, oy1, ox2, oy2, oo)

g.outline(ox1 - oo, oy1 - oo, ox1 - oo, oy1 - oo, 0.3)

g.write()
