n = 93
m = 17
babies = [1]
adult = [0]
for x in range(1, n):
    babies.append(adult[x-1])
    if x >= m:
        adult.append(babies[x-1]+ adult[x-1] - babies[x-m])
    else:
        adult.append(babies[x-1]+ adult[x-1])
print babies[-1] + adult[-1]
