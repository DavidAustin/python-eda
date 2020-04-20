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

g = FootprintGen('WSON8_5x6_PAD')

# https://www.cypress.com/file/316171/download

wx = 5.0
wy = 6.0

pad_w = 0.4 + 0.2
pad_h = 0.6 + 0.2

thermal_pad_w = 4.0
thermal_pad_h = 3.4

p = 1.27

pad_from_cent_x = p * 1.5
pad_from_cent_y = -wy / 2.0

x = 0
y = 0

for i in range(1, 5):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    x += p

x -= p
for i in range(5, 9):
    g.rect_padat(x, -wy, pad_w, pad_h, '%d' % i)
    x -= p

g.rect_padat(pad_from_cent_x, pad_from_cent_y, thermal_pad_w, thermal_pad_h, '0')

ox1 = -(wx - pad_from_cent_x * 2.0) / 2.0
oy1 = (wy + pad_from_cent_y * 2.0) / 2.0
ox2 = ox1 + wx
oy2 = oy1 - wy

ood = 0.3

g.outline(ox1, oy1, ox1, oy2)
g.outline(ox1, oy1, ox2, oy1)

g.outline(ox1, oy2, ox2, oy2)
g.outline(ox2, oy1, ox2, oy2)

g.outline(ox1, oy1 + ood, ox1, oy1 + ood, 0.3)

g.write()
