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

# HHXD500ARA150MF80G from
# https://www.chemi-con.co.jp/products/relatedfiles/capacitor/catalog/HXDRA-e.PDF

import math
from footprintgen import *

g = FootprintGen('HCM1A1105V2-100-R')

part_w = 10.8
part_h = 10.8

w = 3.55
h = 3.5
px = 5.4 + w
py = 0

g.rect_padat(0.0, 0.0, w, h, '1')
g.rect_padat(-px, 0.0, w, h, '2')

ox1 = (part_w - px) / 2.0
oy1 = -(part_h - py) / 2.0

ox2 = ox1 - part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()


