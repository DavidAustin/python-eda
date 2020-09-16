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

g = FootprintGen('LQFP64')

# https://ti.com/lit/ds/symlink/msp430fr4131.pdf

wx = 10.2
wy = 10.2

pad_w = 0.3
pad_h = 1.5

p = 0.5

pad_from_cent_x = 11.4 / 2.0
pad_from_cent_y = 15.0 * p / 2.0

x = 0
y = 0

corner_offset = 11.4 / 2.0 - 15.0 * p / 2.0

for i in range(1, 17):
    g.rect_padat(x, y, pad_h, pad_w, '%d' % i)
    y += p

y -= p
for i in range(33, 49):
    g.rect_padat(11.4, y, pad_h, pad_w, '%d' % i)
    y -= p

x = corner_offset
for i in range(17, 33):
    g.rect_padat(x, 15.0 * p + corner_offset, pad_w, pad_h, '%d' % i)
    x += p

x = corner_offset + 15.0 * p
for i in range(49, 65):
    g.rect_padat(x, -corner_offset, pad_w, pad_h, '%d' % i)
    x -= p
    
ox1 = pad_from_cent_x - wx / 2.0
oy1 = pad_from_cent_y - wy / 2.0
ox2 = ox1 + wx
oy2 = oy1 + wy

ood = 0.3

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox1, oy1, ox2, oy1)

g.outline(ox1, oy2, ox2, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.outline(ox1 - ood, oy1 - ood, ox1 - ood, oy1 - ood, 0.3)

g.write()
