# Python-EDA
# Copyright (C) 2026 COLETEK
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

# Texas Instruments TPD3F303DPVR
# 3-channel ESD protection and EMI filter for SIM card interface.
# Package: DPV / R-PUSON-N8 / USON-8 with exposed thermal/GND pad.
# Datasheet: https://www.ti.com/lit/ds/symlink/tpd3f303.pdf
#
# This footprint uses the same orientation as KiCad's official
# Texas_R-PUSON-N8_USON-8-1EP_1.6x2.1mm_P0.5mm_EP0.4x1.7mm footprint:
#   pads 1..4 down the left side, pads 8..5 down the right side.
# Rotate in PCB layout if you prefer the TI drawing's horizontal orientation.
#
# Pad 9 is a synthetic footprint pad number for the exposed thermal/GND pad.
# The datasheet names this pad GND and notes it must be soldered to the PCB
# for thermal and mechanical performance.

from footprintgen import *

g = FootprintGen("TPD3F303DPVR")

# Nominal body size, oriented to match KiCad footprint naming.
part_w = 1.60
part_h = 2.10

# Signal land pattern dimensions from KiCad IPC generated footprint,
# based on the TI DPV / R-PUSON-N8 mechanical drawing.
pad_w = 0.775
pad_h = 0.250
pitch = 0.500
x_left = -0.7875
x_right = 0.7875
ys = [-0.750, -0.250, 0.250, 0.750]

# Left side pins, top to bottom.
for pin, y in zip([1, 2, 3, 4], ys):
    g.rect_padat(x_left, y, pad_w, pad_h, "%d" % pin)

# Right side pins, top to bottom.
for pin, y in zip([8, 7, 6, 5], ys):
    g.rect_padat(x_right, y, pad_w, pad_h, "%d" % pin)

# Exposed thermal/GND pad.
g.rect_padat(0.0, 0.0, 0.400, 1.700, "9")

# Package outline.
ox1 = -part_w / 2.0
oy1 = -part_h / 2.0
ox2 = part_w / 2.0
oy2 = part_h / 2.0
g.outlinerect(ox1, oy1, ox2, oy2)

# Pin 1 marker, outside top-left corner.
g.outlinecirc(-1.05, -1.15, 0.10)

# Optional centerline marker for exposed pad / visual sanity.
g.outline(0.0, -0.75, 0.0, 0.75, 0.05)

g.write()
