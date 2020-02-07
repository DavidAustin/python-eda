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

import sys
import csv
import pprint

if len(sys.argv) < 2:
  print ("Usage: %s bom.csv" % (sys.argv[0]))
  print ("")
  print ("NOTE: first use gschem_bom.py then pass through this tool to group refdes and provide qty")
  exit()

file = sys.argv[1]

pp = pprint.PrettyPrinter(indent=4)

details = {}
refdes = {}
qtys = {}

with open(file, newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='\'')
  for row in reader:
    if len(row) > 4:
      #print (row[1:])
      device = row[3]
      if device in refdes: 
        refdes[device] += "," + row[0]
        qtys[device] += 1
      else:
        refdes[device] = row[0]
        details[device] = row[1:]
        qtys[device] = 1

#pp.pprint(details)
#pp.pprint(qtys)
#pp.pprint(refdes)

for i in qtys:
  if i == "device":
    print (("\"%s\",qty,%s") % (refdes[i], ','. join(details[i])))
  else:
    print (("\"%s\",%s,%s") % (refdes[i], qtys[i], ','. join(details[i])))
