# Python-EDA
# Copyright (C) 2018 Luke Cole (ported), David Austin (original author)
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

for dia in range(11):
    if dia > 0:
        if int(dia) == dia:
            g = FootprintGen('M%d' % int(dia))
        else:
            g = FootprintGen('M%d_%d' % (int(dia), int(dia * 10) % 10))

        g.pinat(0, 0, dia, dia * 2, '1')
    
        g.write()
