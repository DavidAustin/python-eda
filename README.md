# python-eda

Python EDA tools (initially gEDA)

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

# To Do List - up for discussion

1) fp gen - Support for arrays of pins/pads - should be able to do a whole row
   in one function call
2) fp gen - REFDES text and better positioning of REFDES text - better
   footprint metadata
3) fp gen - Support for two-way and four-way symmetrical arrays of pins and
   pads
4) use a footprint family generator such as:
   mk_QFN-N.py, mk_WFDFN-N.py, mk_SOIC-N.py, mk_SSOP-N.py, mk_TSSOP-N.py, mk_HTSSOP-N.py, mk_WSOP-N.py,
   mk_BGA-N.py, mk_uSIP-N.py, mk_CONN*.py, mk_RADIAL*.py, mk_pe*.py, mk_holes.py
5) Naming standard for family generators - perhaps postfix with "-N"
6) w/x vs l/h/y definition/clarification - perhaps vertical/horizontal
   or stick with x/y standard coordinated frame: x = left/right, y = up/down
7) Merge mk_peSOT23_GSD.py and mk_SOT23_3.py
8) .sym generator (replacing .tsv) - particular for families
9) .sym to match manufacturer part number - likely the high level .sym
   generator should produce all names in the family
10) Check hole sizes - seems tight
11) Produce ruler for checking footprints
12) Add comment to link datasheet (to clarify dimensions)
13) More standardization:
    * uppercase vs lowercase
    * - vs _
    * should / characters be replaced with -
14) Should connectors show the minimal outline and maximum outline
   (e.g. plug) - or perhaps two different footprints depending on size
   objectives
15) Enforce 80 char line limit?
16) Increase pin clearance suitable for pcbway design rules
17) Ensure CONN prefix for all connectors - e.g. usb
18) Ensure footprints pads are larger then part pads
19) Ensure sch part pin spacing is 500
20) Ensure CONN 0,0 is at pin 1
21) Prefix SMT CAPs with CAP-SMT
22) Remove old radials scripts and use mk_RADIAL.py only
23) Cleanup usb sym's - pin number depends on USB version and connector type.
24) ensure bom created can handle part names with ,
25) Improve inductor making standing (e.g. mk_IND_*.py, mk_SRN8040-3R3Y.py, mk_SRR6038-100Y.py, mk_SRU1048-100Y.py, mk_NPI54C100MTRF.py)
26) Drop tvs_vert.sym? Now replaced via tvs_bi.sym ("CA") and tvs_uni.sym ("A")
27) symlinks for common names of JEDEC DO-codes? See below notes, currently effecting fp's:
    mk_SMA.py, depreciated/mk_DO214AC.py (aka DO214AC)
    mk_SMB.py (aka DO214AA)
    mk_SMC.py, depreciated/mk_SMC.py, depreciated/mk_DO214AB.py (aka DO214AB)
    mk_peSOD123FL.py depreciated/mk_SOD123F.py depreciated/mk_SOD123FL.py, (aka DO219AB/SOD123F/SOD123FL)
    mk_SOD_923.py - I don't think this fits the JEDEC DO-codes?
    NOTE: mk_peSOD123 is not like SOD123F/SOD123FL - and not a JEDEC standard name


## 📘 JEDEC DO-codes and Common Names

### DO-214 family (surface-mount power diode/TVS)

| JEDEC Code   | Common Name           | Size (L × W mm, approx) | Notes                                        |
| ------------ | --------------------- | ----------------------- | -------------------------------------------- |
| **DO-214AC** | **SMA**               | 4.3 × 2.5               | Smallest of SMA/SMB/SMC family (\~400 W TVS) |
| **DO-214AA** | **SMB** (a.k.a. SMBJ) | 4.6 × 3.6               | Mid-size (\~600 W TVS)                       |
| **DO-214AB** | **SMC**               | 7.0 × 6.2               | Largest (\~1500 W TVS)                       |

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
| **MO-567** (not “DO”) | **SOD-323**         | 2.5 × 1.25                | ESD suppressors, logic TVS     |
| **JEDEC MO-178**      | **SOT-23**          | 3.0 × 1.3                 | Multi-diode arrays, regulators |

---

### Mapping for TVS “J” series

Vendors tack on **“J”** to show *JEDEC compliant TVS in that package*:

* **SMAJ** → DO-214AC (SMA TVS diode)
* **SMBJ** → DO-214AA (SMB TVS diode)
* **SMCJ** → DO-214AB (SMC TVS diode)
* **SMFJ** → DO-219AB (SOD-123FL TVS diode)
