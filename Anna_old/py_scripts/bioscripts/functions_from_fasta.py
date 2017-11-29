#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from Bio import SeqIO
from py_scripts.helpers.parse_csv import *

def functions_from_fasta(fasta_path, outpath):
    result = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        result.append([record.id, record.description])
    write_list_of_lists(result, outpath)
    return outpath


fasta_path = '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis.fasta'
outpath = '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis.csv'

functions_from_fasta(fasta_path, outpath)
