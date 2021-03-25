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


from footprintgen import *

g = FootprintGen('WSON10_20x30_PAD')

wx = 2.0
wy = 3.0

pad_w = 0.5
pad_h = 0.25

thermal_pad_w = 0.84
thermal_pad_h = 2.4

p = 0.5


x = 0
y = 0

for i in range(1, 6):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    y += p

y -= p
x = 1.9
for i in range(6, 11):
    g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
    y -= p


cx = 1.9/2
cy = p * 2
g.rect_padat(cx, cy, thermal_pad_w, thermal_pad_h, '0')

ox1 = -(wx - cx * 2.0) / 2.0
oy1 = (wy + cy * 2.0) / 2.0
ox2 = ox1 + wx
oy2 = oy1 - wy

ood = 0.3

#g.outline(ox1, oy1, ox1, oy2)
g.outline(ox1, oy1, ox2, oy1)

g.outline(ox1, oy2, ox2, oy2)
#g.outline(ox2, oy1, ox2, oy2)

g.outline(ox1, oy2 - ood, ox1, oy2 - ood, 0.3)

g.write()
