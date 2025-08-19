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

# Goal

Try to standardise fp gen's to:

* DIODE_* - diodes
* IND_* - inductors
* CAP_* - caps
* CONN_* - connectors (created by fp generators mk_CONN*.py)
* CONN_USB_* - USB connectors
* LED_* - LEDs
* RADIAL_* - THT parts (created by fp generator mk_RADIAL*.py)

# Current Footprint Generators:

Should always be postfixed with "-N.py"

SMT: mk_QFN-N.py, mk_WFDFN-N.py, mk_SOIC-N.py, mk_SSOP-N.py, mk_TSSOP-N.py, mk_HTSSOP-N.py, mk_WSOP-N.py, mk_BGA-N.py, mk_uSIP-N.py, mk_pe*.py

THT: mk_CONN*.py, mk_RADIAL*.py, mk_holes.py

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

# gEDA/gaf and LeptonEDA built-in footprints

Under Linux:

$ find /usr/share/pcb/ -name "*.fp" | wc -l
1357

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
  - SOT23_SC59_3 - 3-pin versoin
  - SOT23_SC59_BCE - BCE 3-pin version
  - SOT23_SC59_GSD - GSD 3-pin version
  - SOT23_SC74_5 - 5-pin version
  - SOT23_SC74A_6 - 6-pin version
  
# Footprint Naming

## 📘 JEDEC DO-codes and Common Names

### DO-214 family (surface-mount power diode/TVS)

| JEDEC Code   | Common Name           | Size (L × W mm, approx) | Notes                                        |
| ------------ | --------------------- | ----------------------- | -------------------------------------------- |
| **DO-214AA** | **SMA**               | 4.3 × 2.5               | Smallest of SMA/SMB/SMC family (\~400 W TVS) |
| **DO-214AB** | **SMB**               | 4.6 × 3.6               | Mid-size (\~600 W TVS)                       |
| **DO-214AC** | **SMC**               | 7.0 × 6.2               | Largest (\~1500 W TVS)                       |

---

### DO-219 / SOD family (low-profile / flat power diodes)

| JEDEC Code   | Common Name              | Size (L × W mm, approx) | Notes                                                               |
| ------------ | ------------------------ | ----------------------- | ------------------------------------------------------------------- |
| **DO-219AB** | **SOD-123FL / SOD-123F** | 2.7 × 1.6               | Flat leads, reinforced pads; often used for TVS like **SMF** series |
| **DO-219AC** | **SOD-123HE**            | 3.7 × 1.6               | “High efficiency” variant, slightly longer                          |

---

### DO-41 / DO-35 (axial leaded through-hole)

| JEDEC Code | Common Name             | Size          | Notes              |
| ---------- | ----------------------- | ------------- | ------------------ |
| **DO-41**  | “Rectifier diode axial” | \~5.2 mm body | 1N400x family      |
| **DO-35**  | “Small signal axial”    | \~4 mm body   | 1N4148 glass diode |

---

### Other small-signal SMD diode packages

| JEDEC Code            | Common/Alt Name     | Size (L × W mm, approx)   | Notes                          |
| --------------------- | ------------------- | ------------------------- | ------------------------------ |
| **DO-213AB**          | **MELF / MiniMELF** | Cylindrical, \~3.5 × 1.6  | Glass body, e.g., LL4148       |
| **DO-213AA**          | **MicroMELF**       | Smaller MELF (\~2 × 1.25) | Rare today                     |
| **MO-567**            | **SOD-323**         | 2.5 × 1.25                | ESD suppressors, logic TVS     |
| **JEDEC MO-178**      | **SOT-23**          | 3.0 × 1.3                 | Multi-diode arrays, regulators |

---

### Mapping for TVS “J” series

Vendors tack on **“J”** to show *JEDEC compliant TVS in that package*:

* **SMAJ** → DO-214AC (SMA TVS diode)
* **SMBJ** → DO-214AA (SMB TVS diode)
* **SMCJ** → DO-214AB (SMC TVS diode)
* **SMFJ** → DO-219AB (SOD-123FL TVS diode)
