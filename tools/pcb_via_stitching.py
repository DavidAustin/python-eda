# Python-EDA
# Copyright (C) 2018 Luke Cole
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

import sys
import os
import re
from ast import literal_eval
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

if len(sys.argv) < 12:
  print ("Usage: %s spacing x_offset y_offset board_width board_height "
         "top.poly bottom.poly "
         "top_exclude1.poly top_exclude2.poly "
         "bottom_exclude1.poly bottom_exclude2.poly"
         "\n\n"
         "NOTES:\n"
         "* Currently requires you to manually copy the gEDA PCB poly's into\n"
         "  seperate files\n"
         "* Currently coded to assume two holes in top and bottom layer\n"
         "  (i.e. (top|bottom)_exclude(1|2).poly) - hack code as needed for now,\n"
         "  make generic at some stage"
         % (sys.argv[0]))
  exit()

spacing = float(sys.argv[1]) # typically 2mm
x_offset = float(sys.argv[2]) # typically aimed for equal spacing between vertical board edges
y_offset = float(sys.argv[3]) # typically aimed for equal spacing between horizontal board edges
board_width = float(sys.argv[4])
board_height = float(sys.argv[5])

filename_top = sys.argv[6]
filename_bottom = sys.argv[7]

# fix me - make generic number of exclude (i.e. poly hole)

filename_top_exclude = sys.argv[8]
filename_top_exclude2 = sys.argv[9]

filename_bottom_exclude = sys.argv[10]
filename_bottom_exclude2 = sys.argv[11]

if not os.path.exists(filename_top):
  print ("%s - File does not exist") % (filename_top)
  exit()

if not os.path.exists(filename_top_exclude):
  print ("%s - File does not exist") % (filename_top_exclude)
  exit()

if not os.path.exists(filename_top_exclude2):
  print ("%s - File does not exist") % (filename_top_exclude2)
  exit()
  
if not os.path.exists(filename_bottom):
  print ("%s - File does not exist") % (filename_bottom)
  exit()

if not os.path.exists(filename_bottom_exclude):
  print ("%s - File does not exist") % (filename_bottom_exclude)
  exit()

if not os.path.exists(filename_bottom_exclude2):
  print ("%s - File does not exist") % (filename_bottom_exclude2)
  exit()

infile = open(filename_top, "r")
lines_top = infile.read()
infile.close()

infile = open(filename_top_exclude, "r")
lines_top_exclude = infile.read()
infile.close()

infile = open(filename_top_exclude2, "r")
lines_top_exclude2 = infile.read()
infile.close()

infile = open(filename_bottom, "r")
lines_bottom = infile.read()
infile.close()

infile = open(filename_bottom_exclude, "r")
lines_bottom_exclude = infile.read()
infile.close()


infile = open(filename_bottom_exclude2, "r")
lines_bottom_exclude2 = infile.read()
infile.close()

# replace mil's with mm's
def fix_mil(matchobj):
    value = float(matchobj.group(0).replace("mil", ""))
    return str(round(value / 39.37, 4)) + "mm"
lines_top = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines_top)
lines_top_exclude = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines_top_exclude)
lines_top_exclude2 = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines_top_exclude2)
lines_bottom = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines_bottom)
lines_bottom_exclude = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines_bottom_exclude)
lines_bottom_exclude2 = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines_bottom_exclude2)

# convert pcb to tuples of tuple pairs

lines_top = lines_top.replace("mm ", ", ")
lines_top = lines_top.replace("mm", "")
lines_top = lines_top.replace("\n", "")
lines_top = lines_top.replace("\t", "")
lines_top = lines_top.replace("] [", "), (")
lines_top = lines_top.replace("]", ")]")
lines_top = lines_top.replace("[", "[(")
lines_top = literal_eval(lines_top)

lines_top_exclude = lines_top_exclude.replace("mm ", ", ")
lines_top_exclude = lines_top_exclude.replace("mm", "")
lines_top_exclude = lines_top_exclude.replace("\n", "")
lines_top_exclude = lines_top_exclude.replace("\t", "")
lines_top_exclude = lines_top_exclude.replace("] [", "), (")
lines_top_exclude = lines_top_exclude.replace("]", ")]")
lines_top_exclude = lines_top_exclude.replace("[", "[(")
lines_top_exclude = literal_eval(lines_top_exclude)

