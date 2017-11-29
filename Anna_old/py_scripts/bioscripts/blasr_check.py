#!/usr/bin/python
e262_alignment = '/home/nenarokova/kinetoplastids/illumina/assembly/E262_contigs_pacbio_blasr.out'
pand_alignment = '/home/nenarokova/kinetoplastids/contaminants/p_apista_blasr_only_reads'

pand = []
for line in open(pand_alignment):
    pand.append(line.rstrip())

for i, line in enumerate(open(e262_alignment)):
    if line[:16] == '         Query: ':
        alignment_id = line[17:].rstrip()
        if alignment_id in pand:
            print alignment_id
