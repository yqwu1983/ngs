#!/bin/bash
# PBS -l walltime=100:00:00,cput=10000:00:00,ncpus=60

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
base_name='/home/nenarokova/genomes/novymonas/assembly/azi_spades/azi_scaffolds_cov_more_10'
# $bw2_dir'bowtie2-build' --threads 60 $base_name'.fa' $base_name

s1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_merged_trimmed.fq"
p1_1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_1.fq"
p1_2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_2.fq"
p2_1="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_1_trimmed.fastq"
p2_2="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_2_trimmed.fastq"

alignment=$base_name".sam"
report=$base_name".txt"


unmapped_unpaired=$base_name"_unmapped_unpaired.fq"
unmapped_paired=$base_name"_unmapped_paired.fq"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 60 -x $base_name -1 $p1_1,$p2_1 -2 $p1_2,$p2_2 -U $s1 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted=$base_name"_sorted"
sorted_file=$sorted".bam"

samtools view -bS $samfile > $bamfile -@ 60
samtools sort $bamfile $sorted -@ 60
samtools index $sorted_file

