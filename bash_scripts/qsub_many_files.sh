#!/bin/bash
#PBS -d .

folder="/home/nenarokova/contaminants/trimmed_reads/"
cd $folder

f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
/home/nenarokova/tools/FastQC/fastqc $f
