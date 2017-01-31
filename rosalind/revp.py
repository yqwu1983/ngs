from Bio import SeqIO
from string import maketrans
def reverse(seq):
    complement = maketrans('ATGC', 'TACG')
    reverse = seq.translate(complement)[::-1]
    return reverse

f = '/home/anna/Downloads/rosalind_revp.txt'
DNA = str((SeqIO.read(f, 'fasta')).seq)

rss = []

for i in range(len(DNA)):
	for l in range (4,13):
		end = i+l
		if end < len(DNA) + 1:
			rs = DNA[i: i+l]
			if rs == reverse(rs):
				rss.append([i+1, l])

for rs in rss: print rs[0], rs[1]