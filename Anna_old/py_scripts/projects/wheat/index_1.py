#!/usr/bin/python
import os
import time
import json
from Bio import SeqIO
from collections import Counter
global INDEX_LENGTH; INDEX_LENGTH = 9

def index (fastq_file):
	out_file = fastq_file[0:-6] + '_indexes'
	indexes = []
	for seq_record in SeqIO.parse(fastq_file, "fastq"):
		indexes.append(str(seq_record.seq[0:INDEX_LENGTH]))
	counts = Counter(indexes)
	json.dump(counts.most_common(), open(out_file,'w'))
	return 0

fastq_file = '/home/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1.fastq'
index (fastq_file)
