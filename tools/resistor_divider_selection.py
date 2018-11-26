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

if len(sys.argv) < 2:
  print ("Usage: %s vref vout_target [inverted]\n"
         "\n"
         "non-inverted (default) circuit schematic:\n"
         "\n"
         " Vref\n"
         "  | \n"
         "  \ \n"
         "  / R1\n"
         "  \ \n"
         "  | \n"
         "  |---- Vout\n"
         "  | \n"
         "  \ \n"
         "  / R2\n"
         "  \ \n"
         "  | \n"
         " GND\n"
         "\n"
         "inverted circuit schematic (e.g. power isolators):\n"
         "\n"
         " Viso\n"
         "  | \n"
         "  \ \n"
         "  / R2\n"
         "  \ \n"
         "  | \n"
         "  |---- Vsel\n"
         "  | \n"
         "  \ \n"
         "  / R1\n"
         "  \ \n"
         "  | \n"
         " GNDiso\n"
         "\n"
         "Suggested use (for now):\n"
         "1) python %s > v.txt\n"
         "2) sort -n -k 9,9 v.txt\n"
         "3) look for vout_target" % (sys.argv[0], sys.argv[0]))
  exit()

vref = float(sys.argv[1])
vout_target = float(sys.argv[2])
inverted = False
if len(sys.argv) == 4:
    inverted = True

# https://en.wikipedia.org/wiki/E_series_of_preferred_numbers
E96 = [ 1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24,
        1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62,
        1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10,
        2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74,
        2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57,
        3.65, 3.74, 3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64,
        4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.90, 6.04,
        6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87,
        8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76 ]

resistor_multipliers = [1, 10, 100, 1000, 10000, 100000, 1000000 ]

for m in resistor_multipliers:
    for r in E96:
        R1 = r * m
        R1 = round(R1 / m, 1)
        R1 = R1 * m
        for mm in resistor_multipliers:
            for rr in E96:
                R2 = rr * mm
                R2 = round(R2 / mm, 1)
                R2 = R2 * mm
                if inverted:
                    Vout = vref * (R1 + R2) / R1
                else:
                    Vout = vref * R2 / (R1 + R2)
                if round(Vout * 10.0) / 10.0 == vout_target:
                    print ("R1 = %.1f, R2 = %.1f, Vout = %f" % (R1, R2, Vout))
