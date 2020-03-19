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

g = FootprintGen("HTP-CON-M417")

# https://www.hyte.pro/upload/hytepro-product/file/drawing/pdf/hytepro-magnetic-connector/HTP-CON-M417.pdf

n_pins = 4

part_w = 15
part_h = 6.66

d_hole = 0.9
d_ann = d_hole * 2.0
p = 2.2

d_hole_support = 1.15
d_ann_support = 0
p_support = 1.7

g.pinat(-p_support, 0.0, d_hole_support, d_ann_support, "0")
g.pinat(p * (n_pins - 1) + p_support, 0.0, d_hole_support, d_ann_support, "0")

x = 0
for i in range(1, n_pins + 1):
    opts = {}
    if i == 1:
        opts['square'] = 1
    g.pinat(x, 0.0, d_hole, d_ann, i, opts)
    x += p

ox1 = -(part_w - p * (n_pins - 1) - p_support * 2) / 2.0 - p_support
oy1 = -part_h / 2.0
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox2, oy1, ox2, oy2)
g.outline(ox2, oy2, ox1, oy2)
g.outline(ox1, oy2, ox1, oy1)

g.write()
