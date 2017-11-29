#!/bin/bash
# ssh smrtanalysis@172.18.4.4

source /home/smrtanalysis/current/etc/setup.sh

input="/media/4TB3/trypanoplasma/mapping/pacbio_reads3.cmp.h5"
ref="/media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver2.fasta"

out1="/media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver3.fasta"
out2="/media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver3.fastq"
out3="/media/4TB3/trypanoplasma/mapping/pacbio_variants_quiver3.gff"

quiver -j 25 $input -r $ref -o $out1 -o $out2 -o $out3
