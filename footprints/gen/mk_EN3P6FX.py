# Python-EDA
# Copyright (C) 2021 Luke Cole
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

import math
from footprintgen import *

g = FootprintGen('EN3P6FX')

d_hole = 1 # TODO
d_ann = 2 # TODO
p = 4 # TODO
d = 15.5

opts = {}
opts['square'] = 1
        
g.pinat(p * -1, p, d_hole, d_ann, '1', opts)
g.pinat(p * -1, 0, d_hole, d_ann, '2')
g.pinat(0, 0, d_hole, d_ann, '3')
g.pinat(p * 1, 0, d_hole, d_ann, '4')
g.pinat(p * 1, p, d_hole, d_ann, '5')
g.pinat(p * 1, -p, d_hole, d_ann, '6')

g.outlinecirc(0, 0, d / 2.0)

g.write()
