from math import factorial

def bernulli(k, n, p):
	q = 1 - p
	c = factorial(n) / (factorial(k) * factorial (n-k))
	result = c * (p**k) * (q ** (n-k))
	return result

p = 0.25

gen = 7
het_child = 33

children = 2 ** gen
P = 0

for k in range (children, het_child - 1, -1):
	Pk = bernulli(k, children,  p)
	P += Pk

print P