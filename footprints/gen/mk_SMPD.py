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

from footprintgen import *

g = FootprintGen("SMPD")


g.rect_padat(0.0, 0.0, 10.66, 8.38, "1")
g.rect_padat(-2.67, -8.38/2+14.33-3.05/2, 2.03, 3.05, "2")
g.rect_padat(2.67, -8.38/2+14.33-3.05/2, 2.03, 3.05, "2")


g.write()
