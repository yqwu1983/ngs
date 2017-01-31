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
    input.close
    return seqs

def findmotif (seqs):
    seq1 = min(seqs, key=len)
    length = len(seq1)
    for n in range(length - 1, 0, -1):
        max_shift = length - n + 1
        for shift in range(0, max_shift):
            motif = seq1[shift : shift + n]
            for i in range (0, len(seqs)):
                if motif not in seqs[i]: break
            else: return motif
         
file1 = 'test.txt'
seqs = list(readfasta(file1).values())

a = findmotif(seqs)
print 'lastmotif', a
