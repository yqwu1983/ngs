#!/usr/bin/python
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_dicts import *

def parse_csv(csv_path, delimiter=','):
    with open(csv_path) as handle_file:
        handle_csv = csv.reader(handle_file, delimiter=delimiter)
        results = []
        for row in handle_csv:
            results.append(row)
        handle_file.close()
    return results

def csv_to_list_of_dicts(csv_path, delimiter=','):
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=None, delimiter=delimiter)
        list_of_dicts = []
    	for row in reader:
        	list_of_dicts.append(row)
        fieldnames = reader.fieldnames
        csvfile.close
    return list_of_dicts, fieldnames

def csv_to_dict(csv_path, main_key):
    list_of_dicts, fieldnames = csv_to_list_of_dicts(csv_path)
    csv_dict = dict_list_to_csv_dict(list_of_dicts, main_key)
    return csv_dict, fieldnames

def csv_to_dict_reverse(csv_path, delimiter=','):
    list_of_lists = parse_csv(csv_path, delimiter=delimiter)
    dic = list_of_lists_to_dict_reverse(list_of_lists)
    return dic

def write_list_of_lists(list_of_lists, outpath, delimiter=',', header=False):
    with open(outpath, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        if header: writer.writerow(header)
        writer.writerows(list_of_lists)
        csvfile.close()
    return outpath

def write_list_of_dicts(list_of_dicts, outpath, fieldnames=False):
    with open(outpath, 'w') as csvfile:
        if not fieldnames:
            fieldnames = list_of_dicts[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dicts:
            writer.writerow(row)
        csvfile.close()
	return outpath

def write_dict_of_dicts(dict_of_dicts, outpath, key_name=False, fieldnames=False):
	list_of_dicts = []
	for key in dict_of_dicts:
		cur_dict = {}
		cur_dict[key_name] = key
		for k in dict_of_dicts[key]:
			cur_dict[k] = dict_of_dicts[key][k]
		list_of_dicts.append(cur_dict)
	write_list_of_dicts(list_of_dicts, outpath, fieldnames)
	return outpath
