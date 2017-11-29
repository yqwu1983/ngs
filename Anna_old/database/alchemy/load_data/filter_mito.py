#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
from py_scripts.helpers.flatten import *
from Bio import SeqIO

def filter_mito(mitolist_path, fasta_path, outpath):
    mitolist = flatten(parse_csv(mitolist_path))
    results = []
    id_list = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        if record.id in mitolist:
            results.append(record)
            id_list.append(record.id)
    SeqIO.write(results, outpath, "fasta")
    return id_list

mitolist_path = '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/mitolist.csv'
fasta_path = '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/yeast_orf_trans_all.fasta'
outpath = '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.fasta'

print filter_mito(mitolist_path, fasta_path, outpath)
