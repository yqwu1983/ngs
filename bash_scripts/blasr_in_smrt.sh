#!/bin/bash
# ssh smrtanalysis@172.18.4.4

source /home/smrtanalysis/current/etc/setup.sh

input="/media/4TB1/novymonas/mapping/input.fofn"
genome="/media/4TB1/novymonas/pandoraea_novymonadis.fasta"
base_name="/media/4TB1/novymonas/pandoraea_novymonadis_pacbio"
out=$base_name".sam"
# unaligned="/media/4TB1/novymonas/mapping/pacbio_consensus_quiver3_unaligned.fq"

blasr $input $genome -sam -out $out -nproc 32 -clipping soft #-unaligned $unaligned

samfile=$out
bamfile=$base_name"_unsorted.bam"
sorted=$base_name"_sorted"
sorted_file=$sorted".bam"
mapped_file=$sorted"_mapped.bam"
samtools view -bS -@ 32 $samfile > $bamfile
samtools sort $bamfile $sorted -@ 32
samtools index $sorted_file
