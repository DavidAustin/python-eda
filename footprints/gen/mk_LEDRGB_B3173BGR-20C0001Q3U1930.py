# Python-EDA
# Copyright (C) 2022 Luke Cole
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

# https://media.digikey.com/pdf/Data%20Sheets/Harvatek%20PDFs/B3173BGR-20C0001Q3U1930.pdf

g = FootprintGen('LEDRGB_B3173BGR-20C0001Q3U1930')

pad_w = 0.6
pad_h = 0.55

pad_large_w = pad_w
pad_large_h = 0.9

p = 0.9
p_large = 2.8

py = 0.6 - pad_h / 2.0

g.rect_padat(0, 0, pad_large_w, pad_large_h, '1')
g.rect_padat(p_large / 2.0 - p / 2.0, -py, pad_w, pad_h, '2')
g.rect_padat(p_large / 2.0 + p / 2.0, -py, pad_w, pad_h, '3')
g.rect_padat(p_large, 0, pad_large_w, pad_large_h, '4')

part_w = 3.2
part_h = 1.5

ox1 = -(part_w - p_large) / 2.0
oy1 = -0.25
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
