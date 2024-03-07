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

def make_fp(n_pins, part_w, part_h, px, py, pad_w, pad_h, thermal_pad_w = False, thermal_pad_h = False):
    if thermal_pad_w and thermal_pad_h:
        g = FootprintGen('MSOP-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h, thermal_pad_w, thermal_pad_h))
    else:
        g = FootprintGen('MSOP-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h))

    x = 0
    for i in range(1, n_pins // 2 + 1):
        g.rect_padat(x, 0, pad_w, pad_h, i)
        x += px

    j = i
    x = px * (n_pins / 2.0 - 1)
    for i in range(1, n_pins // 2 + 1):
        g.rect_padat(x, -py, pad_w, pad_h, j + i)
        x -= px

    cx = px * (n_pins / 2.0 - 1) / 2.0
    cy = -py / 2.0

    if thermal_pad_w and thermal_pad_h:
        g.rect_padat(cx, cy, thermal_pad_w, thermal_pad_h, '0')
        
    ox1 = (part_h - px * (n_pins / 2.0 - 1)) / 2.0
    oy1 = (part_w + py) / 2.0

    ox2 = part_h - ox1
    oy2 = part_w - oy1

    g.outlinerect(-ox1, -oy1, ox2, oy2)

    g.outlinecirc(-ox1 + 0.3, oy1 - py - 0.3, 0.05, 0.2)

    g.write()

# based on https://www.ti.com/lit/ds/symlink/lm5085.pdf
make_fp(8, 3.0, 3.0, 0.65, 4.4, 0.45, 1.4, 3.0 * 0.65, 3.0 * 0.65) 
    
# based on https://www.analog.com/media/en/technical-documentation/data-sheets/max3311e-max3313e.pdf
make_fp(10, 3.0, 3.0, 0.5, 3.0 + 1.0, 0.3, 1.4) 
