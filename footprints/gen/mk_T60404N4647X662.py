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

from footprintgen import *
import math

g = FootprintGen('T60404N4647X662')

clearance = 0.3

wx = 22.2
wy = 14.0

p = 1.905
d_hole = math.sqrt(0.46**2 + 0.46**2) + clearance
d_ann = d_hole * 1.75

large_p = 2.54
large_d_hole = 1 + clearance
large_d_ann = large_d_hole * 1.75

x = 0
y = 0

g.pinat(x, y, large_d_hole, large_d_ann, 1)
x += large_p
g.pinat(x, y, large_d_hole, large_d_ann, 2)
x += large_p
g.pinat(x, y, large_d_hole, large_d_ann, 3)

y = -12.7
x = 0
g.pinat(x, y, large_d_hole, large_d_ann, 6)
x += large_p
g.pinat(x, y, large_d_hole, large_d_ann, 5)
x += large_p
g.pinat(x, y, large_d_hole, large_d_ann, 4)

y += (12.7 - 5.72) / 2.0
x = -7.62
g.pinat(x, y, d_hole, d_ann, 7)
y += p
g.pinat(x, y, d_hole, d_ann, 8)
y += p
g.pinat(x, y, d_hole, d_ann, 9)
y += p
g.pinat(x, y, d_hole, d_ann, 10)

ox1 = large_p - 12.0
oy1 = (wy - 12.7) / 2.0

ox2 = ox1 + wx
oy2 = oy1 - wy

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
