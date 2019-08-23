# Python-EDA
# Copyright (C) 2019 Luke Cole
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

g = FootprintGen('PNP8S2D2Y03QE')

d_hole = 2.2
d_ann = 3.5

opts = {}
opts['square'] = 1
        
g.pinat(7.5 / 2.0, 0, d_hole, d_ann, '1', opts)
g.pinat(-7.5 / 2.0, 0, d_hole, d_ann, '2')

g.outlinecirc(0, 0, 17.5 / 2.0)

g.write()
