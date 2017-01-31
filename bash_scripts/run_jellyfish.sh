#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=32

f="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/wt_S2_L001_trimmed_2U.fq"

jellyfish count -m 22 -s 300M -t 32 $f
