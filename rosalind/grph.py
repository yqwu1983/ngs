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

seqs = readfasta('input.fasta')

result = open('result.txt', 'w')

for cur_seq in seqs:
    for seq in seqs:
        if cur_seq != seq:
            if seqs[cur_seq][-3 :] == seqs[seq][:3]:
                result.write(cur_seq + ' ' + seq + "\n")

result.close