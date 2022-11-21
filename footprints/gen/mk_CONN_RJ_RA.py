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

def make_connector(size):
    if size == 11:
        n_pins = 6
    elif size == 45:
        n_pins = 8 
    elif size == 50:
        n_pins = 10

    g = FootprintGen('CONN%d_RJ%d_RA' % (n_pins, size))

    px = 1.27
    py = 2.54
    x = 0
    y = 0
    dia = 1.0
    od = dia * 2.0

    h = 18.5
    w = 7.07 + px * (n_pins + 1)
    
    g.pinat(x, y, dia, od,  1, {'square' : 1})
    x += px
    for i in range(2, int(n_pins) + 1):
      if i % 2 == 0:
        y = -py
      else:
        y = 0
      g.pinat(x, y, dia, od,  i)
      x += px

    x = -px
    y = 8.89 - 2.54
    dia = 3.2
    od = dia * 1.5
    g.pinat(x, y, dia, od,  "0")

    x = px * (n_pins + 1) - px
    y = 8.89 - 2.54
    dia = 3.2
    od = dia * 1.5
    g.pinat(x, y, dia, od,  "0")

    x = -px - 2.0
    y = 8.89 - 2.54 + 3.05
    dia = 1.3
    od = dia * 1.5
    g.pinat(x, y, dia, od,  "0")

    x = -px + px * (n_pins + 1) + 2.0
    y = 8.89 - 2.54 + 3.05
    dia = 1.3
    od = dia * 1.5
    g.pinat(x, y, dia, od,  "0")

    ox1 = -px - 2.0 - (w - px * (n_pins + 1) - 2.0 - 2.0) / 2.0
    oy1 = -2.54 - (h - 8.13 - 8.89)
    ox2 = ox1 + w
    oy2 = oy1 + h
    
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
    g.write()

make_connector(11)
make_connector(45)
make_connector(50)

