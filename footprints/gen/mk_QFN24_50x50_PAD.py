# Python-EDA
# Copyright (C) 2019 David Austin
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

g = FootprintGen('QFN24_50x50_PAD')


wx = 5.0
wy = 5.0

padw = 0.3
padh = 0.4 + 0.4
pitch = 0.65
pad_from_cent = 5.0/2
x = 0
y = 0
for i in range(1, 7):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    x += pitch

x = pitch * 2.5 + pad_from_cent
y = -pad_from_cent + pitch * 2.5
for i in range(7, 13):
    g.rect_padat(x, y, padh, padw, '%d' % i)
    y -= pitch

x = pitch * 2.5 + pitch * 2.5
y = - 2 * pad_from_cent
for i in range(13, 19):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    x -= pitch

x = pitch * 2.5 - pad_from_cent
y = -pad_from_cent - pitch * 2.5

for i in range(19, 25):
    g.rect_padat(x, y, padh, padw, '%d' % i)
    y += pitch


g.rect_padat(2.5 * pitch, -pad_from_cent, 3.2, 3.2, '0')

ox1 = 2.5 * pitch - wx/2.0
oy1 = -pad_from_cent + wy/2.0
oo = 0.25
ox2 = ox1 + wx
oy2 = oy1 - wy
ood = 0.3

g.outline(ox1, oy1, ox1 + oo, oy1)
g.outline(ox1, oy1, ox1, oy1 - oo)
g.outline(ox2, oy1, ox2 - oo, oy1)
g.outline(ox2, oy1, ox2, oy1 - oo)

g.outline(ox1, oy2, ox1 + oo, oy2)
g.outline(ox1, oy2, ox1, oy2 + oo)
g.outline(ox2, oy2, ox2 - oo, oy2)
g.outline(ox2, oy2, ox2, oy2 + oo)

g.outline(ox1, oy1 + ood, ox1, oy1 + ood, 0.3)

g.write()
