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
	json.dump(counts, open(out_file,'w'))
	return 0

folder = '/home/nenarokova/wheat/R2/'
files = os.listdir(folder) 
fastq_files = filter(lambda x: x.endswith('.fastq'), files) 

process_count = 0
max_processes = 24

for f in fastq_files:
	fastq_file = folder + f
	pid = os.fork()
	time.sleep(0.1)
	if pid == 0:
		print "Process started"
		index (fastq_file)
		print "Process ended"
		os._exit(0)

	else:
		process_count += 1
		if process_count >= max_processes:
			os.wait()
			process_count -= 1

for i in range(process_count):
	os.wait()

print "All ended"

indexes_count_files = filter(lambda x: x.endswith('_indexes'), files) 
indexes_counts = Counter({})

for f in indexes_count_files:
	json_file = folder + f
	json_data = open(json_file, 'r')
	indexes_counts += Counter(json.load(json_data))
	json_data.close


out_file = folder + "indexes_result"
out_file = open(out_file, 'w')
out_file.write(json.dumps(indexes_counts.most_common()))
