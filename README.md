# python-eda

Python EDA tools (initially gEDA/gaf and Lepton EDA)

# Build

```
python build.py my_output_dir_symbols my_output_dir_footprints
```

Where,
* my_output_dir_symbols is in the geda gafrc file
* my_output_dir_footprints is in the geda pcb .prj file

# Folder usage

* footprints/fp/ - for manually crafted *.fp files
* footprints/gen/ - for mk_*.py generators (used to auto generate *.fp files)
* symbols/sym/ - for manually crafted *.sym files
* symbols/tsv/ - for *.tsv files (used to auto generate *.sym files)

# Built-in symbols and footprints

Under Linux:

$ find /usr/share/pcb/ -name "*.fp" | wc -l

1357

$ find /usr/share/lepton-eda/ -name "*.sym" | wc -l

1488

# Goal

Try to standardise fp gen's to:

* DIODE_* - diodes (see diodes section below)
* IND_* - inductors
* CAP_* - caps
* CONN_* - connectors (created by fp generators mk_CONN*.py)
* CONN_USB_* - USB connectors
* LED_* - LEDs
* RADIAL_* - THT parts (created by fp generator mk_RADIAL*.py)

# Current Footprint Generators:

Should always be postfixed with "-N.py"

SMT: mk_QFN-N.py, mk_VQFN-N.py, mk_TQFP-N.py, mk_WFDFN-N.py, mk_SOIC-N.py, mk_SSOP-N.py, mk_TSSOP-N.py, mk_HTSSOP-N.py, mk_WSOP-N.py, mk_BGA-N.py, mk_uSIP-N.py, mk_pe*.py

THT: mk_CONN*.py, mk_RADIAL*.py, mk_holes.py

NOTE: for custom SMD/SMT's array's use mk_SMD-N.py

# To Do List - up for discussion

1) fp gen - Support for arrays of pins/pads - should be able to do a whole row
   in one function call
2) fp gen - REFDES text and better positioning of REFDES text - better
   footprint metadata
3) fp gen - Support for two-way and four-way symmetrical arrays of pins and
   pads
4) w/x vs l/h/y definition/clarification - perhaps vertical/horizontal
   or stick with x/y standard coordinated frame: x = left/right, y = up/down
5) .sym generator (replacing .tsv) - particular for families
6) .sym to match manufacturer part number - likely the high level .sym
   generator should produce all names in the family
7) Check hole sizes - seems tight
8) Produce ruler for checking footprints
9) Add comment to link datasheet (to clarify dimensions)
10) Should connectors show the minimal outline and maximum outline
   (e.g. plug) - or perhaps two different footprints depending on size
   objectives
11) Enforce 80 char line limit?
12) Increase pin clearance suitable for pcbway design rules
13) Ensure footprints pads are larger then part pads
14) Ensure sch part pin spacing is 500
15) Ensure CONN 0,0 is at pin 1
16) Prefix SMT CAPs with CAP_SMT
17) Remove old radials scripts and use mk_RADIAL.py only
18) Cleanup usb sym's - pin number depends on USB version and connector type.
19) ensure bom created can handle part names with ,

# Diodes

pin 1 is cathode, so becareful when using gEDA/gaf and leptonEDA which provide both options in the symbol, e.g. use diode-3.sym, zenor-3.sym, schottky-1.sym

Below is a list of improvements to some key footprints:

* The built-in TO220/TO22OS/TO220SW/TO220W is the common 3-pin
* The built-in TO220ACSTAND/TO220ACS is the common 2-pin, we offer a better name:
  - TO220_2 - 2-pin
* The built-in TO247 and TO247_2 is the common 3-pin and 2-pin THT, we offer others:
  - TO247_GCE - GCE 3-pin
* The built-in TO263 is common 3-pin + tab SMT, we offer a few others:
  - TO263_GSD - GSD 3-pin + tab
  - TO263_2 - 2-pin + tab
  - TO263_7 - 7-pin + tab
* The built-in SOT23/SOT23D is the common 3-pin SMT, we offer:
  - SOT23_3 - 3-pin versoin
  - SOT23_BCE - BCE 3-pin version
  - SOT23_GSD - GSD 3-pin version
  - SOT23_5 - 5-pin version
  - SOT23_6 - 6-pin version
  
# Footprint Naming Cross-Reference

## **Through-hole power packages**

| Our Footprint  | JEDEC / Std Name                | Common Aliases               | Notes               |
| -------------- | ------------------------------- | ---------------------------- | ------------------- |
| `TO220_2`      | TO-220-2 (JEDEC MO-036, MO-093) | TO-220AB, I-PAK (2 leads)    | Regulators, diodes  |
| `TO247_GCE`    | TO-247AD (JEDEC MO-247)         | TO-3P (vendor), G–C–E (IGBT) | High-power BJT/IGBT |

