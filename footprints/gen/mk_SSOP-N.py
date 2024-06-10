# Python-EDA
# Copyright (C) 2024 Luke Cole
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
    g = FootprintGen('SSOP-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h))

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

# https://en.wikipedia.org/wiki/Small_outline_integrated_circuit
# https://www.holtek.com/webapi/106680/Footprints_for_SOP_SSOP_Series_20230710.pdf/b3eb1361-295e-4f22-b705-8f1008399503

make_fp(28, 9.7, 5.3, 0.635, 5.4, 0.35, 1.5)
#make_fp(28, 9.7, 5.3, 0.635, 7.3, 0.35, 1.5)

# NOTE: 18/3/24 corrected part_w and part_h to align with x, y

# TODO: make_fp() up to 64-pin
