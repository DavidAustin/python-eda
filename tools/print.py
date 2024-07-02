import os
import sys
import subprocess
import glob
import argparse

def convert_schematic(converter, schematic, script_dir):
    if converter == 'gschem':
        subprocess.run(['gschem', '-p', '-o', f'{schematic}.ps', '-s', os.path.join(script_dir, 'print.scm'), schematic])
    elif converter == 'lepton-cli':
        subprocess.run(['lepton-cli', 'export', '-p', 'iso_a4', '-o', f'{schematic}.ps', schematic])
    else:
        raise ValueError("Unsupported converter. Use 'gschem' or 'lepton-cli'.")

def main():
    parser = argparse.ArgumentParser(description="Convert schematic files to a single PDF.")
    parser.add_argument('-o', '--output', type=str, required=True, help='The output PDF filename.')
    parser.add_argument('schematics', nargs='+', type=str, help='The schematic (.sch) files to be converted.')
    parser.add_argument('--converter', type=str, choices=['gschem', 'lepton-cli'], default='lepton-cli', help='The converter to use (gschem or lepton-cli).')

    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))

    for schematic in args.schematics:
        convert_schematic(args.converter, schematic, script_dir)

    ps_files = glob.glob('*.ps')
    subprocess.run(['gs', '-sDEVICE=pdfwrite', '-dNOPAUSE', '-dBATCH', '-dSAFER', '-sOutputFile=' + args.output] + ps_files)

if __name__ == '__main__':
    main()
