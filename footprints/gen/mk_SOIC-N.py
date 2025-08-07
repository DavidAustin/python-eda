# Python-EDA
# Copyright (C) 2018-2025 Luke Cole
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
        g = FootprintGen('SOIC-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h, thermal_pad_w, thermal_pad_h))
    else:
        g = FootprintGen('SOIC-%d-%.2fx%.2f-%.2fx%.2f-%.2fx%.2f' % (n_pins, part_w, part_h, px, py, pad_w, pad_h))

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

    g.outlinecirc(-ox1 + 0.3, oy1 - py - 0.3, 0.05, 0.2)

    g.write()

make_fp(6, 4.4, 3.6, 1.27, 6.46, 0.64, 1.8) # based on https://docs.broadcom.com/doc/AV02-2150EN (SO-5)
    
make_fp(8, 3.9, 4.9, 1.27, 6.25, 0.8, 1.5) # based on https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit#Narrow_SOIC_(JEDEC)
make_fp(8, 3.9, 4.9, 1.27, 5.75, 0.45, 2.15, 3.1, 2.4) # based on https://www.ti.com/lit/ds/symlink/tps54328.pdf
make_fp(8, 3.9, 4.9, 1.27, 4.93, 0.53, 1.98) # based on https://www.analog.com/media/en/technical-documentation/data-sheets/DS3231M.pdf
                                             # and https://www.analog.com/media/en/technical-documentation/data-sheets/max33045e-max33046e.pdf
make_fp(8, 3.9, 4.9, 1.27, 5.4, 0.6, 1.55) # based on https://ww1.microchip.com/downloads/en/DeviceDoc/ATA6562.3-Data-Sheet-DS20005790D.pdf
make_fp(14, 3.9, 8.65, 1.27, 6.25, 0.8, 1.5) # based on https://en.wikipedia.org/wiki/Small_Outline_Integrated_Circuit#Narrow_SOIC_(JEDEC)
make_fp(14, 3.9, 8.65, 1.27, 5.4, 0.6, 1.55) # based on https://ww1.microchip.com/downloads/en/DeviceDoc/External-CAN-FD-Controller-with-SPI-Interface-DS20006027B.pdf
make_fp(16, 3.9, 9.9, 1.27, 5.4, 0.8, 1.5) # based on https://ww1.microchip.com/downloads/en/DeviceDoc/21295d.pdf
make_fp(16, 4.4, 10.28, 1.27, 6.25, 0.8, 1.5) # based on http://optoelectronics.liteon.com/upload/download/DS70-2009-0014/LTV-2X7%20sereis%20Mar17.PDF
make_fp(16, 7.5, 12.8, 1.27, 8.9, 0.8, 1.5) # based on https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM6020-6028.pdf
make_fp(28, 5.3, 10.2, 0.65, 7.2, 0.45, 1.75) # based on http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf
