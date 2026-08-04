#!/usr/bin/env bash
#
# Python-EDA
# Copyright (C) 2026 Luke Cole
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Generate a BOM from one or more gEDA/Lepton EDA schematic sheets.
#
# This script is intended to live in python-eda/tools beside:
#   gschem_bom.py
#   bom_with_qty.py
#
# Examples:
#
#   tools/make_bom.sh -o adc adc01.sch
#
#   tools/make_bom.sh -o backplane \
#       backplane01.sch backplane02.sch backplane03.sch
#
#   NEXAR_ACCESS_TOKEN='...' tools/make_bom.sh -o adc adc*.sch
#
# Outputs:
#
#   <prefix>.bom.csv
#       One clean, ungrouped CSV containing components from every sheet.
#
#   <prefix>.bom.ordering.csv
#       Components grouped by the existing bom_with_qty.py tool.
#
#   <prefix>.bom.summary.txt
#       Per-sheet totals and missing-price counts emitted by
#       gschem_bom.py.
#
# Notes:
#
# - Pricing is optional. Set NEXAR_ACCESS_TOKEN or
#   OCTOPART_NEXAR_ACCESS_TOKEN in the environment to enable it.
# - Do not store access tokens in this script or in a board repository.
# - Existing output files are replaced only after all processing succeeds.

set -Eeuo pipefail

usage() {
    cat <<'EOF'
Usage:
  make_bom.sh [options] SCHEMATIC.sch [SCHEMATIC.sch ...]

Options:
  -o, --output-prefix PREFIX
      Output prefix. Default:
        - one input sheet: the sheet basename
        - multiple sheets: current directory basename

  --no-pricing
      Ignore any Nexar token in the environment.

  -h, --help
      Show this help.

Environment:
  PYTHON
      Python interpreter. Default: python3

  PYTHON_EDA_HOME
      Optional python-eda repository root. When unset, the script uses
      the directory containing this script.

  NEXAR_ACCESS_TOKEN
      Optional Nexar access token used by gschem_bom.py.

  OCTOPART_NEXAR_ACCESS_TOKEN
      Backward-compatible alternative token variable.

Examples:
  make_bom.sh -o adc adc01.sch

  make_bom.sh -o controller \
      controller01.sch controller02.sch

  NEXAR_ACCESS_TOKEN='...' make_bom.sh -o controller controller*.sch
EOF
}

die() {
    printf 'make_bom.sh: error: %s\n' "$*" >&2
    exit 1
}

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ -n "${PYTHON_EDA_HOME:-}" ]]; then
    tools_dir="${PYTHON_EDA_HOME%/}/tools"
else
    tools_dir="$script_dir"
fi

python_bin="${PYTHON:-python3}"
gschem_bom="${tools_dir}/gschem_bom.py"
bom_with_qty="${tools_dir}/bom_with_qty.py"

output_prefix=""
use_pricing=1
schematics=()

while (($#)); do
    case "$1" in
        -o|--output-prefix)
            (($# >= 2)) || die "$1 requires a value"
            output_prefix="$2"
            shift 2
            ;;
        --no-pricing)
            use_pricing=0
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        --)
            shift
            while (($#)); do
                schematics+=("$1")
                shift
            done
            ;;
        -*)
            die "unknown option: $1"
            ;;
        *)
            schematics+=("$1")
            shift
            ;;
    esac
done

((${#schematics[@]} > 0)) || {
    usage >&2
    exit 2
}

command -v "$python_bin" >/dev/null 2>&1 \
    || die "Python interpreter not found: $python_bin"

[[ -f "$gschem_bom" ]] \
    || die "missing tool: $gschem_bom"

[[ -f "$bom_with_qty" ]] \
    || die "missing tool: $bom_with_qty"

for schematic in "${schematics[@]}"; do
    [[ -f "$schematic" ]] \
        || die "schematic does not exist: $schematic"
done

if [[ -z "$output_prefix" ]]; then
    if ((${#schematics[@]} == 1)); then
        first_name="$(basename -- "${schematics[0]}")"
        output_prefix="${first_name%.sch}"
    else
        output_prefix="$(basename -- "$PWD")"
    fi
fi

output_dir="$(dirname -- "$output_prefix")"
mkdir -p -- "$output_dir"

raw_output="${output_prefix}.bom.csv"
ordering_output="${output_prefix}.bom.ordering.csv"
summary_output="${output_prefix}.bom.summary.txt"

tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/python-eda-bom.XXXXXXXX")"

cleanup() {
    rm -rf -- "$tmp_dir"
}
trap cleanup EXIT INT TERM

raw_tmp="${tmp_dir}/combined.bom.csv"
ordering_tmp="${tmp_dir}/combined.bom.ordering.csv"
summary_tmp="${tmp_dir}/combined.bom.summary.txt"

: > "$raw_tmp"
: > "$summary_tmp"

token=""
if ((use_pricing)); then
    token="${NEXAR_ACCESS_TOKEN:-${OCTOPART_NEXAR_ACCESS_TOKEN:-}}"
fi

first_sheet=1

for index in "${!schematics[@]}"; do
    schematic="${schematics[$index]}"
    sheet_tmp="${tmp_dir}/sheet-${index}.txt"

    command=(
        "$python_bin"
        "$gschem_bom"
        -i "$schematic"
    )

    if [[ -n "$token" ]]; then
        command+=(-k "$token")
    fi

    printf 'Processing %s\n' "$schematic" >&2
    "${command[@]}" > "$sheet_tmp"

    grep -q '^refdes,' "$sheet_tmp" \
        || die "gschem_bom.py produced no CSV header for: $schematic"

    {
        printf '[%s]\n' "$schematic"
        grep '^Total (' "$sheet_tmp" || true
        printf '\n'
    } >> "$summary_tmp"

    # Keep one CSV header, discard per-sheet totals, and avoid duplicated
    # headers when combining several schematic sheets.
    awk -v keep_header="$first_sheet" '
        /^Total \(/ {
            next
        }

        /^refdes,/ {
            if (keep_header == 1) {
                print
            }
            next
        }

        NF {
            print
        }
    ' "$sheet_tmp" >> "$raw_tmp"

    first_sheet=0
done

"$python_bin" "$bom_with_qty" "$raw_tmp" > "$ordering_tmp"

# Replace completed outputs atomically within their destination directory.
raw_stage="${raw_output}.tmp.$$"
ordering_stage="${ordering_output}.tmp.$$"
summary_stage="${summary_output}.tmp.$$"

cp -- "$raw_tmp" "$raw_stage"
cp -- "$ordering_tmp" "$ordering_stage"
cp -- "$summary_tmp" "$summary_stage"

mv -f -- "$raw_stage" "$raw_output"
mv -f -- "$ordering_stage" "$ordering_output"
mv -f -- "$summary_stage" "$summary_output"

printf '\nGenerated:\n'
printf '  %s\n' "$raw_output"
printf '  %s\n' "$ordering_output"
printf '  %s\n' "$summary_output"
