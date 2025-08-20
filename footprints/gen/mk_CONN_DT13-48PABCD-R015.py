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

# https://www.digikey.com/en/products/detail/te-connectivity-deutsch-ict-connectors/DT13-48PABCD-R015/6566691
# https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=DT13-XPX-R015&DocType=Customer+Drawing&DocLang=English

g = FootprintGen('CONN_DT13-48PABCD-R015')

n_pins = 6

px = 9.12
py = 4.45
cx = 45.72 - 19.56
ccx = 19.56 * 2

d_hole = 1.588 + 1
d_ann = d_hole * 1.5

# A set
x = 0
y = 0
g.pinat(x, y, d_hole, d_ann,  "A1", {'square' : 1})
y += py
for i in range(2,7):
    g.pinat(x, y, d_hole, d_ann,  "A%d" % i)
    y += py
y -= py
x -= px
for i in range(7,13):
    g.pinat(x, y, d_hole, d_ann,  "A%d" % i)
    y -= py

# B set
x = cx
y = 0
g.pinat(x, y, d_hole, d_ann,  "B1", {'square' : 1})
y += py
for i in range(2,7):
    g.pinat(x, y, d_hole, d_ann,  "B%d" % i)
    y += py
y -= py
x -= px
for i in range(7,13):
    g.pinat(x, y, d_hole, d_ann,  "B%d" % i)
    y -= py

# C set
x = cx + ccx
y = 0
g.pinat(x, y, d_hole, d_ann,  "C1", {'square' : 1})
y += py
for i in range(2,7):
    g.pinat(x, y, d_hole, d_ann,  "C%d" % i)
    y += py
y -= py
x -= px
for i in range(7,13):
    g.pinat(x, y, d_hole, d_ann,  "C%d" % i)
    y -= py

# D set
x = 2 * cx + ccx
y = 0
g.pinat(x, y, d_hole, d_ann,  "D1", {'square' : 1})
y += py
for i in range(2,7):
    g.pinat(x, y, d_hole, d_ann,  "D%d" % i)
    y += py
y -= py
x -= px
for i in range(7,13):
    g.pinat(x, y, d_hole, d_ann,  "D%d" % i)
    y -= py

cccx = 118.11
cc_hole = 3.18 + 1

y = py * 5 + 5.46 - 6.6

x = -px / 2 + cx + ccx / 2 - cccx / 2
g.holeat(x, y, cc_hole)
x = -px / 2 + cx + ccx / 2 + cccx / 2
g.holeat(x, y, cc_hole)

pcb_width = 127
pcb_length = 165.1

ox1 = -px / 2 + cx + ccx / 2 + pcb_width / 2
ox2 = -px / 2 + cx + ccx / 2 - pcb_width / 2
oy1 = oy2 = py * 5 + 5.46
w = 1
g.outline(ox1, oy1, ox2, oy1, w)


#ox1 = -3.54
#oy1 = -2.0
#ox2 = p * (n_pins - 1) + 3.54
#oy2 = oy1 + 12.0
    
#g.outlinerect(ox1, oy1, ox2, oy2, 0.1)
    
#oy3 = oy2 - 0.3
    
#g.outline(ox1, oy3, ox2, oy3, 0.1)
##oy4 = oy1 + 15
##outline(f, ox1, oy4, ox2, oy4, 0.1)

g.write()
