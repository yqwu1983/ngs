#!/usr/bin/python
import json
import os
from collections import Counter
from collections import OrderedDict
import distance 
barcodes = ["TGTTTACGA", "TTAGTACGA", "GGAATACGA", "AAGTCACGA", "CTGCCACGA", "TGAACACGA", "TCCGAACGA", "GATTTACGA", "TCAATACGA", "GTGCGACGA", "TGCTCACGA", "TTCCCACGA", "GAAACACGA", "CTTCAACGA", "ATGTTACGA", "ACAGTACGA", "TTTTGACGA", "ACGCGACGA", "GTATCACGA", "ACACCACGA", "GGTCAACGA", "CTCTTACGA", "AATTGACGA", "AACCGACGA", "TCATCACGA", "GGTACACGA", "CAGTAACGA", "TATCAACGA", "GGCTTACGA", "AAGCTACGA", "GGGTGACGA", "CAACGACGA", "TTTGCACGA", "ACTACACGA", "AGCTAACGA", "ATCCAACGA", "AACTTACGA", "GTCCTACGA", "AGATGACGA", "CTTAGACGA", "ATGGCACGA", "TATACACGA", "CTATAACGA", "GACCAACGA", "TGACTACGA", "GAATGACGA", "TAGGCACGA", "AGTGTACGA", "TTGACACGA", "GGATAACGA", "CCACTACGA", "TGGGGACGA", "GAGAGACGA", "AACGCACGA", "AGGACACGA", "AATGAACGA", "GCACAACGA", "GGGGTACGA", "CGTATACGA", "AAGGGACGA", "GGCAGACGA", "GGAGCACGA", "CAGACACGA", "CTGGAACGA", "AAACAACGA", "CCGGTACGA", "GCTATACGA", "CTCGGACGA", "ACCAGACGA", "CCAGCACGA", "CTCACACGA", "AGGGAACGA", "AGTAAACGA", "TGCGTACGA", "GTGATACGA", "CCAAGACGA", "GTTCCACGA", "TCCACACGA", "CCTAAACGA", "CACGTACGA", "TACATACGA", "GCTTCACGA", "CATCCACGA", "ATAACACGA", "CGCGAACGA", "GGGAAACGA", "TGCGACGA", "TCACCCGA"]
# json_file = "/home/anna/bioinformatics/htses/katya/indexes_result"
# json_file = '/home/anna/bioinformatics/wheat/indexes/indexes_R1_9'
json_file = '/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_1_indexes'
json_data = open(json_file, 'r')

indexes_counts = json.load(json_data) 
indexes = []
i = 0
for count in indexes_counts:
		not_in_indexes = True
		if len(indexes) > 0:
			for barcode in barcodes:
				if distance.hamming(count[0], barcodes) <= 1:
					index[1] += count[1]
					not_in_indexes = False
		if not_in_indexes:
			indexes.append([count[0], count[1]])
json_data.close

indexes = sorted(indexes,  key=lambda index: index[1], reverse=True)
out_file = json_file + "_dist1"
out_file = open(out_file, 'w')
out_file.write(json.dumps(indexes))