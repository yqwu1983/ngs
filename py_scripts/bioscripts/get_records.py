#!/usr/bin/python
from Bio import SeqIO

l = [
"utg000008l|quiver|quiver|quiver",
"utg000035l|quiver|quiver|quiver"
]

fasta = '/home/anna/bioinformatics/genomes/trypanoplasma/pacbio_consensus_quiver3.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/home/anna/bioinformatics/genomes/trypanoplasma/pacbio_consensus_quiver3_most_covered_scaffolds.fasta'

SeqIO.write(results, outpath, "fasta")
