#!/usr/bin/python
from math import *
import os

def prob(string, gcc_array):
    result = []
    gcc_array = gcc_array.split(' ')
    for gc_c in gcc_array:
        gcc = float(gc_c)
        gc_p = gcc/2
        at_p = (1-gcc)/2
        log_p = 0
        for s in string:
            if s in ('A', 'T'):
                p = at_p
            elif s in ('G', 'C'):
                p = gc_p
            else:
                print 'Undefined symbol'
                os.exit(1)
            log_p += log10(p)
        result.append(log_p)

    return result

string = 'CAAAGGTGACTTGTCAGCTGTCCAAATTCACTAGAAGTCGTTTAGTACCAGCGCCGTTTTTCTGTATCGCGCCACGTGAGC'
gcc_array = '0.065 0.145 0.174 0.255 0.293 0.342 0.440 0.454 0.549 0.597 0.664 0.714 0.734 0.813 0.886 0.918'


for i in prob(string, gcc_array):
    print i,