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

def make_fp(n_pins, part_w, part_h, px, py, pad_w, pad_h, thermal_pad_w = False, thermal_pad_h = False):
    if thermal_pad_w and thermal_pad_h:
        g = FootprintGen('WSON-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h, thermal_pad_w, thermal_pad_h))
    else:
        g = FootprintGen('WSON-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h))

    x = 0
    for i in range(1, n_pins // 2 + 1):
        g.rect_padat(x, 0, pad_w, pad_h, i)
        x += px

    j = i
    x = px * (n_pins / 2.0 - 1)
    for i in range(1, n_pins // 2 + 1):
        g.rect_padat(x, -py, pad_w, pad_h, j + i)
        x -= px

    cx = -(part_w - px * (n_pins / 2.0 - 1)) / 2.0 + part_w / 2.0
    cy = -py / 2.0
    
    if thermal_pad_w and thermal_pad_h:
        g.rect_padat(cx, cy, thermal_pad_w, thermal_pad_h, '0')
        
    ox1 = (part_h - px * (n_pins / 2.0 - 1)) / 2.0
    oy1 = (part_w + py) / 2.0

    ox2 = part_h - ox1
    oy2 = part_w - oy1

    g.outlinerect(-ox1, -oy1, ox2, oy2)

    g.outlinecirc(-ox1 - 0.3, oy1 - py + 0.3, 0.05, 0.2)

    g.write()

# https://www.ti.com/lit/ds/symlink/tps62063.pdf
make_fp(8, 2.0, 2.0, 0.5, 1.9, 0.25, 0.5, 1.6, 0.9)
