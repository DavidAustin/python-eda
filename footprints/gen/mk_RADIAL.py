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

    oo = 0.5

    ox = p / 2.0 + (d / 2.0) * math.cos(math.radians(45)) + oo
    oy = (d / 2.0) * math.sin(math.radians(45)) + oo

    ox1 = ox - oo
    oy1 = oy
    ox2 = ox + oo
    oy2 = oy
    g.outline(ox1, oy1, ox2, oy2)

    ox1 = ox
    oy1 = oy - oo
    ox2 = ox
    oy2 = oy + oo
    g.outline(ox1, oy1, ox2, oy2)
    
    g.write()
    
clearance = 0.3

# 10000uF 50V UVR1H103MRD https://www.nichicon.co.jp/english/products/pdfs/e-uvr.pdf
# I think this is the biggest before screw terminals are required
d_hole = 1.0 + clearance
d_ann = d_hole * 1.75
make_radial(25, 12.5, d_hole, d_ann)

# 2000uF 50V EKYC500ELL202ML30S - http://www.chemi-con.co.jp/cgi-bin/CAT_DB/SEARCH/cat_db_al.cgi?e=e&j=p&pdfname=kyc
d_hole = 0.8 + clearance
d_ann = d_hole * 1.75
make_radial(16, 7.5, d_hole, d_ann)

# 1000uF 50V UVR1H102MHD1TO - https://www.nichicon.co.jp/english/products/pdfs/e-uvr.pdf
d_hole = 0.6 + clearance
d_ann = d_hole * 1.75
make_radial(12.5, 5.0, d_hole, d_ann)

# 470uF 50V ESH477M050AH4AA - https://www.nichicon.co.jp/english/products/pdfs/e-uvr.pdf
d_hole = 0.6 + clearance
d_ann = d_hole * 1.75
make_radial(10.0, 5.0, d_hole, d_ann)

# 10uF 50V 860020672010 - https://www.we-online.de/katalog/datasheet/860020672010.pdf
d_hole = 0.5 + clearance
d_ann = d_hole * 1.75
make_radial(5.0, 2.0, d_hole, d_ann)

