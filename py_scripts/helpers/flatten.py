#!/usr/bin/python

def flatten(list_of_lists):
    result = [item for sublist in list_of_lists for item in sublist]
    return result