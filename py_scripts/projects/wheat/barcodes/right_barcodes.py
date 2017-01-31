#!/usr/bin/python
import json
import os
import time
from collections import Counter
from collections import OrderedDict
import distance 
import csv

def compare_barcodes(bcs_counts_file, barcodes):
	bcs_counts_data = open(bcs_counts_file, 'r')
	barcodes_counts = json.load(bcs_counts_data) 
	for barcode in barcodes:
		barcode.append(0)

	all_barcodes = 0
	for barcode_count in barcodes_counts:
		all_barcodes += barcode_count[1]
	
	for barcode_count in barcodes_counts:
		for barcode in barcodes:
			bc_len = len(barcode[1])
			cur_bc = barcode_count[0][0:bc_len]
			if cur_bc == barcode[1]:
			# if distance.hamming(cur_bc, barcode[1]) <= 1:
				barcode[2] += barcode_count[1]
				barcodes_counts.remove(barcode_count)
				break

	right_barcodes = 0
	for barcode in barcodes:
		right_barcodes += barcode[2]	
	bcs_counts_data.close

	print bcs_counts_file
	print "all ", all_barcodes, "right_barcodes", right_barcodes

	out = sorted(barcodes,  key=lambda index: index[2], reverse=False)
	out_file = bcs_counts_file + "_right_barcodes_dist0"
	out_file = open(out_file, 'w')
	out_file.write(json.dumps(out))
	return 0

barcodes = []
barcodes_file = '/home/anna/bioinformatics/wheat/indexes/right_barcodes.csv'

with open(barcodes_file, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader: 
		barcodes.append(row)
	csvfile.close()

process_count = 0
max_processes = 8

f = '/home/anna/bioinformatics/htses/katya/0sec_ACAGTG_L001_R1_001_indexes'
# f = '/home/anna/bioinformatics/htses/ERR015599_1_indexes'

compare_barcodes(f, barcodes)

# files = ['/home/anna/bioinformatics/wheat/indexes/indexes_R1_9', '/home/anna/bioinformatics/wheat/indexes/indexes_R2_9',
# '/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_1_indexes', '/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_2_indexes']

for f in files:
	pid = os.fork()
	time.sleep(0.1)
	if pid == 0:
		print "Process started"
		compare_barcodes(f, barcodes)
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
