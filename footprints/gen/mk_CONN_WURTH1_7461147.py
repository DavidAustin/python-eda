# Python-EDA
# Copyright (C) 2020 David Austin
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

g = FootprintGen("CONN_WURTH1_7461147")


d = 3.0
dh = 1.45
p = 2.54
for i in [-1.5, -0.5, 0.5, 1.5]:
    for j in [-1.5, -0.5, 0.5, 1.5]:
        g.pinat(i * p, j * p, dh, d, '1')
g.rect_padat(0,   0, 12.0, 12.0, '1')

g.write()
