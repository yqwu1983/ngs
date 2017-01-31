#!/usr/bin/python
from Bio import SeqIO

fasta_file = '/home/anna/bioinformatics/phd/trypanoplasma/miniasm_contigs.fasta'
out_file = '/home/anna/bioinformatics/phd/trypanoplasma/miniasm_contigs_sorted.fasta'
seqs = list(SeqIO.parse(fasta_file, "fasta"))
print len(seqs[0].seq)
seqs = sorted(seqs, key=lambda seqrecord: -len(seqrecord.seq))
print len(seqs[0].seq)
SeqIO.write(seqs, out_file, "fasta")
