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

g = FootprintGen('QFP48_70x70_narrow')


wx = 7.0
wy = 7.0

padw = 0.29
padh = 1.5
pitch = 0.5
pad_from_cent = 8.4 / 2
n_per_side = 12
x = 0
y = 0
for i in range(1, 13):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    x += pitch

x = pitch * float(n_per_side-1)/2 + pad_from_cent
y = -pad_from_cent + pitch * float(n_per_side-1)/2
for i in range(13, 25):
    g.rect_padat(x, y, padh, padw, '%d' % i)
    y -= pitch

x = pitch * float(n_per_side-1)/2 + pitch * float(n_per_side-1)/2
y = - 2 * pad_from_cent
for i in range(25, 37):
    g.rect_padat(x, y, padw, padh, '%d' % i)
    x -= pitch

x = pitch * float(n_per_side-1)/2 - pad_from_cent
y = -pad_from_cent - pitch * float(n_per_side-1)/2

for i in range(37, 49):
    g.rect_padat(x, y, padh, padw, '%d' % i)
    y += pitch



ox1 = float(n_per_side-1)/2 * pitch - wx/2.0
oy1 = 0.0#-pad_from_cent + wy/2.0
ood = 0.3


g.outline(ox1, oy1 + ood, ox1, oy1 + ood, 0.4)

g.write()
