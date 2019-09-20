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

from footprintgen import *

g = FootprintGen("PLCC2")

part_w = 2.7
part_h = 2

pad_x = 1
pad_y = 2

p = 2.25

g.rect_padat(0.0, 0.0, pad_x, pad_y, "1")
g.rect_padat(p, 0.0, pad_x, pad_y, "2")

ox1 = -(part_w - p) / 2.0
oy1 = -pad_y / 2.0
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

ox3 = ox2 - 0.8
oy3 = oy1

ox4 = ox2 - 0.8
oy4 = oy2

g.outline(ox3, oy3, ox4, oy4)

g.write()
