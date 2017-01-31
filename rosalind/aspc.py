#!/usr/bin/python
from math import *

def combination(n, k):
    C_n_k = factorial(n)/(factorial(n-k)*factorial(k))
    return C_n_k

def aspc(n, m):
    sset_sum = 0
    for k in range(m, n+1):
        sset_sum += combination(n, k)

    result = sset_sum % 1000000
    return result

n = 1918
m = 1126

print aspc(n, m)