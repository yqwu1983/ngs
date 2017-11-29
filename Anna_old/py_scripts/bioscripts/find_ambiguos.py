#!/usr/bin/python
def find_ambiguos(pattern, seq):
	rules = {
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
	
	while end < len(seq)

