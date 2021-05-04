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

g = FootprintGen('TSOP362_UP')


wx = 7.5
wy = 5.3
px = 1.27
pw = 0.9
ph = 2.2
g.rect_padat(0.0, 0.0, pw, ph, '1')
g.rect_padat(px, 0.0, pw, ph, '2')
g.rect_padat(2*px, 0.0, pw, ph, '3')
g.rect_padat(3*px, 0.0, pw, ph, '4')

oo = 0.1
cx = 1.5 * px
cy = 1.5/2 - wy/2
g.outline(cx - wx/2 - oo, cy - wy/2 - oo, cx + wx/2 + oo, cy - wy/2 - oo)
g.outline(cx - wx/2 - oo, cy + wy/2 + oo, cx - wx/2 - oo, cy - wy/2 - oo)
g.outline(cx + wx/2 + oo, cy + wy/2 + oo, cx + wx/2 + oo, cy - wy/2 - oo)

xo = 0.2
g.outline(cx - xo, cy, cx + xo, cy)
g.outline(cx, cy - xo, cx, cy + xo)

g.outline(-1, 1.5, -1, 1.5, 0.3)

g.write()
