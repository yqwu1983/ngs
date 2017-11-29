#!/usr/bin/python
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from helpers.parse_csv import *

def b2g_to_functions(b2g_dict):
    result = {}
    for seqid in b2g_dict:
        function = b2g_dict[seqid]['SeqDesc']  + ', ' +  b2g_dict[seqid]['GOTerms']
        result[seqid] = {}
        result[seqid]['function'] = function
    return result

def add_mitoscore(b2dict, mitogenes_csv_path):
    mitogenes_csv = parse_csv(mitogenes_csv_path)
    mitogenes = []
    for row in mitogenes_csv:
        mitogenes.append(row[0])
    results = {}

    for key in b2dict:
        results[key] = b2dict[key]
        if key in mitogenes:
            results[key]['mitoscore'] = 100
        else:
            results[key]['mitoscore'] = 0

    return results

def prepare_for_loading(b2g_csv_path, mitogenes_csv_path):
    seq_info_dict = seq_info_to_dict(b2g_csv_path)
    b2g_functions_dict = b2g_to_functions(seq_info_dict)
    result = add_mitoscore(b2g_functions_dict, mitogenes_csv_path)
    return result

mitogenes_csv_path = '/home/anna/bioinformatics/euglena_project/euglena/other_sequences/mitogenes_223/223_mitogenes.csv'
b2g_csv_path = '/home/anna/bioinformatics/euglena_project/euglena/all_euglena_proteins/blast2go_annotdescriptions_20151104_1903.csv'
outfile = '/home/anna/bioinformatics/euglena_project/euglena/all_euglena_proteins/euglena_function_info.csv'

result = prepare_for_loading(b2g_csv_path, mitogenes_csv_path)

write_dict_of_dicts(result, outfile, key_name='seqid')
