#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
cd /home/nenarokova/genomes/novymonas/assembly/wt_all_spades/
$bw2_dir'bowtie2-build' --threads 60 contigs.fasta wt_novymonas

bt2_base='/home/nenarokova/genomes/novymonas/assembly/wt_all_spades/wt_novymonas'

s1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_merged_trimmed.fq"
p1_1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_1.fq"
p1_2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_2.fq"
p2_1="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_1_trimmed.fastq"
p2_1="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_2_trimmed.fastq"

unmapped_reads="/home/nenarokova/genomes/novymonas/assembly/mapping/wt_unmapped_reads.gz"

base_name="/home/nenarokova/genomes/novymonas/assembly/mapping/wt_all"
alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 60 -x $bt2_base -1 $fw_paired -2 $rv_paired --un-gz $clean_reads_unpaired --un-conc-gz $clean_reads_paired -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted=$base_name"_sorted"
sorted_file=$sorted".bam"

samtools view -bS $samfile > $bamfile -@ 60
samtools sort $bamfile $sorted -@ 60
samtools index $sorted_file

