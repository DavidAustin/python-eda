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

# https://content.u-blox.com/sites/default/files/SARA-N3_DataSheet_UBX-18066692.pdf

from footprintgen import *

g = FootprintGen("SARA-R5")

A = 26.0
B = 16.0
C = 2.2
D = 2.0
E = 2.5
F = 1.05
G = 1.1
H = 0.8
I = 1.5
J = 0.3
K = 2.75
L = 2.75
M1 = 1.8
M2 = 3.6
N = 2.1
O = 1.1
P = 0.9
Q = 1.0
R = 0.5

part_w = A
part_h = B

pad_x = R
pad_y = R

x = D - P
y = -F + Q
g.rect_padat(x, y, pad_x, pad_y, "0")

p = G
pad_x = H
pad_y = I

x = 0
y = 0
for i in range(1, 22):
    g.rect_padat(x, y, pad_x, pad_y, "%d" % i)
    x += -p

x = D - part_w + F
y = -F + E
for i in range(22, 33):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p
    
x = -p * 20
y = B - 2.0 * F
for i in range(33, 54):
    g.rect_padat(x, y, pad_x, pad_y, "%d" % i)
    x += p

x = D - F
y = -F + part_h - E
for i in range(54, 65):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y -= p

p = N
pad_x = O
pad_y = O

x = D - K
y = -F + L
for i in range(65, 71):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p

x -= M1
y = -F + L
for i in range(71, 77):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p

p = part_h - 2.0 * L
x -= M1
y = -F + L
for i in range(77, 79):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p

x -= M2
y = -F + L
for i in range(79, 81):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p

x = D - part_w + K + M1 + M1 + M2
y = -F + L
for i in range(81, 83):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p

x -= M2
y = -F + L
for i in range(83, 85):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p

p = N
x -= M1
y = -F + L
for i in range(85, 91):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p

x -= M1
y = -F + L
for i in range(91, 97):
    g.rect_padat(x, y, pad_y, pad_x, "%d" % i)
    y += p
    
ox1 = D
oy1 = -F
ox2 = ox1 - part_w
oy2 = oy1 + part_h

g.outlinerect(ox1, oy1, ox2, oy2)

g.write()
