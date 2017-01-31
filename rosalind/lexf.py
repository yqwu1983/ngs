#!/usr/bin/python

def lexf_rec(alphabet, n, strings):
    n = n - 1
    result = []
    for l in alphabet:
        for s in strings:
            result.append(l + s)
    if n > 0:
        result = lexf_rec(alphabet, n, result)
    return result


def lexf(alphabet, n, outfile_path):
    alphabet = alphabet.replace(" ", "")
    strings = ['']
    result = lexf_rec(alphabet, n, strings)
    with open(outfile_path, 'w') as outfile:
        for s in result:
            outfile.write("%s\n" % s)
    outfile.closed
    return result



alphabet = 'K Z L S I Q H O M'

n = 3

outfile_path = '/home/anna/bioinformatics/ngs/rosalind/data/lexf_out.txt'

lexf(alphabet, n, outfile_path)
