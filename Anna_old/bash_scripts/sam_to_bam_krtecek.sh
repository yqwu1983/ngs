#!/bin/bash
# PBS -l nodes=1:ppn=60
# PBS -l walltime=10000:00:00

samfile="/home/nenarokova/genomes/trypanoplasma/miniasm/read_mapping.sam"
bamfile="/home/nenarokova/genomes/trypanoplasma/miniasm/read_mapping_unsorted.bam"
sorted="/home/nenarokova/genomes/trypanoplasma/miniasm/read_mapping_sorted"
sorted_file=$sorted".bam"
mapped_file=$sorted"_mapped.bam"
samtools view -bS -@ 60 $samfile > $bamfile
samtools sort $bamfile $sorted -@ 60
samtools index $sorted_file

chmod 644 $sorted_file

samtools view -b -F 4 -@ 60 $sorted_file > $mapped_file
samtools index $mapped_file

chmod 644 $mapped_file
