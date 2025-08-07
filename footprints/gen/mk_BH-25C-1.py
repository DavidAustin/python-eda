# Python-EDA
# Copyright (C) 2025 Luke Cole
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

g = FootprintGen('BH-25C-1')

# physical part dimensions (not including pins)
part_dia = 24.5

# pin dimensions
d = 2.0
a = d * 2.0

g.pinat(-7.9, 0.0, d, a, '1')
g.pinat(12.10, 0.0, d, a, '2')

g.outlinecirc(0.0, 0.0, part_dia / 2)

g.outlineplus(part_dia / 2 + 2, 4.5)

g.write()
