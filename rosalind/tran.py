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
seqs = readfasta('test.txt')
str1 = seqs.values()[0]
str2 = seqs.values()[1]
transitions = 0.0
transversions = 0.0
for n in range (0, len(str1)):
	if str1[n] != str2[n]:
		if (str1[n] == 'A' and str2[n] =='G') or (str1[n] == 'G' and str2[n] =='A') or (str1[n] == 'C' and str2[n] =='T') or (str1[n] == 'T' and str2[n] =='C'): transitions += 1
		else: transversions += 1
R = transitions/transversions
print R