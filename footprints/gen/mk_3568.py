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

g = FootprintGen('3568')

wx = 16.0
wy = 6.73

px = 9.91
py = 3.4

d_hole = 1.6
d_ann = d_hole * 2.0

x = 0
y = 0

g.pinat(x, y, d_hole, d_ann, 1)
y -= py
g.pinat(x, y, d_hole, d_ann, 1)

y = 0
x = px
g.pinat(x, y, d_hole, d_ann, 2)
y -= py
g.pinat(x, y, d_hole, d_ann, 2)

ox1 = -(wx - px) / 2.0
oy1 = (wy - py) / 2.0

ox2 = ox1 + wx
oy2 = oy1 - wy

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
