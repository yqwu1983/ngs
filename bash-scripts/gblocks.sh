#!/bin/sh
#this script is not working! :-/
#variables
DATAFILE="/Users/tomas/Data/m6A_review/large_set_results/renamed/"
GBSET="-b3=8 -b4=4 -b5=h -b6=y -s=y -p=y"
############################################################
#puvodni nastaveni ./Gblocks ALKBH5_OG0008107.fa -b1=10 -b2=12 -b3=8 -b4=10 -b5=h -b6=y -s=y -p=y
cd $DATAFILE
for i in *_fin.fst
do
    FILENAME=${i%.*}
    Gblocks $i $GBSET
done
wait
echo "Gblocks finnished with settings:" $GBSET

