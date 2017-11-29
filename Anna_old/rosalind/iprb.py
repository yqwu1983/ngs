k = 1.0
m = 1.0
n = 1.0
s = k + m + n

Pmm = m*(m-1)/(s*(s-1))
Pmn = m*n/(s*(s-1))
Pnn = n*(n-1)/(s*(s-1))

q = 0.25*Pmm + Pmn + Pnn
p = 1.0 - q

print p
