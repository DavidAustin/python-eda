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

# http://www.assmann-wsw.com/uploads/datasheets/ASS_4888_CO.pdf

import math
from footprintgen import *

def make_connector(n_pins, sex = "M"):
    g = FootprintGen('CONN%d_uDB_%s_RA' % (n_pins, sex))

    if n_pins == 9:
        A = 19.93
        B = 14.35 # also equals D and F
        C = 5.08
    elif n_pins == 15:
        A = 19.93
        B = 18.16 # also equals D and F
        C = 8.88
    elif n_pins == 25:
        A = 30.1
        B = 24.51 # also equals D and F
        C = 24.51
    
    px = 1.27
    py = 2.54
    x = 0
    y = 0
    dia = 0.71
    od = dia * 1.7

    if sex == "M":
        g.pinat(x, y, dia, od,  1, {'square' : 1})
        x += px
        for i in range(2, int(n_pins / 2.0) + 2):
            g.pinat(x, y, dia, od,  i)
            x += px

        x = 0.5 * px
        y = py
        for i in range(int(n_pins / 2.0) + 2, n_pins + 1):
            g.pinat(x, y, dia, od,  i)
            x += px
    else:
        x = px * int(n_pins / 2.0)
        g.pinat(x, y, dia, od,  1, {'square' : 1})
        x -= px
        for i in range(2, int(n_pins / 2.0) + 2):
            g.pinat(x, y, dia, od,  i)
            x -= px

        x = px * int(n_pins / 2.0) - 0.5 * px
        y = py
        for i in range(int(n_pins / 2.0) + 2, n_pins + 1):
            g.pinat(x, y, dia, od,  i)
            x -= px
            
    p = (B - C) / 2.0
        
    x = -p
    y = py / 2.0
    dia = 2.79
    od = dia * 1.7
    g.pinat(x, y, dia, od,  "0")

    x += B
    y = py / 2.0
    dia = 2.79
    od = dia * 1.7
    g.pinat(x, y, dia, od,  "0")
    
    ox1 = -(A - C) / 2.0
    oy1 = -2.0
    ox2 = ox1 + A
    oy2 = -oy1 + py + 1.27
    
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
    g.write()

make_connector(9, "M")
make_connector(15, "M")
make_connector(25, "M")

make_connector(9, "F")
make_connector(15, "F")
make_connector(25, "F")
