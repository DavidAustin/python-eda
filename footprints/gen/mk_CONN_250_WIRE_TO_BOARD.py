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

# https://media.digikey.com/pdf/Data%20Sheets/Phoenix%20Contact%20PDFs/COMBICON%20Spring-Cage%20PCB%20Term.%20Blocks.pdf

import math
from footprintgen import *

def make_connector(n_pins):
    g = FootprintGen('CONN%d_250_WIRE_TO_BOARD' % n_pins)
    
    p = 2.5
    x = 0
    y = 0
    dia = 1.0
    od = dia * 1.75
    g.pinat(0, y, dia, od,  1, {'square' : 1})
    x += p
    for i in range(2, n_pins + 1):
        g.pinat(x, y, dia, od,  i)
        x += p
    
    p_len = (n_pins - 1) * p
    C = p_len + (58.4 - 48.26)
    oy = p / 2.0
    ox = p / 2.0
    
    ox1 = -2.5 / 2.0
    oy1 = -(12 - 7.3)
    ox2 = p_len + ox
    oy2 = 7.3
    
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
    g.write()

for i in range(1,41):
    make_connector(i)
