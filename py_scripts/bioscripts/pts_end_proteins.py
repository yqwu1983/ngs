#!/usr/bin/python
from Bio import SeqIO
import sys

def pts_skl(fasta_path, outpath):
    results = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        if str(record.seq[-3::]) == 'SKL':
            results.append(record)
    SeqIO.write(results, outpath, "fasta")
    return 0

fasta_path='/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_all_proteins.fasta'
outpath='/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_proteins_skl.fasta'

pts_skl(fasta_path, outpath)
