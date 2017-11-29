#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

bt2_base='/home/nenarokova/genomes/hinxton_species/contaminants/genomes/leptomonas'

folder="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_trimmed/with_endosym_trimmed/"

fw_paired=$folder"wt_S2_L001_trimmed_1P.fq"
rv_paired=$folder"wt_S2_L001_trimmed_2P.fq"
fw_unpaired=$folder"wt_S2_L001_trimmed_1U.fq"
rv_unpaired=$folder"wt_S2_L001_trimmed_2U.fq"

clean_reads_paired="/home/nenarokova/genomes/novymonas/mapping/l_pyrrhocoris/with_endosym_trimmed_clean_paired.fq.gz"
clean_reads_unpaired="/home/nenarokova/genomes/novymonas/mapping/l_pyrrhocoris/with_endosym_trimmed_clean_unpaired.fq.gz"


alignment="/home/nenarokova/genomes/novymonas/mapping/l_pyrrhocoris/wt_S2_L001_trimmed.sam"
report="/home/nenarokova/genomes/novymonas/mapping/l_pyrrhocoris/wt_S2_L001_trimmed.txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 60 -x $bt2_base -1 $fw_paired -2 $rv_paired --un-gz $clean_reads_unpaired --un-conc-gz $clean_reads_paired -S $alignment 2> $report
