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

g = FootprintGen("SK-14D01-G-6")

#https://media.digikey.com/pdf/Data%20Sheets/C&K/SK-14D01-G.pdf

part_w = 14.6
part_h = 4.3

d_hole = 0.8
d_ann = d_hole * 1.75

p = 2

g.pinat(-2.1, 0.0, 1.25, 1.25 * 1.75, "0")
g.pinat(2 * 5 + 2.1, 0.0, 1.25, 1.25 * 1.75, "0")

x = 0
for i in range(1, 7):
    opts = {}
    if i == 1:
        opts['square'] = 1
    g.pinat(x, 0.0, d_hole, d_ann, i, opts)
    x += p

ox1 = -(part_w - p * 5 - 2.1 * 2) / 2.0 - 2.1
oy1 = -part_h / 2.0
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox2, oy1, ox2, oy2)
g.outline(ox2, oy2, ox1, oy2)
g.outline(ox1, oy2, ox1, oy1)

g.write()
