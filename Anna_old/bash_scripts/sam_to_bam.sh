#!/bin/bash
# PBS -l nodes=1:ppn=60
# PBS -l walltime=10000:00:00
source /home/smrtanalysis/current/etc/setup.sh

samfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads_quiver_consensus3.sam"
bamfile="/media/4TB3/trypanoplasma/mapping/pacbio_reads_quiver_consensus3_unsorted.bam"
sorted="/media/4TB3/trypanoplasma/mapping/pacbio_reads_quiver_consensus3_sorted"
sorted_file=$sorted".bam"
mapped_file=$sorted"_mapped.bam"
samtools view -bS -@ 32 $samfile > $bamfile
samtools sort $bamfile $sorted -@ 32
samtools index $sorted_file

chmod 644 $sorted_file

samtools view -b -F 4 -@ 32 $sorted_file > $mapped_file
samtools index $mapped_file

chmod 644 $mapped_file
