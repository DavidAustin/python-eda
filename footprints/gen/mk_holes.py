# Python-EDA
# Copyright (C) 2018 Luke Cole & David Austin
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
import numpy as np

# added by Luke
# https://trfastenings.com/products/knowledgebase/tables-standards-terminology/Tapping-Sizes-and-Clearance-Holes
holes = {1: 1.2,
         1.2: 1.4,
         1.4: 1.6,
         1.6: 1.8,
         1.8: 2,
         2: 2.4,
         2.2: 2.4,
         2.5: 2.9,
         3: 3.4,
         3.5: 3.9,
         4: 4.5,
         5: 5.5,
         6: 6.6,
         8: 9,
         10: 11,
         12: 13.5,
         14: 15.5,
         16: 17.5,
         18: 20,
         20: 22,
         22: 24,
         24: 26,
         27: 30,
         30: 33}

for key, value in holes.items():

    if int(key) == key:
        g = FootprintGen('M%d' % int(key))
    else:
        g = FootprintGen('M%d_%d' % (int(key), int(key * 10) % 10))
    g.pinat(0, 0, value, value * 2, '0')
    g.write()
