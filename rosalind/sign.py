#!/usr/bin/python

def sign_perm(s):
    if len(s) > 2:
        orderings = []
        for number in s:
            new_set = list(s)
            new_set.remove(number)
            number_orderings = sign_perm(new_set)
            minus_number_orderings = []
            for ordering in number_orderings:
                ordering.append(number)
                minus_number_ordering = list(ordering)
                minus_number_ordering[-1] *= -1
                minus_number_orderings.append(minus_number_ordering)
            orderings.extend(number_orderings)
            orderings.extend(minus_number_orderings)
        return orderings
    else:
        orderings = []
        for i in (1, -1):
            for k in (1, -1):
                orderings.append( [ s[0]*i, s[1]*k ] )
                orderings.append( [ s[1]*i, s[0]*k ] )
    return orderings

def sign(n, outf_path):
    s = range (1, n + 1)
    orderings = sign_perm(s)
    with open(outf_path, 'w') as outf:
        outf.write(str(len(orderings))+'\n')
        for o in orderings:
            outf.write(' '.join(str(x) for x in o)+'\n')
        outf.closed
    return orderings

n = 4

outf_path = '/home/anna/bioinformatics/ngs/rosalind/data/sign_out.txt'

sign(n, outf_path)
