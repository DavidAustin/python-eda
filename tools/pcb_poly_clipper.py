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
import pyclipper
from ast import literal_eval

if len(sys.argv) < 3:
  print ("Usage: %s file.poly clip"
         "\n\n"
         "NOTES:\n"
         "* Currently requires you to manually copy the gEDA PCB poly's into\n"
         "  seperate file (file.poly)\n"
         "* clip is in mm - +ve will expand poly, and -ve will reduce poly\n"
         "KNOWN ISSUES:\n"
         "* space required between [x y] pts\m"
         "* any 0.0 value must have dimension (e.g. 0.0mm)\m"
         % (sys.argv[0]))
  exit()

filename = sys.argv[1]
clip = float(sys.argv[2])

if not os.path.exists(filename):
  print ("%s - File does not exist") % (filename)
  exit()

infile = open(filename, "r")
lines = infile.read()
infile.close()

# replace mil's with mm's
def fix_mil(matchobj):
    value = float(matchobj.group(0).replace("mil", ""))
    return str(round(value / 39.37, 4)) + "mm"
lines = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines)

# convert pcb to tuples of tuple pairs
lines = lines.replace("mm ", ", ")
lines = lines.replace("mm", "")
lines = lines.replace("\n", "")
lines = lines.replace("\t", "")
lines = lines.replace("] [", "), (")
lines = lines.replace("]", "))")
lines = lines.replace("[", "((")
subj = literal_eval(lines)

# multiply tuple elements by 10000
tuples = ()
for value in subj:
    new = (int(value[0] * 10000), int(value[1] * 10000))
    tuples = tuples + (new,)
subj = tuples

pco = pyclipper.PyclipperOffset()
pco.AddPath(subj, pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)

solution = pco.Execute(clip * 10000)

# divide list elements by 10000
output = ""
i = 0
for i in range(len(solution[0])):
    new = "[%fmm %fmm] " % (float(round(solution[0][i][0] / 10000.0, 4)),
                            float(round(solution[0][i][1] / 10000.0, 4)))
    output += new
print (output)
