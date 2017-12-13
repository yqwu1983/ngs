#!/bin/sh
for i in *_ren.fa
do
    FILENAME=${i%.*}
    grep -hv
