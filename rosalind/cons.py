def readfasta (fasta):
    input = open(fasta, 'r')
    seqs = {}
    for line in input:
        if line[0] == '>':
            name = line[1:].rstrip()
            seqs[name] = [] 
        else:
            seqs[name].append(line.rstrip())
    for name in seqs:
        seqs[name] = ''.join(seqs[name])
    return seqs

seqs = readfasta('cons.fasta')
length = len(seqs.values()[0])

nts = dict(A = [0] * length, C = [0] * length, G = [0] * length, T = [0] * length)
consensus = [None] * length

for name in seqs:
    n = 0
    for char in seqs[name]:
        if  char in nts: nts[char][n] += 1
        else: print 'error'
        n += 1

for n in range(0, length):
    max_n = 0
    max_nt = ''
    for nt in nts:
        if nts[nt][n] > max_n:
            max_n = nts[nt][n]
            max_nt = nt
    consensus[n] = max_nt
consensus =  ''.join(consensus)

print consensus
for k, v in nts.iteritems():
    print  str(k) + ": " + ' '.join(map(lambda k: str(k), v))