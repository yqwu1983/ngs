input = open('rosalind_gc (1).txt', 'r')
seqs = {}
max_gc = 0
name_max_gc = ''
for line in input:
    if line[0] == '>':
        name = line[1:].rstrip()
        seqs[name] = [] 
    else:
        seqs[name].append(line.rstrip())
for name in seqs:
    seqs[name] = ''.join(seqs[name])
    cur_gc = (float(seqs[name].count('G') + seqs[name].count('C')))/len(seqs[name])*100
    if cur_gc > max_gc :
        max_gc = cur_gc
        name_max_gc = name
print name_max_gc
print max_gc

input.close
