# Python-EDA
# Copyright (C) 2018 Luke Cole
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

def make_connector(n_pins, part_w, part_h):
    g = FootprintGen('SOIC-%d-N' % n_pins)

    px = 1.27
    py = 6.25
    
    pad_w = 0.8
    pad_h = 1.5
    
    x = 0
    for i in range(1, n_pins / 2 + 1):
        g.rect_padat(x, 0, pad_w, pad_h, i)
        x += px

    j = i
    x = px * (n_pins / 2 - 1)
    for i in range(1, n_pins / 2 + 1):
        g.rect_padat(x, py, pad_w, pad_h, j + i)
        x -= px

    ox1 = (part_h - px * (n_pins / 2 - 1)) / 2
    oy1 = (part_w - py) / 2

    ox2 = part_h - ox1
    oy2 = part_w - oy1

    g.outlinerect(-ox1, -oy1, ox2, oy2)

    g.outlinecirc(-ox1 + 0.3, -oy1 + 0.3, 0.05, 0.2)

    g.write()

make_connector(8, 3.9, 4.9) # based on https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit#Narrow_SOIC_(JEDEC)
make_connector(14, 3.9, 8.65) # based on https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit#Narrow_SOIC_(JEDEC)
make_connector(16, 4.4, 10.28) # based on http://optoelectronics.liteon.com/upload/download/DS70-2009-0014/LTV-2X7%20sereis%20Mar17.PDF
