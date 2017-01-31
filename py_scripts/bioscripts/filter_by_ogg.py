#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
from database.nonspecific_functions import *
from database.nonspecific_ogs import *

def get_specific_ogs(dic_list, max_number):
    ogs = {}
    for dic in dic_list:
        if dic['query_og'] in ogs:
            ogs[dic['query_og']] += 1
        else:
            ogs[dic['query_og']] = 1
    specific_ogs = []
    for og in ogs:
        if ogs[og]<=max_number:
            specific_ogs.append(og)
    return specific_ogs

def filter_dic_list(dic_list, outhpath, fieldnames_list, filter_functions=True, specific_ogs=False):
    results = []
    for dic in dic_list:
        if ( (dic['query_loc'] == 'M' and dic['query_locrate'] == 1)
            or
            ( (dic['query_mitoscore'] == 100) and ('double-stranded DNA binding;regulation of transcription' not in dic['query_function']) ) ):
            results.append(dic)
        elif (dic['query_og'] == dic['subject_og']) or (dic['subject_og'] == ''):
            is_specific = True
            if filter_functions:
                for function in nonspecific_functions:
                    if function.lower() in dic['subject_function'].lower() or function in dic['query_function'].lower():
                        is_specific = False
                        break
            elif specific_ogs:
                if dic['query_og'] not in specific_ogs:
                    is_specific = False
                    break
            if is_specific:
                results.append(dic)
    write_list_of_dicts(results, outpath, fieldnames=fieldnames_list)
    return outpath

an_path = '/home/anna/bioinformatics/phd/euglena_project/all_results_with_ogs_and_reverse.csv'

dic_list = csv_to_list_of_dicts(an_path)[0]

fieldnames_list = ['query_id', 'query_function', 'query_mitoscore', 'query_loc', 'query_locrate', 'subject_id', 'subject_organism', 'subject_function', 'evalue', 'qlen', 'slen', 'length', 'alen_slen', 'alen_qlen', 'query_og', 'subject_og', 'bh_id', 'has_reverse_best_blast_hit', 'reverse_alen', 'reverse_evalue']

outpath = '/home/anna/bioinformatics/phd/euglena_project/filtered_by_og.csv'

filter_dic_list(dic_list, outpath, fieldnames_list, filter_functions=False)

outpath = '/home/anna/bioinformatics/phd/euglena_project/filtered_by_specific_ogs.csv'

max_number = 10
specific_ogs = get_specific_ogs(dic_list, max_number)
filter_dic_list(dic_list, outpath, fieldnames_list, specific_ogs=specific_ogs)

