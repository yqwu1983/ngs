#!/usr/bin/python
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

def cut_proteins_M(fasta_path, outpath):
    results = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        for i, aa in enumerate(record.seq):
            if aa == 'M' and i > 5:
                results.append(record[i::])
                break
    SeqIO.write(results, outpath, "fasta")
    return outpath

fasta_path='/home/anna/bioinformatics/phd/euglena_project/E_gracilis_transcriptome_final.PROTEINS.fasta'
outpath='/home/anna/bioinformatics/phd/euglena_project/E_gracilis_transcriptome_final.PROTEINS_M_cut.fasta'
cut_proteins_M(fasta_path, outpath)
