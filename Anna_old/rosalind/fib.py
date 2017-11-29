n = 24
k = 1
pairs = [1, 1]
for x in range(2, n):
    pairs.append(pairs[x-1] + k * pairs[x-2])
print pairs[-1]
