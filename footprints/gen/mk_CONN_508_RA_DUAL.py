# Python-EDA
# Copyright (C) 2022 Luke Cole
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

# designed for cost-effective Wurth Elektronik connectors, might work for Weidmuller, but not reviewed
# e.g.
# https://www.we-online.com/katalog/datasheet/6913195100xx.pdf

def make_connector(n_pins):
    g = FootprintGen('CONN%d_508_RA_DUAL' % n_pins)
    
    p = 5.08
    x = p * (n_pins-1)
    y = 0
    od = 3.0
    
    g.pinat(x, y, 1.4, od,  1, {'square' : 1})
    x -= p
    for i in range(2,n_pins+1):
        g.pinat(x, y, 1.4, od,  i)
        x -= p
    x = p * (n_pins-1) + 2.54
    y += 10.16
    for i in range(n_pins, n_pins*2):
        g.pinat(x, y, 1.4, od, i + 1)
        x -= p
        
    ox1 = -3.5
    oy1 = -2.0
    ox2 = ox1 + 3.5 + p * (n_pins - 1) + 6.1
    oy2 = oy1 + 22.0
    
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
    oy3 = oy2 - 0.5
    
    g.outline(ox1, oy3, ox2, oy3, 0.1)
    #oy4 = oy1 + 15
    #outline(f, ox1, oy4, ox2, oy4, 0.1)

    g.write()

for i in range(2,21):
    make_connector(i)


