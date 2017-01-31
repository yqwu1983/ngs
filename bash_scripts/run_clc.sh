#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=32

reads1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/without_endosym_trimmed/azi_S1_L001_trimmed_1P.fq"
reads2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/without_endosym_trimmed/azi_S1_L001_trimmed_2P.fq"
reads3="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/without_endosym_trimmed/azi_S1_L001_trimmed_1U.fq"
reads4="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/without_endosym_trimmed/azi_S1_L001_trimmed_2U.fq"
/home/nenarokova/tools/clc-assembly-cell-5.0.1-linux_64/clc_assembler -o contigs.fasta -p fb ss 180 1000 -q -i $reads1 $reads2 -q $reads3 $reads4 --cpus 32
