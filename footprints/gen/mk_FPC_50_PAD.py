# Python-EDA
# Copyright (C) 2018 David Austin
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

# https://www.buydisplay.com/download/connector/ER-CON24HT-1.pdf

import math
from footprintgen import *

def make(n_pins, top):

    if top:
        name = 'FPC%d_TOP_50_PAD' % n_pins
    else:
        name = 'FPC%d_BOT_50_PAD' % n_pins
        
    g = FootprintGen(name)

    x = 0.0
    y = 0.0
    px = 0.5
    w = 0.3
    h = 1.25
    if top:
        l = range(n_pins,0,-1)
    else:
        l = range(1, n_pins+1, 1)
        
    for i in l:
        g.rect_padat(x, y, w, h, str(i))
        x += px


    y = 1.45 - 1.25/2 + 3.0/2
    g.rect_padat(-2.54+2.0/2, y, 2.0, 3.0, '0')
    g.rect_padat(2.54-2.0/2 + (n_pins-1) * px, y, 2.0, 3.0, '0')

    oo = 0.07
    oy2 = 0 - h/2 + 1.0 + 4.5 + 1.5

    g.outline(0.0, oy2, px*(n_pins-1), oy2, 0.1)
    g.write()
    
    

for i in range(6, 51):
    for t in [True, False]:
        make(i, t)