## **Surface-mount power packages (DPAK / D2PAK)**

| Our Footprint           | Package / JEDEC Outline   | Common Aliases                 | Notes                                      |
|--------------------------|---------------------------|--------------------------------|-------------------------------------------|
| `TO252_3`               | TO-252 (DPAK)             | “TO-252-3 (2 leads + tab)”     | **Diodes** (anode, cathode, **tab = cathode**) |
| `TO252_GSD`             | TO-252 (DPAK)             | DPAK-3, SMD-220                | **MOSFETs** (G–S–D, **tab = D**)          |
| `TO263_2`               | TO-263-2 (D2PAK, MO-169)  | D2PAK-2, SMD-220 large         | **Diodes**, 2 leads + tab                 |
| `TO263_3` / `TO263_GSD` | TO-263-3 (D2PAK, MO-169)  | D2PAK-3                        | **MOSFETs**, tab = D                      |
| `TO263_7`               | TO-263-7 (D2PAK, MO-169)  | D2PAK-7                        | Multi-lead regulators, drivers             |

**Naming note (TO-252):** We follow distributor/JEDEC terminal count for diodes:
* `TO252_3` = “2 leads + tab” - for diodes like symbols/sym/DIODE_TO252_3.sym
* For TO-263 we keep the more common **lead-count style** (`TO263_2`, `TO263_7`).

## **Small-signal transistor packages**

| Our Footprint  | JEDEC / Std Name        | Common Aliases      | Notes                       |
| -------------- | ----------------------- | ------------------- | --------------------------- |
| `SOT23_3`      | TO-236AB (JEDEC MO-178) | SOT-23-3, SC-59     | Generic 3-pin               |
| `SOT23_BCE`    | TO-236AB                | SOT-23 (BCE pinout) | Bipolar transistors         |
| `SOT23_GSD`    | TO-236AB                | SOT-23 (GSD pinout) | MOSFETs                     |
| `SOT23_5`      | JEDEC MO-178 (variant)  | SOT-23-5, SC-74     | Regulators, op-amps         |
| `SOT23_6`      | JEDEC MO-178 (variant)  | SOT-23-6, SC-74A    | Analog switches, FET arrays |
| `SOT416_3`     | JEDEC MO-193 (variant)  | SOT-416, SC-75      | 3-pin numbering (BJTs)      |
| `SOT416_GSD`   | JEDEC MO-193 (variant)  | SOT-416, SC-73      | MOSFET G-S-D mapping        |

## **Surface-mount diode / TVS packages**

| Our Footprint   | JEDEC / Std Name | Common Aliases                 | Notes                     |
| --------------- | ---------------- | ------------------------------ | ------------------------- |
| `DIODE_SMA`     | DO-214AC         | SMA, **SMAJ** (TVS)            | ~4.3 × 2.5 mm             |
| `DIODE_SMB`     | DO-214AA         | SMB, **SMBJ** (TVS)            | ~4.6 × 3.6 mm             |
| `DIODE_SMC`     | DO-214AB         | SMC, **SMCJ** (TVS)            | ~7.0 × 6.2 mm             |
| `DIODE_SOD123`  | —                | SOD-123                        | ~2.7 × 1.6 mm             |
| `DIODE_SOD123F` | DO-219AB         | SOD-123FL, SOD-123F, **SMF**   | Flat-lead TVS form factor |
| `DIODE_SOD323`  | MO-567           | SOD-323, SC-90                 | 2.5 × 1.25 mm             |
| `DIODE_SOD923`  | MO-254           | SOD-923                        | Ultra-mini (1.0 × 0.6 mm) |

## **Key takeaways**

* **TO-252 / TO-263:**  
  - `TO252_3` = diode (2 leads + tab), by distributor convention.  
  - `TO252_GSD` = MOSFET (3 leads + tab).  
  - `TO263_2`, `TO263_3`, `TO263_7` follow lead-count style.
* **SOT / SC naming:**  
  - SC-59 = SOT-23-3  
  - SC-74 = SOT-23-5  
  - SC-74A = SOT-23-6  
  - SC-73 / SC-75 = SOT-416
* **DO / SOD families:**  
  - SMA = DO-214AC  
  - SMB = DO-214AA  
  - SMC = DO-214AB  
  - SOD-123F = DO-219AB (SMF)  
  - SOD-323 = MO-567  
  - SOD-923 = MO-254  
