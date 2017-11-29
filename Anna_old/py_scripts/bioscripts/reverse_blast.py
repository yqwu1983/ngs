#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

an_path = '/home/anna/bioinformatics/phd/euglena_project/all_results_with_ogs.csv'
reverse_path = '/home/anna/bioinformatics/phd/euglena_project/all_results_reverse.csv'

an = parse_csv(an_path)

reverse = csv_to_list_of_dicts(reverse_path)[0]

results = []
first = True
for row in an:
    euglena_id = row[0]
    other_id = row[5]
    if first:
        first = False
        row.append('reverse_alen')
        row.append('reverse_evalue')
    else:
        for dic in reverse:
                if other_id == dic['query_id'] and euglena_id == dic['subject_id']:
                    row.append(dic['length'])
                    row.append(dic['evalue'])
                    break
    results.append(row)


outpath = '/home/anna/bioinformatics/phd/euglena_project/all_results_with_ogs_and_reverse.csv'
write_list_of_lists(results, outpath)
