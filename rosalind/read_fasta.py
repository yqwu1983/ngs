def readfasta_dict (fasta):
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