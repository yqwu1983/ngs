n = 88
k = 10

pper = 1

for i in range (n, n-k, -1):
	pper = (pper * i)%1000000

print pper