# Python-EDA
# Copyright (C) 2019 Luke Cole
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

w = 3
h = 3

g_pad_w = 1.06
g_pad_h = 2.2

s_pad_w = 1
s_pad_h = 1

g = FootprintGen('UFL-R-SMT-1-10')
# U.FL-R-SMT-1(10)
# https://www.digikey.com.au/product-detail/en/hirose-electric-co-ltd/U.FL-R-SMT-1-10/H11891CT-ND/2504612

g.rect_padat(0, 0, g_pad_w, g_pad_h, '1')
g.rect_padat(2.95, 0, g_pad_w, g_pad_h, '2')
g.rect_padat(1.475, 1.5, s_pad_w, s_pad_h, '3')

ox1 = -0.025
oy1 = -1.5

ox2 = ox1 + 3
oy2 = oy1 + 3

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
