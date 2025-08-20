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


import math
from footprintgen import *

g = FootprintGen("TO247_GCE") # TO-247AD, TO-3P (vendor), MO-247

px = 5.44
d = 3.0
dh = 1.5
g.pinat(0,    0, dh, d, 'G', {'square' : 1})
g.pinat(px,   0, dh, d, 'C')
g.pinat(px*2, 0, dh, d, 'E')

g.write()
