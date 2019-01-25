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

g = FootprintGen('DFN10_38x31_PAD')


wx = 3.8
wy = 3.1

padw = 0.65
padh = 0.3
pitch = 0.6
pad_from_cent = 3.05/2
x = 0
y = 0
for i in range(1, 6):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    y += pitch

x = 2*pad_from_cent
y = + 4 * pitch
for i in range(6, 11):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    y -= pitch



g.rect_padat(pad_from_cent, 2 *pitch, 0.7, 2.9, '0')

ox1 = pad_from_cent - wx/2.0
oy1 = 2 * pitch + wy/2.0
oo = 0.25
ox2 = ox1 + wx
oy2 = oy1 - wy
ood = -0.3

g.outline(ox1, oy1, ox2, oy1)

g.outline(ox1, oy2, ox2, oy2)
          
g.outline(ox1, oy2 + ood, ox1, oy2 + ood, 0.3)

g.write()
