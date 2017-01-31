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

def list_of_lists_to_dict_reverse(list_of_lists):
    first = True
    dic = {}
    for l in list_of_lists:
        if first:
            keys = l[1::]
            for key in keys:
                dic[key] = {}
            first = False
        else:
            key2 = l[0]
            for key1, value in zip(keys, l[1:]):
                dic[key1][key2] = value
    return dic