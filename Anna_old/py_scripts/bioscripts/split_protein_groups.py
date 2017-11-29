#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

def split_protein_groups(csv_path, outpath=False):
    rows = parse_csv(csv_path)
    results = []
    for i, row in enumerate(rows):
        if i == 0:
            header = ['group_id', 'seqid']
            row.extend(header)
            results.append(row)
        else:
            group_id = i
            for seqid in row[1].split(';'):
                result = list(row)
                result.extend([group_id, seqid])
                results.append(result)
    if not outpath: outpath = csv_path[0:-4] + '_splitted_major.csv'
    write_list_of_lists(results, outpath)
    return outpath

csv_path = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/euglena_new/all_protein_data.csv'
split_protein_groups(csv_path, outpath=False)
