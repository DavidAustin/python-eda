#!/bin/bash

if [ $# -lt 1 ]
then
    echo "Usage: $0 files0*.sch"
    echo ""
    echo "NOTE: currently need to run in the location where the sch are located."
    exit
fi

d=`dirname $0`

for arg in "$@"
do
    #gschem -p -o $arg.ps -s $d/print.scm $arg
    lepton-cli export -p iso_a4 -o $arg.ps $arg
done

gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -sOutputFile=circuit_schematic.pdf *.ps
