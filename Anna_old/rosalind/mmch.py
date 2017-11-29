#!/usr/bin/python
from math import factorial
def mmch(seq):
    a = seq.count("A")
    c = seq.count("C")
    g = seq.count("G")
    t = seq.count("U")
    result = a * c * g * t
    return result

rna_string = 'ACUCAAAACGGGUCAAGUGUCACCGGCUGUAUCUAAGUGCGUUACUCUGGAAGUCGACUUAAGCGUCCUACAUG'
print mmch(rna_string)