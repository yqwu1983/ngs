#!/bin/sh
# Data located on Trypka server
cd /media/4TB3/Tomas_data/Reads_mappings_bbmap
#fastqc Free_1_un-mapped_reads_paired.fastq &
#fastqc Free_2_un-mapped_reads_paired.fastq &
#fastqc Free_3_un-mapped_reads_paired.fastq &
#fastqc Sessile_1_un-mapped_reads_paired.fastq &
#fastqc Sessile_2_un-mapped_reads_paired.fastq &
#fastqc Sessile_3_un-mapped_reads_paired.fastq
#perl ./fastq2fasta.pl --infile=Free_1_un-mapped_reads_paired.fastq > Free_1_un-mapped_reads_paired.fasta
#perl ./fastq2fasta.pl --infile=Free_2_un-mapped_reads_paired.fastq > Free_2_un-mapped_reads_paired.fasta &
#perl ./fastq2fasta.pl --infile=Free_3_un-mapped_reads_paired.fastq > Free_3_un-mapped_reads_paired.fasta &
#perl ./fastq2fasta.pl --infile=Sessile_1_un-mapped_reads_paired.fastq > Sessile_1_un-mapped_reads_paired.fasta &
#perl ./fastq2fasta.pl --infile=Sessile_2_un-mapped_reads_paired.fastq > Sessile_2_un-mapped_reads_paired.fasta &
#perl ./fastq2fasta.pl --infile=Sessile_3_un-mapped_reads_paired.fastq > Sessile_3_un-mapped_reads_paired.fasta
sixpack -reverse Y -sequence Free_1_un-mapped_reads_paired.fa -outfile Free_1_un-mapped_reads_paired_6frames -outseq Free_1_un-mapped_reads_paired_6frames_ORFs &
sixpack -reverse Y -sequence Free_2_un-mapped_reads_paired.fasta -outfile Free_2_un-mapped_reads_paired_6frames -outseq Free_2_un-mapped_reads_paired_6frames_ORFs &
sixpack -reverse Y -sequence Free_3_un-mapped_reads_paired.fasta -outfile Free_3_un-mapped_reads_paired_6frames -outseq Free_3_un-mapped_reads_paired_6frames_ORFs &
sixpack -reverse Y -sequence Sessile_1_un-mapped_reads_paired.fasta -outfile Sessile_1_un-mapped_reads_paired_6frames -outseq Sessile_1_un-mapped_reads_paired_6frames_ORFs &
sixpack -reverse Y -sequence Sessile_2_un-mapped_reads_paired.fasta -outfile Sessile_2_un-mapped_reads_paired_6frames -outseq Sessile_2_un-mapped_reads_paired_6frames_ORFs &
sixpack -reverse Y -sequence Sessile_3_un-mapped_reads_paired.fasta -outfile Sessile_3_un-mapped_reads_paired_6frames -outseq Sessile_3_un-mapped_reads_paired_6frames_ORFs
