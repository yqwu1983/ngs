#!/bin/bash
# ssh smrtanalysis@172.18.4.4

source /home/smrtanalysis/current/etc/setup.sh

input="/media/4TB3/trypanoplasma/mapping/input.fofn"
genome="/media/4TB3/trypanoplasma/mapping/pacbio_consensus_quiver2.fasta"
out="/media/4TB3/trypanoplasma/mapping/pacbio_reads3.cmp.h5"
pbalign $input $genome $out --nproc 25 --forQuiver



