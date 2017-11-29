#!/usr/bin/python
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

def count_right_prot(fasta_path, outpath=False):
    m_starts = 0
    other_starts = 0
    results = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        if record.seq[0] == 'M':
            results.append([record.id, '1'])
            m_starts += 1
        else:
            other_starts += 1
            results.append([record.id, '0'])
    if outpath: write_list_of_lists(results, outpath)
    return m_starts, other_starts

fasta_path='/home/anna/bioinformatics/phd/euglena_project/E_gracilis_transcriptome_final.PROTEINS.fasta'
outpath='/home/anna/bioinformatics/phd/euglena_project/all_proteins_disrupted.csv'
print count_right_prot(fasta_path, outpath)
