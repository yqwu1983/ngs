from collections import Counter
s = 'We tried list and we tried dicts also we tried Zen'
words = s.split(' ')
count = Counter()
for word in words:
    count[word] += 1
    count
print count
