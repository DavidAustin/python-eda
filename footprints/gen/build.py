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
pyfp_dir='.'

try:
    shutil.rmtree(build_dir)
except:
    pass

os.mkdir(build_dir)

f = []
for (dirpath, dirname, filenames) in os.walk(pyfp_dir):
    for f in filenames:
        if "mk_" in f:
            pyfp_file = os.path.join(pyfp_dir, f)
            cmd = "python %s" % (pyfp_file)
            print (cmd)
            os.system(cmd)

cmd = "mv *.fp %s" % (build_dir)
print (cmd)
os.system(cmd)
