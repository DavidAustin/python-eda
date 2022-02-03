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
   mk_QFN-N.py, mk_WFDFN-N.py, mk_SOIC-N.py, mk_TSSOP-N.py,
   mk_CONN*.py, mk_RADIAL.py, mk_pe*.py, mk_holes.py
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
