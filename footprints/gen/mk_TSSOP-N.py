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

def make_connector(n_pins, part_w, part_h, px, py, pad_w, pad_h):
    g = FootprintGen('TSSOP-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h))

    x = 0
    for i in range(1, n_pins / 2 + 1):
        g.rect_padat(x, 0, pad_w, pad_h, i)
        x += px

    j = i
    x = px * (n_pins / 2 - 1)
    for i in range(1, n_pins / 2 + 1):
        g.rect_padat(x, -py, pad_w, pad_h, j + i)
        x -= px

    ox1 = (part_h - px * (n_pins / 2 - 1)) / 2
    oy1 = (part_w + py) / 2

    ox2 = part_h - ox1
    oy2 = part_w - oy1

    g.outlinerect(-ox1, -oy1, ox2, oy2)

    g.outlinecirc(-ox1 + 0.3, oy1 - py - 0.3, 0.05, 0.2)

    g.write()

# https://en.wikipedia.org/wiki/Small_outline_integrated_circuit#Thin-shrink_small-outline_package_(TSSOP)

# https://pdfserv.maximintegrated.com/land_patterns/90-0092.PDF
# https://pdfserv.maximintegrated.com/package_dwgs/21-0036.PDF
make_connector(8, 3, 3, 0.65, 4.3, 0.4, 1.35)

# http://www.ti.com/lit/ds/symlink/msp430fr2355.pdf
make_connector(38, 4.4, 9.7, 0.5, 5.6, 0.25, 1.55)

# TODO: make_connector() up to 64-pin
