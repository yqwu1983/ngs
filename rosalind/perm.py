#!/usr/bin/python

def rec_perm(s):
    if len(s) > 2:
        orderings = []
        for number in s:
            new_set = list(s)
            new_set.remove(number)
            number_orderings = rec_perm(new_set)
            for ordering in number_orderings:
                ordering.append(number)
            orderings.extend(number_orderings)
        return orderings
    else:
        orderings = [
                        [ s[0], s[1] ],
                        [ s[1], s[0] ]
                    ]
    return orderings

def perm(n):
    s = range(1, n + 1)
    orderings = rec_perm(s)
    print len(orderings)
    for o in orderings:
        print ' '.join(str(x) for x in o)
    return orderings



n = 7

perm(n)
