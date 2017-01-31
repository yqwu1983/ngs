#!/usr/bin/python
def dict_list_to_csv_dict(dict_list, main_key):
    csv_dict = {}
    for dic in dict_list:
        key = dic[main_key]
        csv_dict[key] = {}
        for k in dic:
            if not k == main_key:
                csv_dict[key][k] = dic[k]
    return csv_dict

def dict_list_to_dict(dict_list, key):
    result = {}
    for row in dict_list:
        if row[key] not in result.keys():
            result[row[key]] = []
        result[row[key]].append(row)
    return result