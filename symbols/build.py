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

import os
import shutil

build_dir='build'
tsv_dir='tsv'
sym_dir='sym'

try:
    shutil.rmtree(build_dir)
except:
    pass

os.mkdir(build_dir)

sym_files = os.listdir(sym_dir)
for f in sym_files:
    sym_file = os.path.join(sym_dir, f)
    if (os.path.isfile(sym_file)):
        print ("cp %s %s" % (sym_file, build_dir))
        shutil.copy(sym_file, build_dir)

f = []
for (dirpath, dirname, filenames) in os.walk(tsv_dir):
    for f in filenames:
        sym_file = os.path.splitext(f)[0] + ".sym"
        sym_file = os.path.join(build_dir, sym_file)
        tsv_file = os.path.join(tsv_dir, f)
        cmd = "tragesym %s %s" % (tsv_file, sym_file)
        print (cmd)
        os.system(cmd)
    break
