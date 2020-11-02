# Python-EDA
# Copyright (C) 2020 Luke Cole
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

def make_radial(d, p, d_hole, d_ann):
    g = FootprintGen('RADIAL-%.2f-%.2f-%.2f-%.2f' % (d, p, d_hole, d_ann))
    
    g.pinat(0, 0, d_hole, d_ann,  1, {'square' : 1})
    g.pinat(p, 0, d_hole, d_ann,  2)
    
    g.outlinecirc(p / 2.0, 0, d / 2.0)
    
    g.write()

# 500C602T040AB2B - https://www.cde.com/resources/catalogs/500C.pdf
d_hole = 8 + 1 # i.e. 9mm for M8
d_ann = d_hole + 2
make_radial(34.93, 12.7, d_hole, d_ann)
