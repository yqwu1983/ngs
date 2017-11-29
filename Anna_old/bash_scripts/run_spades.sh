#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

se1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_merged_trimmed.fq"
pe1_1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_1.fq"
pe1_2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_2.fq"

pe2_1="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_1_trimmed.fastq"
pe2_2="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_2_trimmed.fastq"

contigs="/home/nenarokova/genomes/novymonas/assembly/anzhelika/E262_contigs.fa"

outdir="/home/nenarokova/genomes/novymonas/assembly/wt_all_spades/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.9.0-Linux/bin/spades.py --s1 $se1 --pe1-1 $pe1_1 --pe1-2 $pe1_2 --pe2-1 $pe2_1 --pe2-2 $pe2_2 --untrusted-contigs $contigs --careful -t 60 -o $outdir 2> $report
