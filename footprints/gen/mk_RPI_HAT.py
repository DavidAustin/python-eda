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

fn = 'RPI_HAT'

g = FootprintGen('%s' % fn)

g.pinat(3.5, -3.5, 3.0, 6.0, '0')
g.pinat(3.5 + 58.0, -3.5, 3.0, 6.0, '0')
g.pinat(3.5, -3.5 - 49, 3.0, 6.0, '0')
g.pinat(3.5 + 58.0, -3.5 - 49, 3.0, 6.0, '0')
       
ow = 85.0
oh = 56.0

g.outlinerect(0, 0, ow, -oh)

conx = 3.5 + 29
cony = -3.5 - 49
pitch = 2.54

x = conx - pitch * 9.5
for i in range(1,41,2):

    # LC addition
    if i == 1:
        opts = {'square' : 1 }
    else:
        opts = None
        
    g.pinat(x, cony + pitch / 2, 1.0, 1.8, str(i), opts)
    g.pinat(x, cony - pitch / 2, 1.0, 1.8, str(i + 1))
    x += pitch

# LC addition
rows = 2
cols = 20
oo = 1.23
ox1 = - oo
oy1 = - oo
ox2 = pitch * (cols - 1) + oo
oy2 = pitch * (rows - 1) + oo
x = conx - pitch * 9.5
y = cony - pitch / 2

g.outlinerect(x + ox1, y + oy1, x + ox2, y + oy2)
    
g.write()
