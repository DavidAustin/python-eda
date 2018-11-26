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
