#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

def add_csv_info(main_csv_path, info_csv_path, id_key='seqid', info_id_key='seqid'):
    main_csv, fieldnames = csv_to_list_of_dicts(main_csv_path)
    info, info_fieldnames = csv_to_dict(info_csv_path, info_id_key)
    info_fieldnames.remove(info_id_key)
    fieldnames.extend(info_fieldnames)
    for dic in main_csv:
        key = dic[id_key]
        if key in info:
            cur_info = info[key]
            for k in cur_info:
                dic[k] = cur_info[k]
    outpath = main_csv_path[0:-4] + '_extended.csv'
    write_list_of_dicts(main_csv, outpath, fieldnames=fieldnames)
    return main_csv_path

main_csv_path = '/home/anna/Dropbox/phd/mitoproteome_project/euglena results/proteomics/mt_all_extended_extended.csv'
info_csv_path = '/home/anna/Dropbox/phd/mitoproteome_project/euglena results/proteomics/only_ogs_result.csv'
add_csv_info(main_csv_path, info_csv_path, id_key='og', info_id_key='og')
