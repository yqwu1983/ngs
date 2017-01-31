#!/usr/bin/python
import itertools

global RULES; 

RULES = {
	'R': ['A', 'G'],
	'Y': ['C', 'T'],
	'S': ['G', 'C'],
	'W': ['A', 'T'],
	'K': ['G', 'T'],
	'M': ['A', 'C'],
	'B': ['C', 'G', 'T'],
	'D': ['A', 'G', 'T'],
	'H': ['A', 'C', 'T'],
	'V': ['A', 'C', 'G'],
	'N': ['A', 'C', 'G', 'T'],
	'I': ['A', 'C', 'G', 'T']
}

def convert_ambiguous(seq):
	sequence = []
	for s in seq:
		if s in RULES:
			sequence.append(RULES[s])
		else:
			sequence.append([s])

	return map(lambda x: ''.join(x), list(itertools.product(*tuple(sequence))))


seqs = ['GTWGTYTTICCYRAICCIGGCATICC', 'GTWGTYTTICCYRAICCISSCAT', 'TGTGGAGGRTTACCTCTAGC', 'ATTGTTGGRATGGGMGGIMTIGG', 'YYTKRTHGTMITKGATGAYGTITGG', 'YYTKRTHGTMITKGATGATATITGG']
result = []

for seq in seqs:
	result.extend(convert_ambiguous(seq))

print len(result)