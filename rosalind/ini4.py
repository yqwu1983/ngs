min = 4259
max = 8770
odd_numbers = [x for x in range (min, max + 1) if x%2 == 1]
summ = reduce (( lambda x, y : x + y), odd_numbers)
print summ
