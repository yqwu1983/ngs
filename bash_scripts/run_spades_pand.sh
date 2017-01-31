#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

se1="/home/nenarokova/genomes/novymonas/assembly/azi_spades/azi_scaffolds_cov_more_10_unmapped_unpaired.fq"
pe1_1="/home/nenarokova/genomes/novymonas/assembly/azi_spades/azi_scaffolds_cov_more_10_unmapped_paired.fq.1.gz"
pe1_2="/home/nenarokova/genomes/novymonas/assembly/azi_spades/azi_scaffolds_cov_more_10_unmapped_paired.fq.2.gz"

outdir="/home/nenarokova/genomes/novymonas/assembly/pandoraea/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.9.0-Linux/bin/spades.py --s1 $se1 --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 60 -o $outdir 2> $report
