#!/usr/bin/python
from Bio import SeqIO

min_cov=100
inpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/pandoraea_scaffolds.fasta'
results = []

for record in SeqIO.parse(inpath, "fasta"):
    if float(record.id.split("_")[-1]) > min_cov:
		results.append(record)

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/pandoraea_scaffolds_more_100.fasta'
SeqIO.write(results, outpath, "fasta")
