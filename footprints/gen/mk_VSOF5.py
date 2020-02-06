# Python-EDA
# Copyright (C) 2018-2020 Luke Cole (ported), David Austin (original author)
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

g = FootprintGen('VSOF5')

padw = 0.25
padh = 0.35
pitch = 0.5
pitchy = 1.35

cx = pitch
cy = -pitchy/2.0

g.rect_padat(0, 0, padw, padh, '1')
g.rect_padat(pitch, 0, padw, padh, '2')
g.rect_padat(2*pitch,0, padw, padh, '3')

g.rect_padat(2*pitch, -pitchy, padw, padh, '4')
g.rect_padat(0, -pitchy, padw, padh, '5')

ow = 1.6
oh = 1.2

ox1 = cx - ow/2.0
oy1 = cy + oh/2.0
ox2 = ox1 + ow
oy2 = oy1 - oh

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.write()
