#!/bin/bash
cd /home/nenarokova/tools/pilon/target/scala-2.11
genome="//media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver3.fasta"
bam="/media/4TB1/novymonas/mapping/pacbio_reads_quiver_consensus3_sorted.bam"
outdir="/media/4TB3/trypanoplasma/pilon_out/"
output="trypanoplasma_quiver3"
report="/media/4TB3/trypanoplasma/pilon_out/pilon_out_quiver3.txt"
java -Xmx16G -jar pilon_2.11-1.20-one-jar.jar --fix bases,gaps --genome $genome --output $output --outdir $outdir --bam $bam --threads 32 &>$report
