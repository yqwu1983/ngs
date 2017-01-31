#!/usr/bin/python
from math import *

def combination(n, k):
    C_n_k = factorial(n)/(factorial(n-k)*factorial(k))
    return C_n_k

def binom(n, k, p):
    q = 1 - p
    n_k = combination(n, k)
    p = n_k*(p**k)*(q**(n-k))
    return p

def indc(haploid_set):
    n = 2 * haploid_set
    p = 0.5
    result = []
    P = 0
    for k in range(n):
        P += binom(n, k, p)
        result.insert(0, log10(P))
    return result

n = 42

for p in indc(n):
    print p,