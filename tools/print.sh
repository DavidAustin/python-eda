#!/bin/bash

d=`dirname $0`

for arg in "$@"
do
    gschem -p -o $arg.ps -s $d/print.scm $arg
done

gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -sOutputFile=circuit_schematic.pdf *.ps
