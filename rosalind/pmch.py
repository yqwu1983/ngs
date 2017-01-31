#!/usr/bin/python
from math import factorial
def pmch(rna_string):
    at = 0
    gc = 0
    for nt in rna_string:
        if nt in ('A', 'U'):
            at += 1
        elif nt in ('C', 'G'):
            gc += 1
        else: exit(1)
    result = factorial(at/2)*factorial(gc/2)
    return result

rna_string = 'ACUCAAAACGGGUCAAGUGUCACCGGCUGUAUCUAAGUGCGUUACUCUGGAAGUCGACUUAAGCGUCCUACAUG'
print pmch(rna_string)