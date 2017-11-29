#!/usr/bin/python

def lexv_rec(alphabet, n, strings):
    n = n - 1
    result = []
    for s in strings:
        if s[-1] == ' ':
            result.append(s)
        else:
            for l in alphabet:
                result.append(s + l)
    if n > 0:
        result = lexv_rec(alphabet, n, result)
    return result


def lexv(alphabet, n, outfile_path):
    alphabet = alphabet.split(" ")
    strings = list(alphabet)
    alphabet.insert(0, ' ')
    result = lexv_rec(alphabet, n-1, strings)
    with open(outfile_path, 'w') as outfile:
        for s in result:
            outfile.write("%s\n" % s)
    outfile.closed
    return result



alphabet = 'G P Y Q T A U H D V'

n = 4

outfile_path = '/home/anna/bioinformatics/ngs/rosalind/data/lexv_out.txt'

lexv(alphabet, n, outfile_path)
