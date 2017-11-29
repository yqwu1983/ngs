#!/usr/bin/python
def rev_list_dict(list_dict):
    new_dict = {}
    for key in list_dict:
        for o in list_dict[key]:
            new_dict[o] = key
    return new_dict

def rev_dict(dic):
    new_dict = {}
    for key in dic:
        new_dict[dic[key]] = key
    return new_dict

