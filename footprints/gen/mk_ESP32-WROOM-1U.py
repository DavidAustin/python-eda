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


import math
from footprintgen import *

def make_fp():
    name = 'ESP32-WROOM-1U'
    g = FootprintGen(name)

    # === Module dimensions ===
    mod_w = 18.0  # mm
    mod_h = 19.2  # mm (no PCB antenna)

    # === Pad params ===
    pad_w = 1.5   # mm (width)
    pad_h = 0.9   # mm (height)
    pitch = 1.27   # mm

    # === Pad rows ===
    # Left (pins 1–14, top to bottom)
    x_lhs = -17.5 / 2
    y_lhs_start = mod_h / 2 - pitch * 13 - 1.5
    for i in range(14):
        y = y_lhs_start + i * pitch
        g.rect_padat(x_lhs, y, pad_w, pad_h, i + 1)

    # Bottom (pins 15–26, left to right)
    y_bot = mod_h / 2 - pad_w / 2 + 0.5
    x_bot_start = -mod_w / 2 + 2.015
    for i in range(27-15):
        x = x_bot_start + i * pitch
        g.rect_padat(x, y_bot, pad_h, pad_w, 15 + i)

    # Right (pins 27–40, bottom to top)
    x_rhs = 17.5 / 2
    y_rhs_start = mod_h / 2 - 1.5
    for i in range(41-27):
        y = y_rhs_start - i * pitch
        g.rect_padat(x_rhs, y, pad_w, pad_h, 27 + i)

    # === Outline ===
    g.outlinerect(-mod_w / 2, -mod_h / 2, mod_w / 2, mod_h / 2)

    # === Pin 1 marker ===
    g.outlinecirc(x_lhs - 1.0, y_lhs_start, 0.05, 0.25)

    # === Thermal pads ===
    cx = -mod_w / 2 + 7.5
    cy = mod_h / 2 - 10.29
    thermal_pad_w = thermal_pad_h = 0.9

    g.rect_padat(cx - 3.7 / 2 + thermal_pad_w / 2, cy - 3.7 / 2 + thermal_pad_h / 2, thermal_pad_w, thermal_pad_h, '0')
    g.rect_padat(cx, cy - 3.7 / 2 + thermal_pad_h / 2, thermal_pad_w, thermal_pad_h, '0')
    g.rect_padat(cx + 3.7 / 2 - thermal_pad_w / 2, cy - 3.7 / 2 + thermal_pad_h / 2, thermal_pad_w, thermal_pad_h, '0')

    g.rect_padat(cx - 3.7 / 2 + thermal_pad_w / 2, cy, thermal_pad_w, thermal_pad_h, '0')
    g.rect_padat(cx, cy, thermal_pad_w, thermal_pad_h, '0')
    g.rect_padat(cx + 3.7 / 2 - thermal_pad_w / 2, cy, thermal_pad_w, thermal_pad_h, '0')

    g.rect_padat(cx - 3.7 / 2 + thermal_pad_w / 2, cy + 3.7 / 2 - thermal_pad_h / 2, thermal_pad_w, thermal_pad_h, '0')
    g.rect_padat(cx, cy + 3.7 / 2 - thermal_pad_h / 2, thermal_pad_w, thermal_pad_h, '0')
    g.rect_padat(cx + 3.7 / 2 - thermal_pad_w / 2, cy + 3.7 / 2 - thermal_pad_h / 2, thermal_pad_w, thermal_pad_h, '0')
    
    g.write()

make_fp()
