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
import shutil

if len(sys.argv) < 3:
    print ("Usage: %s output_dir_symbols output_dir_footprints\n" % sys.argv[0])
    exit()

output_dir_symbols = sys.argv[1]
output_dir_footprints = sys.argv[2]

symbols_dir = 'symbols'
tsv_dir = 'tsv'
sym_dir = 'sym'

try:
    shutil.rmtree(output_dir_symbols)
except:
    pass

os.mkdir(output_dir_symbols)

sym_dir_full = os.path.join(symbols_dir, sym_dir)

sym_files = os.listdir(sym_dir_full)

for f in sym_files:
    if ".tsv" in f:
        sym_file = os.path.join(sym_dir_full, f)
        if (os.path.isfile(sym_file)):
            print ("mv %s %s" % (sym_file, output_dir_symbols))
            shutil.copy(sym_file, output_dir_symbols)

tsv_dir_full = os.path.join(symbols_dir, tsv_dir)

f = []
for (dirpath, dirname, filenames) in os.walk(tsv_dir_full):
    for f in filenames:
        print (f)
        sym_file = os.path.splitext(f)[0] + ".sym"
        sym_file = os.path.join(output_dir_symbols, sym_file)
        tsv_file = os.path.join(tsv_dir_full, f)
        if (os.path.isfile(tsv_file)):
            cmd = "tragesym %s %s" % (tsv_file, sym_file)
            print (cmd)
            os.system(cmd)
    break

footprints_dir = 'footprints'
fp_gen_dir = 'gen'
fp_dir = 'fp'

try:
    shutil.rmtree(output_dir_footprints)
except:
    pass

os.mkdir(output_dir_footprints)

fp_dir_full = os.path.join(footprints_dir, fp_dir)

fp_files = os.listdir(fp_dir_full)

for f in fp_files:
    fp_file = os.path.join(fp_dir_full, f)
    if (os.path.isfile(fp_file)):
        print ("mv %s %s" % (fp_file, output_dir_footprints))
        shutil.copy(fp_file, output_dir_footprints)

fp_gen_full = os.path.join(footprints_dir, fp_gen_dir)

f = []
for (dirpath, dirname, filenames) in os.walk(fp_gen_full):
    for f in filenames:
        if "mk_" in f:
            fp_gen_file = os.path.join(fp_gen_full, f)
            if (os.path.isfile(fp_gen_file)):
                cmd = "python %s" % (fp_gen_file)
                print (cmd)
                os.system(cmd)

cmd = "mv *.fp %s" % (output_dir_footprints)
print (cmd)
os.system(cmd) # TODO: make multi-platform
