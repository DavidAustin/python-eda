# Python-EDA
# Copyright (C) 2025 Luke Cole
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

def make_fp(x_pins, y_pins, part_w, part_h, x_pads_offset, y_pads_offset, px, py, pad_w, pad_h, ground_pad_w, ground_pad_h):
    g = FootprintGen('TQFP-%dx%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (x_pins, y_pins, part_w, part_h, x_pads_offset, y_pads_offset, px, py, pad_w, pad_h))

    pad_from_cent_x = (x_pins - 1) / 2.0 * px
    pad_from_cent_y = -x_pads_offset / 2.0
    
    x = 0
    y = 0
    for i in range(1, x_pins + 1):
        g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
        x += px
        
    x = pad_from_cent_x + y_pads_offset / 2.0
    y = pad_from_cent_y + (y_pins - 1) / 2.0 * py
    for i in range(x_pins + 1, x_pins + y_pins + 1):
        g.rect_padat(x, y, pad_h, pad_w, '%d' % i)
        y -= py

    x = (x_pins - 1) * px
    y = -x_pads_offset
    for i in range(x_pins + y_pins + 1, x_pins * 2 + y_pins + 1):
        g.rect_padat(x, y, pad_w, pad_h, '%d' % i)
        x -= px

    x = pad_from_cent_x - y_pads_offset / 2.0
    y = pad_from_cent_y - (y_pins - 1) / 2.0 * py
    for i in range(x_pins * 2 + y_pins + 1, x_pins * 2 + y_pins * 2 + 1):
        g.rect_padat(x, y, pad_h, pad_w, '%d' % i)
        y += py

    if ground_pad_w != 0:
        g.rect_padat(pad_from_cent_x, pad_from_cent_y, ground_pad_w, ground_pad_h, '0')

    ox1 = pad_from_cent_x - part_w / 2.0
    oy1 = pad_from_cent_y + part_h / 2.0
    oo = 0.25
    ox2 = ox1 + part_w
    oy2 = oy1 - part_h
    ood = 0.3
    
    g.outline(ox1, oy1, ox1 + oo, oy1)
    g.outline(ox1, oy1, ox1, oy1 - oo)
    g.outline(ox2, oy1, ox2 - oo, oy1)
    g.outline(ox2, oy1, ox2, oy1 - oo)
    
    g.outline(ox1, oy2, ox1 + oo, oy2)
    g.outline(ox1, oy2, ox1, oy2 + oo)
    g.outline(ox2, oy2, ox2 - oo, oy2)
    g.outline(ox2, oy2, ox2, oy2 + oo)
    
    g.outline(ox1, oy1 + ood, ox1, oy1 + ood, 0.3)

    g.write()

# https://www.analog.com/media/en/technical-documentation/data-sheets/ADG726_732.pdf
make_fp(12, 12, 7, 7, 8.3, 8.3, 0.5, 0.5, 0.3, 1.3, 0, 0)