lines_top_exclude2 = lines_top_exclude2.replace("mm ", ", ")
lines_top_exclude2 = lines_top_exclude2.replace("mm", "")
lines_top_exclude2 = lines_top_exclude2.replace("\n", "")
lines_top_exclude2 = lines_top_exclude2.replace("\t", "")
lines_top_exclude2 = lines_top_exclude2.replace("] [", "), (")
lines_top_exclude2 = lines_top_exclude2.replace("]", ")]")
lines_top_exclude2 = lines_top_exclude2.replace("[", "[(")
lines_top_exclude2 = literal_eval(lines_top_exclude2)

lines_bottom = lines_bottom.replace("mm ", ", ")
lines_bottom = lines_bottom.replace("mm", "")
lines_bottom = lines_bottom.replace("\n", "")
lines_bottom = lines_bottom.replace("\t", "")
lines_bottom = lines_bottom.replace("] [", "), (")
lines_bottom = lines_bottom.replace("]", ")]")
lines_bottom = lines_bottom.replace("[", "[(")
lines_bottom = literal_eval(lines_bottom)

lines_bottom_exclude = lines_bottom_exclude.replace("mm ", ", ")
lines_bottom_exclude = lines_bottom_exclude.replace("mm", "")
lines_bottom_exclude = lines_bottom_exclude.replace("\n", "")
lines_bottom_exclude = lines_bottom_exclude.replace("\t", "")
lines_bottom_exclude = lines_bottom_exclude.replace("] [", "), (")
lines_bottom_exclude = lines_bottom_exclude.replace("]", ")]")
lines_bottom_exclude = lines_bottom_exclude.replace("[", "[(")
lines_bottom_exclude = literal_eval(lines_bottom_exclude)

lines_bottom_exclude2 = lines_bottom_exclude2.replace("mm ", ", ")
lines_bottom_exclude2 = lines_bottom_exclude2.replace("mm", "")
lines_bottom_exclude2 = lines_bottom_exclude2.replace("\n", "")
lines_bottom_exclude2 = lines_bottom_exclude2.replace("\t", "")
lines_bottom_exclude2 = lines_bottom_exclude2.replace("] [", "), (")
lines_bottom_exclude2 = lines_bottom_exclude2.replace("]", ")]")
lines_bottom_exclude2 = lines_bottom_exclude2.replace("[", "[(")
lines_bottom_exclude2 = literal_eval(lines_bottom_exclude2)

polygon_top = Polygon(lines_top)
polygon_top_exclude = Polygon(lines_top_exclude)
polygon_top_exclude2 = Polygon(lines_top_exclude2)
polygon_bottom = Polygon(lines_bottom)
polygon_bottom_exclude = Polygon(lines_bottom_exclude)
polygon_bottom_exclude2 = Polygon(lines_bottom_exclude2)

x = 0.0
y = 0.0

for x in range(int((board_width + x_offset * 2) / spacing)):
  x *= spacing
  x += x_offset
  for y in range(int((board_height + y_offset * 2) / spacing)):
    y *= spacing
    y += y_offset
    
    tp = Point(x, y)

    make_via = True
    if not polygon_top.contains(tp):
      make_via = False
    if not polygon_bottom.contains(tp):
      make_via = False
    if polygon_top_exclude.contains(tp):
      make_via = False
    if polygon_top_exclude2.contains(tp):
      make_via = False
    if polygon_bottom_exclude.contains(tp):
      make_via = False
    if polygon_bottom_exclude2.contains(tp):
      make_via = False

    # x y thickness clearance mask drillholedia name number flags
    if make_via:
      print ('Via[%fmm %fmm 0.7000mm 20.00mil 0.0000 0.3000mm "" "thermal(0S,5S)"]' % (x, y))

#print (int((board_width + x_offset * 2) / spacing))
#print (int((board_height + y_offset * 2) / spacing))

