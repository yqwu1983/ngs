#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
def convert_evalue(evalue):
    if evalue == '': result = 100
    else: result = float(evalue)
    return result

def get_og_statistics(dic_list, outhpath, fieldnames):
    og_statistics = {}
    for dic in dic_list:
        query_og = dic['query_og']
        new_dic = dic.copy()
        if query_og in og_statistics.keys():
            cur_evalue = convert_evalue(dic['evalue'])
            prev_evalue = convert_evalue(og_statistics[query_og]['evalue'])
            if cur_evalue < prev_evalue:
                new_dic['og_size'] = og_statistics[query_og]['og_size'] + 1
                og_statistics[query_og] = new_dic
            else:
                og_statistics[query_og]['og_size']+=1
        else:
            new_dic['og_size']=1
            og_statistics[query_og] = new_dic


    write_dict_of_dicts(og_statistics, outpath, key_name='query_og', fieldnames=fieldnames)
    return outpath

an_path = '/home/anna/bioinformatics/phd/euglena_project/filtered_by_og.csv'

dic_list = csv_to_list_of_dicts(an_path)[0]

fieldnames = ['query_id', 'query_og', 'og_size', 'subject_function', 'query_function', 'query_mitoscore', 'query_loc', 'query_locrate', 'subject_id', 'subject_og', 'subject_organism', 'evalue', 'qlen', 'slen', 'length', 'alen_slen', 'alen_qlen',  'bh_id']
outpath = '/home/anna/bioinformatics/phd/euglena_project/filtered_euglena_mito_ogs.csv'
get_og_statistics(dic_list, outpath, fieldnames)
