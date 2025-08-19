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

g = FootprintGen("peSOD923")

g.rect_padat(0.0, 0.0, 0.36, 0.25, "1")
g.rect_padat(1.2-0.36, 0.0, 0.36, 0.25, "2")

oo = 0.05
ox1 = (1.2 - 0.36) / 2 - 0.8/2
oy1 = 0.0 - 0.6 / 2
ox2 = ox1 + 0.8
oy2 = oy1 + 0.6

g.outline(ox1 - oo, oy1 - oo, ox2 + oo, oy1 - oo)
g.outline(ox1 - oo, oy2 + oo, ox2 + oo, oy2 + oo)

g.outline(ox1 - oo, oy1 - oo, ox1 - oo, oy1 + 2 * oo)
g.outline(ox1 - oo, oy2 + oo, ox1 - oo, oy2 - 2 * oo)


g.write()
