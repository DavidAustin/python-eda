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

g = FootprintGen('MIC_376x295')


wx = 3.76
wy = 2.95
g.round_pad_at(-2.1, -0.965, 0.723, '4')
g.round_pad_at(-2.1, 0.0, 0.612, '5')
g.round_pad_at(-2.1, 0.965, 0.723, '1')
g.arc_pad_at(0.0, 0.0, 0.96/2, 1.56/2, 0, 360, '6')
g.round_pad_at(-2.1 + 2.74, -1.015, 0.562, '3')
g.round_pad_at(-2.1 + 2.74, 1.015, 0.562, '2')
g.holeat(0.0, 0.0, 0.75)

oo = 0.1
g.outlinerect(1.13-3.76-oo, 1.475+oo, 1.13+oo, 1.475-2.95-oo)

g.outline(1.13-3.76, 1.475+0.4,
          1.13-3.76, 1.475+0.4,
          0.3)

g.write()
