#!/usr/bin/python
from math import *

def combination(n, k):
    C_n_k = factorial(n)/(factorial(n-k)*factorial(k))
    return C_n_k

def sset(n):
    result = 2 ** n
    return result


n = 810
result = sset(n) % 1000000

print result