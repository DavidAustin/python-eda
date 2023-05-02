# Python-EDA
# Copyright (C) 2023 Luke Cole
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

# https://www.digikey.com/en/products/detail/jst-sales-america-inc/BM02B-ACHSS-GAN-TF-LF-SN/1647788

def make_it(n_pins):
    g = FootprintGen('CONN%d_120_SMD' % n_pins)
    
    p = 1.2
    x = p * (n_pins - 1)
    y = 0
    w = 0.6
    h = 0.85
    g.rect_padat(x, y, w, h, 1)
    x -= p
    for i in range(2, n_pins+1):
        g.rect_padat(x, y, w, h, i)
        x -= p

    p = 1.2 * (n_pins - 1)
    y = -3.75 - 0.85/2.0 + 0.8/2.0
    w = 0.7
    h = 0.8
    g.rect_padat(-0.8-0.7/2.0, y, w, h, 0)
    g.rect_padat(p + 0.8+0.7/2.0, y, w, h, 0)
    
    pw = p + 0.8 * 2.0 + 0.7 * 2.0
    py = 3.75 + 0.85 / 2.0
    
    ox1 = -0.8 - 0.7
    oy1 = -py
    ox2 = ox1 + pw
    oy2 = oy1 + py
    g.outlinerect(ox1, oy1, ox2, oy2, 0.1)

    g.write()

for i in range(2,4):
    make_it(i)


