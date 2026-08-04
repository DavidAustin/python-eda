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
# Render one or more gEDA/Lepton EDA schematic sheets to a single PDF.
#
# This script is intended to live in python-eda/tools beside print.py.
#
# Examples:
#
#   tools/render_schematics.sh -o adc.pdf adc*.sch
#
#   tools/render_schematics.sh \
#       --converter lepton-cli \
#       -o backplane.pdf \
#       backplane01.sch backplane02.sch
#
# By default, temporary PostScript files produced in the current
# directory are removed. Any PostScript files that existed before the
# command are backed up and restored.

set -Eeuo pipefail

usage() {
    cat <<'EOF'
Usage:
  render_schematics.sh [options] SCHEMATIC.sch [SCHEMATIC.sch ...]

Options:
  -o, --output FILE.pdf
      Output PDF. Default:
        - one input sheet: the sheet basename with .pdf
        - multiple sheets: current directory basename with .pdf

  -c, --converter NAME
      Converter passed to print.py. Default: lepton-cli

  --keep-ps
      Keep PostScript files produced by print.py.

  -h, --help
      Show this help.

Environment:
  PYTHON
      Python interpreter. Default: python3

  PYTHON_EDA_HOME
      Optional python-eda repository root. When unset, the script uses
      the directory containing this script.

  EDA_SCHEMATIC_CONVERTER
      Default converter when --converter is not supplied.

Examples:
  render_schematics.sh -o adc.pdf adc*.sch

  render_schematics.sh -o controller.pdf \
      controller01.sch controller02.sch
EOF
}

die() {
    printf 'render_schematics.sh: error: %s\n' "$*" >&2
    exit 1
}

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ -n "${PYTHON_EDA_HOME:-}" ]]; then
    tools_dir="${PYTHON_EDA_HOME%/}/tools"
else
    tools_dir="$script_dir"
fi

python_bin="${PYTHON:-python3}"
print_tool="${tools_dir}/print.py"
converter="${EDA_SCHEMATIC_CONVERTER:-lepton-cli}"
output_file=""
keep_ps=0
schematics=()

while (($#)); do
    case "$1" in
        -o|--output)
            (($# >= 2)) || die "$1 requires a value"
            output_file="$2"
            shift 2
            ;;
        -c|--converter)
            (($# >= 2)) || die "$1 requires a value"
            converter="$2"
            shift 2
            ;;
        --keep-ps)
            keep_ps=1
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

[[ -f "$print_tool" ]] \
    || die "missing tool: $print_tool"

for schematic in "${schematics[@]}"; do
    [[ -f "$schematic" ]] \
        || die "schematic does not exist: $schematic"
done

if [[ -z "$output_file" ]]; then
    if ((${#schematics[@]} == 1)); then
        first_name="$(basename -- "${schematics[0]}")"
        output_file="${first_name%.sch}.pdf"
    else
        output_file="$(basename -- "$PWD").pdf"
    fi
fi

output_dir="$(dirname -- "$output_file")"
mkdir -p -- "$output_dir"

working_dir="$PWD"
tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/python-eda-render.XXXXXXXX")"
ps_backup_dir="${tmp_dir}/existing-ps"
mkdir -p -- "$ps_backup_dir"

shopt -s nullglob
existing_ps=("$working_dir"/*.ps)
shopt -u nullglob

for ps_file in "${existing_ps[@]}"; do
    cp -a -- "$ps_file" "$ps_backup_dir/"
done

cleanup() {
    status=$?

    if ((keep_ps == 0)); then
        shopt -s nullglob
        generated_or_existing_ps=("$working_dir"/*.ps)
        shopt -u nullglob

        if ((${#generated_or_existing_ps[@]} > 0)); then
            rm -f -- "${generated_or_existing_ps[@]}"
        fi

        shopt -s nullglob
        backups=("$ps_backup_dir"/*.ps)
        shopt -u nullglob

        for backup in "${backups[@]}"; do
            cp -a -- "$backup" "$working_dir/"
        done
    fi

    rm -rf -- "$tmp_dir"
    exit "$status"
}
trap cleanup EXIT INT TERM

printf 'Rendering %d schematic sheet(s) to %s\n' \
    "${#schematics[@]}" "$output_file" >&2

"$python_bin" "$print_tool" \
    -o "$output_file" \
    --converter "$converter" \
    "${schematics[@]}"

[[ -s "$output_file" ]] \
    || die "rendering completed without creating a non-empty output: $output_file"

printf 'Generated:\n  %s\n' "$output_file"
