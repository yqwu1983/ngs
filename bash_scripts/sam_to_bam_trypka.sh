#!/bin/bash
samfile="/media/4TB1/blasto/mapping/p57_bw2.sam"
bamfile="/media/4TB1/blasto/mapping/p57_bw2_unsorted.bam"
sorted="/media/4TB1/blasto/mapping/p57_bw2_sorted"
sorted_file=$sorted".bam"

samtools view -bS $samfile > $bamfile -@ 32
samtools sort -T $sorted -o $sorted_file -@ 32 $bamfile
samtools index $sorted_file
