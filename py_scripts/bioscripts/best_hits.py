#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

def best_hits(blast_csv_path):
    blast_hits = parse_csv(blast_csv_path)
    blast_hits = sorted(blast_hits, key=lambda bh: ( bh[0], float(bh[5]) ) )
    cur_id = False
    results = []
    for bh in blast_hits:
        if cur_id != bh[0]:
            results.append(bh)
            cur_id = bh[0]
    outpath = blast_csv_path[0:-4] + '_best.csv'
    write_list_of_lists(results, outpath)
    return outpath
