#!/usr/bin/python
from Bio import SeqIO

record_id = 'TR34074|c0_g1_i1'

fasta_file = '/home/anna/Dropbox/PhD/bioinformatics/genomes/euglena/data/euglena_all_proteins.fasta'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/euglena/data/euglena_all_proteins_gatb.fasta'

SeqIO.write(result, outpath, "fasta")

