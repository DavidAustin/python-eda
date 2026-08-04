# Generic Python-EDA shell tools

Place these files in `python-eda/tools/` beside the existing Python tools.

## BOM generation

```bash
cd /path/to/board

~/0/github.com/python-eda/tools/make_bom.sh \
    -o adc \
    adc01.sch
```

For a multi-sheet board:

```bash
~/0/github.com/python-eda/tools/make_bom.sh \
    -o backplane \
    backplane01.sch \
    backplane02.sch \
    backplane03.sch
```

Optional Nexar pricing:

```bash
export NEXAR_ACCESS_TOKEN='...'

~/0/github.com/python-eda/tools/make_bom.sh \
    -o backplane \
    backplane*.sch
```

The token is read from the environment. Do not put it in a script or commit it.

Outputs:

```text
backplane.bom.csv
backplane.bom.ordering.csv
backplane.bom.summary.txt
```

## Schematic rendering

```bash
cd /path/to/board

~/0/github.com/python-eda/tools/render_schematics.sh \
    -o backplane.pdf \
    backplane*.sch
```

The default converter is `lepton-cli`.

## Optional shell path

Add the tools directory to `PATH`:

```bash
export PATH="$HOME/0/github.com/python-eda/tools:$PATH"
```

Then use:

```bash
make_bom.sh -o adc adc*.sch
render_schematics.sh -o adc.pdf adc*.sch
```
