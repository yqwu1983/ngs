#!/bin/bash
#PBS -d .
dir1="/home/nenarokova/genomes/novymonas/raw_illumina/WT_MiSeq_trimmed/with_endosym_trimmed/"
dir2="/home/nenarokova/genomes/novymonas/raw_illumina/WT_MiSeq_trimmed/without_endosym_trimmed/"

cd $dir2
f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
/home/nenarokova/tools/FastQC/fastqc $f
