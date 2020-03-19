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

g = FootprintGen("EEE-HC1C101XP")

#https://industrial.panasonic.com/cdbs/www-data/pdf/RDE0000/ABA0000C1160.pdf - D8 size

part_w = 6.6
part_h = 6.6

pad_w = 3.2
pad_h = 3.6

p = 4.8

g.rect_padat(0.0, 0.0, pad_w, pad_h, "1") # +ve
g.rect_padat(p, 0.0, pad_w, pad_h, "2")

ox1 = -(part_w - p) / 2.0
oy1 = -part_h / 2.0
ox2 = ox1 + part_w
oy2 = oy1 + part_h

g.outline(ox1, oy1, ox2, oy1)
g.outline(ox2, oy1, ox2, oy2)
g.outline(ox2, oy2, ox1, oy2)
g.outline(ox1, oy2, ox1, oy1)

# polarity sign
g.outline(ox1 - 0.2, oy1 + 0.8, ox1 - 0.6, oy1 + 0.8)
g.outline(ox1 - 0.4, oy1 + 0.6, ox1 - 0.4, oy1 + 1.0)

g.write()
