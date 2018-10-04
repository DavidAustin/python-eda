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


def make_flags_str(opts):
    # TODO support integer opts - or mixed
    can_opts = {}
    if isinstance(opts, dict):
        can_opts.update(opts)
    
    return ','.join(can_opts.keys())

    
def frommm(m):
    return m / 25.4 * 1e5

def tomm(i):
    return i * 25.4
