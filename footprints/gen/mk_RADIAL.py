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

class footprintradial:

    def __init__(self, name):
        self.g = FootprintGen(name)
    
    def make_radial(self, d, p, d_hole, d_ann, origin_x = 0, origin_y = 0):
        self.g.pinat(origin_x, origin_y, d_hole, d_ann,  1, {'square' : 1})
        self.g.pinat(origin_x + p, origin_y, d_hole, d_ann,  2)
    
        self.g.outlinecirc(origin_x + p / 2.0, origin_y, d / 2.0)

        oo = 0.5

        ox = origin_x + p / 2.0 + (d / 2.0) * math.cos(math.radians(45)) + oo
        oy = origin_y + (d / 2.0) * math.sin(math.radians(45)) + oo
        
        ox1 = ox - oo
        oy1 = oy
        ox2 = ox + oo
        oy2 = oy
        self.g.outline(ox1, oy1, ox2, oy2)

        ox1 = ox
        oy1 = oy - oo
        ox2 = ox
        oy2 = oy + oo
        self.g.outline(ox1, oy1, ox2, oy2)

    def write(self):
        self.g.write()

clearance = 0.3

data = {
    '10000uF 50V UVR1H103MRD': [25, 12.5, 1.0 + clearance], # https://www.nichicon.co.jp/english/products/pdfs/e-uvr.pdf - I think this is the biggest before screw terminals are required
    '2000uF 50V EKYC500ELL202ML30S' : [16, 7.5, 0.8 + clearance], # http://www.chemi-con.co.jp/cgi-bin/CAT_DB/SEARCH/cat_db_al.cgi?e=e&j=p&pdfname=kyc
    '1000uF 50V UVR1H102MHD1TO' : [12.5, 5.0, 0.6 + clearance], # https://www.nichicon.co.jp/english/products/pdfs/e-uvr.pdf
    '470uF 50V ESH477M050AH4AA' : [10.0, 5.0, 0.6 + clearance], # https://www.nichicon.co.jp/english/products/pdfs/e-uvr.pdf
    '10uF 50V 860020672010' : [5.0, 2.0, 0.5 + clearance] # https://www.we-online.de/katalog/datasheet/860020672010.pdf
}

for v in data.values():
    d_ann = v[2] * 1.75
    r = footprintradial('RADIAL-%.2f-%.2f-%.2f-%.2f' % (v[0], v[1], v[2], d_ann))
    r.make_radial(v[0], v[1], v[2], d_ann)
    r.write()

r = footprintradial('RADIAL-multi')
origin_x = 0
origin_y = 0
origin_dia = data['10000uF 50V UVR1H103MRD'][0]
origin_pitch = data['10000uF 50V UVR1H103MRD'][1]
i = 0

data = sorted(data.items(), key=lambda x: x[1], reverse=True)

for v in data:
    d = v[1]
    d_ann = d[2] * 1.75
    if i > 0:
        origin_x = (origin_pitch - d[1]) / 2.0
        origin_y = (d[0] - origin_dia) / 2.0
        r.make_radial(d[0], d[1], d[2], d_ann)
    r.make_radial(d[0], d[1], d[2], d_ann, origin_x, origin_y)
    r.make_radial(d[0], d[1], d[2], d_ann, origin_x, -origin_y)
    i += 1
r.write()
