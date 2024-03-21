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


from footprintgen import *

def make_fp(x_pins, y_pins, part_w, part_h, px, py, pad_w, pad_h):
    g = FootprintGen('BGA-%dx%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (x_pins, y_pins, part_w, part_h, px, py, pad_w, pad_h))

    x = 0
    y = 0
    for j in range(0, y_pins):
        for i in range(0, x_pins):
            x = i * px
            y = j * py
            g.rect_padat(x, y, pad_w, pad_h, '%d' % i)

    oo = 0.25
            
    ox1 = -(part_w - (x_pins - 1) * px) / 2.0
    oy1 = -(part_h - (y_pins - 1) * py) / 2.0
    ox2 = ox1 + part_w
    oy2 = oy1 + part_h

    # top left
    g.outline(ox1, oy1, ox1 + oo, oy1)
    g.outline(ox1, oy1, ox1, oy1 + oo)

    # top right
    g.outline(ox2, oy1, ox2 - oo, oy1)
    g.outline(ox2, oy1, ox2, oy1 + oo)

    # bottom left
    g.outline(ox1, oy2, ox1 + oo, oy2)
    g.outline(ox1, oy2, ox1, oy2 - oo)

    # bottom right
    g.outline(ox2, oy2, ox2 - oo, oy2)
    g.outline(ox2, oy2, ox2, oy2 - oo)

    ood = 0.3
    
    g.outline(ox1 - ood, oy1 - ood, ox1 - ood, oy1 - ood, 0.3)

    g.write()

# TODO:
# replace the following scripts with this generic tool:
# mk_QFN16_40x40_PAD.py, mk_QFN20_50x50_PAD.py, mk_QFN32_PAD.py
# mk_VQFN16_PAD.py, mk_VQFN20_PAD.py, mk_VQFN24_PAD.py
# mk_WQFN16_3x3_PAD.py

# https://www.analog.com/media/en/technical-documentation/data-sheets/8064fa.pdf
make_fp(9, 12, 11.9, 16.0, 1.27, 1.27, 0.63, 0.63)
