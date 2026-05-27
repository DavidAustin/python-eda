# Python-EDA
# Footprint generator for Nordic Semiconductor nRF9151-LACA-R
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Prepared from Nordic nRF9151 Product Sheet v1.1 mechanical dimensions,
# with pad locations cross-checked against the KiCad official footprint:
#   Nordic_nRF9151-LAxx_LGA-80-33EP_12.1x11.1mm_P0.5mm.kicad_mod
#
# Notes:
# - Coordinates are in mm, top-view PCB orientation.
# - Pin 1 is the upper-left corner.
# - The 80 perimeter pads use 0.5 mm pitch.
# - Pads 81..104 are RESERVED/DNC mechanical lands.
# - Pads 105..113 are exposed GND lands.
# - For production RF work, compare against Nordic's current reference layout,
#   PCB stack-up, paste-mask, and assembly recommendations before fab.

from footprintgen import *


g = FootprintGen("NRF9151-LACA-R")


def pad(n, x, y, w, h):
    g.rect_padat(x, y, w, h, "%d" % n)


# -----------------------------------------------------------------------------
# Nominal package body outline, mm
# -----------------------------------------------------------------------------
PART_W = 12.1
PART_H = 11.1


# -----------------------------------------------------------------------------
# Perimeter LGA pads 1..80
# -----------------------------------------------------------------------------
PITCH = 0.5
CORNER_PAD = 0.70
SIDE_PAD_W = 0.45
SIDE_PAD_H = 0.30
EDGE_PAD_W = 0.30
EDGE_PAD_H = 0.45

# Corner pads
pad(1,  -5.50, -5.00, CORNER_PAD, CORNER_PAD)
pad(20, -5.50,  5.00, CORNER_PAD, CORNER_PAD)
pad(41,  5.50,  5.00, CORNER_PAD, CORNER_PAD)
pad(60,  5.50, -5.00, CORNER_PAD, CORNER_PAD)

# Left side, pins 2..19, top to bottom
for i, n in enumerate(range(2, 20)):
    pad(n, -5.625, -4.25 + i * PITCH, SIDE_PAD_W, SIDE_PAD_H)

# Bottom side, pins 21..40, left to right
for i, n in enumerate(range(21, 41)):
    pad(n, -4.75 + i * PITCH, 5.125, EDGE_PAD_W, EDGE_PAD_H)

# Right side, pins 42..59, bottom to top
for i, n in enumerate(range(42, 60)):
    pad(n, 5.625, 4.25 - i * PITCH, SIDE_PAD_W, SIDE_PAD_H)

# Top side, pins 61..80, right to left
for i, n in enumerate(range(61, 81)):
    pad(n, 4.75 - i * PITCH, -5.125, EDGE_PAD_W, EDGE_PAD_H)


# -----------------------------------------------------------------------------
# Internal RESERVED / DNC mechanical lands 81..104
# -----------------------------------------------------------------------------
reserved_pads = [
    (81,  -4.10, -3.40),
    (82,  -4.10, -2.85),
    (83,  -4.10, -2.30),
    (84,  -4.10, -0.55),
    (85,  -4.10,  0.00),
    (86,  -4.10,  0.55),
    (87,  -4.10,  2.30),
    (88,  -4.10,  2.85),
    (89,  -4.10,  3.40),
    (90,  -0.55,  2.15),
    (91,   0.00,  2.15),
    (92,   0.55,  2.15),
    (93,   4.10,  3.40),
    (94,   4.10,  2.85),
    (95,   4.10,  2.30),
    (96,   4.10,  0.55),
    (97,   4.10,  0.00),
    (98,   4.10, -0.55),
    (99,   4.10, -2.30),
    (100,  4.10, -2.85),
    (101,  4.10, -3.40),
    (102,  0.55, -2.15),
    (103,  0.00, -2.15),
    (104, -0.55, -2.15),
]

for n, x, y in reserved_pads:
    pad(n, x, y, 0.30, 0.30)


# -----------------------------------------------------------------------------
# Internal exposed GND lands 105..113
# -----------------------------------------------------------------------------
gnd_pads = [
    (105, -2.85, -2.85, 1.60, 1.60),
    (106, -2.85,  0.00, 1.60, 1.60),
    (107, -2.85,  2.85, 1.60, 1.60),
    (108,  0.00,  3.575, 1.60, 1.95),
    (109,  2.85,  2.85, 1.60, 1.60),
    (110,  2.85,  0.00, 1.60, 1.60),
    (111,  2.85, -2.85, 1.60, 1.60),
    (112,  0.00, -3.575, 1.60, 1.95),
    (113,  0.00,  0.00, 1.60, 1.60),
]

for n, x, y, w, h in gnd_pads:
    pad(n, x, y, w, h)


# -----------------------------------------------------------------------------
# Mechanical outline and pin-1 mark
# -----------------------------------------------------------------------------
ox1 = -PART_W / 2.0
oy1 = -PART_H / 2.0
ox2 = PART_W / 2.0
oy2 = PART_H / 2.0

g.outlinerect(ox1, oy1, ox2, oy2)

# Pin 1 marker outside the upper-left corner.
g.outlinecirc(ox1 - 0.45, oy1 - 0.45, 0.18)


g.write()
