# Python-EDA
# Copyright (C) 2019 David Austin
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


def make_it(n_pins):
    g = FootprintGen('CONN_JST_ZH%d_15_RA' % n_pins)

    
    px = 1.5
    w = 0.7 
    h = 7-4.3

    x = 0#p * (n_pins-1)
    y = 0
    x = 0
    y = 4.3 + h/2
    for i in range(1,n_pins+1):
        g.rect_padat(x, y, w, h, str(i))
        x -= px

    y = 4.3-1.4-1.9/2
    g.rect_padat(1.4+1.1/2, y, 1.1, 1.9, '0')
    g.rect_padat(-(n_pins-1)*px-1.4-1.1/2, y, 1.1, 1.9, '0')

    g.outline(1.4, 0.0, -1.4-(n_pins-1)*px, 0.0, 0.5)


    g.write()

for i in range(2,11):
    make_it(i)


