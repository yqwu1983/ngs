#!/bin/sh
#this script is not working! :-/
#variables
DATAFILE="/Users/tomas/Data/m6A_review/large_set_results/renamed/"
############################################################
cd $DATAFILE
for i in *_ren.fst
do
    FILENAME=${i%.*}
    sed -E '/>Celega_\d+\n.*\n/d' <"$i" > $FILENAME"_fin.fst"
    #grep -hvE -A 1 ">Celega.*" $i > $FILENAME"_fin.fst"  #print all lines with exception og Celegans species and its sequence
done
