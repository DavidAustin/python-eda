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

g = FootprintGen('ER-CON30HT-1')

# https://www.buydisplay.com/download/connector/ER-CON30HT-1.pdf

wx = 19.35
wy = 4.5

w = 0.3
h = 1.25

p = 0.5

pin_count = 24

# shouldn't have to edit below this line

x = 0.0
for i in range(1, pin_count + 1):
    g.rect_padat(x, 0.0, w, h, '%d' % i)
    x += p

big_pad_w = 2.0
big_pad_h = 3.0
    
g.rect_padat(big_pad_w / 2.0 - 2.54, -big_pad_h / 2.0 + h / 2.0 - 1.45, big_pad_w, big_pad_h, '0')
g.rect_padat((pin_count + 1) * p - big_pad_w + 2.54, -big_pad_h / 2.0 + h / 2.0 - 1.45, big_pad_w, big_pad_h, '0')
    
ox1 = ((pin_count - 1) * p - wx) / 2.0
oy1 = h / 2.0 - 1.45

ox2 = ox1 + wx
oy2 = oy1 - wy

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
