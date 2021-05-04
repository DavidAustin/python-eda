# Python-EDA
# Copyright (C) 2020 David Austin
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

def mk_a_track(x, y):
    g = FootprintGen("TRACK_%03dx%03d" % (x,y))

    g.FG_DEFAULTS['clearance'] = -float(y)/10
    g.rect_padat(0.0, 0.0, float(x) / 10, float(y)/10, "1", opts={})

    g.write()




for x in range(10,305,10):
    for y in range(10,105,5):
        mk_a_track(x,y)
