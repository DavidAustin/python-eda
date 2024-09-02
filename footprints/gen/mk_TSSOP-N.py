# Python-EDA
# Copyright (C) 2020-2022 Luke Cole
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

def make_fp(n_pins, part_w, part_h, px, py, pad_w, pad_h):
    g = FootprintGen('TSSOP-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h))

    x = 0
    for i in range(1, n_pins // 2 + 1):
        g.rect_padat(x, 0, pad_w, pad_h, i)
        x += px

    j = i
    x = px * (n_pins / 2.0 - 1)
    for i in range(1, n_pins // 2 + 1):
        g.rect_padat(x, -py, pad_w, pad_h, j + i)
        x -= px

    ox1 = (part_w - px * (n_pins / 2.0 - 1)) / 2
    oy1 = (part_h + py) / 2.0

    ox2 = part_w - ox1
    oy2 = part_h - oy1

    g.outlinerect(-ox1, -oy1, ox2, oy2)

    g.outlinecirc(-ox1 + 0.3, oy1 - py - 0.3, 0.05, 0.2)

    g.write()

# https://en.wikipedia.org/wiki/Small_outline_integrated_circuit#Thin-shrink_small-outline_package_(TSSOP)

# http://ww1.microchip.com/downloads/en/DeviceDoc/22147a.pdf
make_fp(6, 2, 1.25, 0.65, 2.2, 0.4, 0.9)

# https://www.ti.com/lit/ds/symlink/lm4889.pdf
make_fp(8, 3.0, 3.0, 0.65, 4.4, 0.45, 1.5)

# https://www.ti.com/lit/ds/symlink/msp430fr2111.pdf
# https://www.ti.com/lit/ds/symlink/msp430fr2000.pdf
make_fp(16, 5.0, 4.4, 0.65, 5.8, 0.45, 1.5)

# https://toshiba.semicon-storage.com/info/74VHCT245AFT_datasheet_en_20170222.pdf?did=13949&prodName=74VHCT245AFT
# https://www.ti.com/lit/ds/symlink/txs0108e.pdf?ts=1725240466504
make_fp(20, 6.5, 4.4, 0.65, 5.8, 0.45, 1.5)

# https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf
make_fp(28, 9.7, 4.4, 0.65, 5.4, 0.45, 1.5)

# http://www.ti.com/lit/ds/symlink/msp430fr2355.pdf
make_fp(38, 9.7, 4.4, 0.5, 5.6, 0.25, 1.55)

# NOTE: 18/3/24 corrected part_w and part_h to align with x, y

# TODO: make_fp() up to 64-pin
