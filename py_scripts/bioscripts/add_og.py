#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
from py_scripts.bioscripts.gi_to_ccds import *
from py_scripts.bioscripts.mitocarta_to_gi import *

an_path = '/home/anna/bioinformatics/phd/euglena_project/results.csv'

path_og = '/home/anna/bioinformatics/phd/euglena_project/parsed_ortho_groups.csv'

ll = parse_csv(an_path)

ogs = csv_to_list_of_dicts(path_og, delimiter=';')[0]

synonims = { 'Euglena gracilis':'E_gracilis', 'Homo sapiens':'H_sapiens', 'Trypanosoma brucei': 'T_brucei', 'Saccharomyces cerevisiae':'S_cerevisiae' }

results = []
first = True
for l in ll:
    if first:
        first = False
        l.append('query_og')
        l.append('subject_og')
    else:
        query_id = l[0]
        subject_id = l[5]
        subject_organism = l[6]
        query_organism = 'E_gracilis'
        query_og = ''
        subject_og = ''
        finded = [0, 0]
        if subject_id:
            subject_organism = synonims[l[6]]
            if subject_organism == 'H_sapiens':
                subject_ids = gi_to_ccds[mitocarta_to_gi[subject_id]]
        for og in ogs:
            if query_id in og[query_organism]:
                query_og = og['OrthoGroup']
                finded[0] = 1
            if subject_id:
                if subject_organism == 'H_sapiens':
                    for subject_id in subject_ids:
                        if subject_id in og[subject_organism]:
                            subject_og = og['OrthoGroup']
                            finded[1] = 1
                elif subject_id in og[subject_organism]:
                    subject_og = og['OrthoGroup']
                    finded[1] = 1
            else:
                finded[1] = 1
            if finded == [1, 1]: break
        l.append(query_og)
        l.append(subject_og)

    results.append(l)

outpath = '/home/anna/bioinformatics/phd/euglena_project/all_results_with_ogs.csv'
write_list_of_lists(results, outpath)
