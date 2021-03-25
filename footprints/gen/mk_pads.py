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

from footprintgen import *

def mk_a_pad(x, y):
    g = FootprintGen("pad%03dx%03d" % (x,y))


    g.rect_padat(0.0, 0.0, float(x) / 10, float(y)/10, "1")

    g.write()




for x in range(5,155,5):
    for y in range(5,105,5):
        mk_a_pad(x,y)
