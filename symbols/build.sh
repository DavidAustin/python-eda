#!/bin/bash

rm -rf build
mkdir build
for file in tsv/*.tsv
do
    tragesym $file build/$(basename -s tsv $file)sym
done

rsync -av sym/ build

