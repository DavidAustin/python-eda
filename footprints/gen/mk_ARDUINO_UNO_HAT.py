# Python-EDA
# Copyright (C) 2026 Luke Cole
#
# Arduino UNO R3 shield footprint generator for pcb/pcb-rnd/LeptonEDA flow.
#
# Pad names match symbols/tsv/ARDUINO_UNO.tsv:
#
#   0..13   = D0..D13
#   14      = GND beside AREF
#   15      = AREF
#   16      = SDA/A4/D18, R3 duplicate I2C header
#   17      = SCL/A5/D19, R3 duplicate I2C header
#   18..25  = NC, IOREF, RESET, 3V3, 5V, GND, GND, VIN
#   26..31  = A0..A5
#
# Coordinate basis:
#   Uses Arduino UNO R3 shield header coordinates, shifted so the board outline
#   is roughly at x=0..68.58 mm, y=0..-53.34 mm.
#
# Notes:
#   - This does not include the 2x3 ICSP header.
#   - The odd Arduino digital header gap between D7 and D8 is preserved.
#   - Mounting holes are non-electrical holes.

import math
from footprintgen import *

# Keep this name if your symbol has:
#   footprint=ARDUINO_UNO_HAT
#
# Better long-term name would be:
#   fn = 'ARDUINO_UNO_R3_SHIELD'
fn = 'ARDUINO_UNO_HAT'

g = FootprintGen('%s' % fn)

pitch = 2.54

# UNO R3 board envelope, approximately 2.7" x 2.1".
board_w = 68.58
board_h = 53.34

# Header hole and annulus sizes, same style as your RPI_HAT generator.
hole_d = 1.0
ann_d = 1.8

# Header outline margin around pin centres.
oo = 1.23

# KiCad-style Arduino shield coordinates use power header pin 1 at x=0, y=0.
# Convert to this generator's top-left-ish coordinate style:
#   x = xk + 27.94
#   y = yk - 50.80
#
# This places:
#   board left   ~= 0
#   board right  ~= 68.58
#   board top    ~= 0
#   board bottom ~= -53.34
x_offset = 27.94
y_top_k = 50.80


def xy(xk, yk):
    return xk + x_offset, yk - y_top_k


def pinat_k(xk, yk, name, square=False):
    x, y = xy(xk, yk)
    opts = {'square': 1} if square else {}
    g.pinat(x, y, hole_d, ann_d, name, opts)


def holeat_k(xk, yk, d_hole):
    x, y = xy(xk, yk)
    g.holeat(x, y, d_hole)


def outline_header_k(points):
    xs = []
    ys = []

    for xk, yk in points:
        x, y = xy(xk, yk)
        xs.append(x)
        ys.append(y)

    g.outlinerect(min(xs) - oo, min(ys) - oo,
                  max(xs) + oo, max(ys) + oo)


# Board outline.
g.outlinerect(0, 0, board_w, -board_h)


# ---------------------------------------------------------------------------
# Bottom headers
# ---------------------------------------------------------------------------

# Power header, left-to-right:
#   NC, IOREF, RESET, 3.3V, 5V, GND, GND, VIN
power_pins = ['18', '19', '20', '21', '22', '23', '24', '25']
power_points = []

for i, name in enumerate(power_pins):
    xk = i * pitch
    yk = 0.0
    power_points.append((xk, yk))
    pinat_k(xk, yk, name, square=(i == 0))

outline_header_k(power_points)


# Analog header, left-to-right:
#   A0, A1, A2, A3, A4/SDA, A5/SCL
analog_pins = ['26', '27', '28', '29', '30', '31']
analog_points = []

for i, name in enumerate(analog_pins):
    xk = 22.86 + i * pitch
    yk = 0.0
    analog_points.append((xk, yk))
    pinat_k(xk, yk, name, square=(i == 0))

outline_header_k(analog_points)


# ---------------------------------------------------------------------------
# Top headers
# ---------------------------------------------------------------------------

# Digital header, right side, right-to-left:
#   D0, D1, D2, D3, D4, D5, D6, D7
digital_0_7_pins = ['0', '1', '2', '3', '4', '5', '6', '7']
digital_0_7_points = []

for i, name in enumerate(digital_0_7_pins):
    xk = 35.56 - i * pitch
    yk = 48.26
    digital_0_7_points.append((xk, yk))
    pinat_k(xk, yk, name, square=(i == 0))

outline_header_k(digital_0_7_points)


# Digital/R3 header, right-to-left:
#   D8, D9, D10, D11, D12, D13, GND, AREF, SDA, SCL
#
# The first pin here starts at x=13.72 rather than 15.24, preserving the
# weird Arduino offset gap between D7 and D8.
digital_8_13_r3_pins = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
digital_8_13_r3_points = []

for i, name in enumerate(digital_8_13_r3_pins):
    xk = 13.72 - i * pitch
    yk = 48.26
    digital_8_13_r3_points.append((xk, yk))
    pinat_k(xk, yk, name, square=(i == 0))

outline_header_k(digital_8_13_r3_points)


# ---------------------------------------------------------------------------
# Mounting holes
# ---------------------------------------------------------------------------

# UNO-compatible mounting-hole centres.
# Use 3.2 mm holes for M3 / 4-40 style clearance.
mounting_hole_d = 3.2

mounting_holes = [
    (-13.97, 0.00),
    (-12.70, 48.26),
    (38.10, 33.02),
    (38.10, 5.08),
]

for xk, yk in mounting_holes:
    holeat_k(xk, yk, mounting_hole_d)


g.write()

