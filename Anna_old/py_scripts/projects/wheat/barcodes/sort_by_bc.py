#!/usr/bin/python
import json
import os
import time
import distance 
import csv

def compare_barcodes(bcs_counts_file, right_bcs_file, dist=0):
	bcs_counts_open = open(bcs_counts_file, 'r')
	bcs_counts = json.load(bcs_counts_open) 
	bcs_counts_open.close()

	all_barcodes = 0
	for bcs_count in bcs_counts:
		all_barcodes += bcs_count[1]

	right_bcs = []
	right_bcs_file = open(right_bcs_file, 'rb')
	bc_reader = csv.reader(right_bcs_file)
	for row in bc_reader: 
		right_bcs.append(row)
	right_bcs_file.close()
	barcodes = []
	i = 0

	for right_bc in right_bcs:
		right_bc.append(0)
		barcodes.append(right_bc)
		for bcs_count in bcs_counts:
			cur_bc = bcs_count[0][0:len(right_bc[1])]
			if dist == 0:
				if right_bc[1] == cur_bc:
					# print barcodes
					barcodes[i][2] += bcs_count[1]
					bcs_counts.remove(bcs_count)
			else:
				if distance.hamming(right_bc[1], cur_bc) <= dist:
					barcodes[i][2] += bcs_count[1]
					bcs_counts.remove(bcs_count)
		i += 1

	right_barcodes = 0
	for barcode in barcodes:
		right_barcodes += barcode[2]
	print bcs_counts_file
	print "all ", all_barcodes, "right_barcodes", right_barcodes
	barcodes = sorted(barcodes,  key=lambda index: index[2], reverse=False)
	out_file = bcs_counts_file + "_right_barcodes_dist" + str(dist)
	out_file = open(out_file, 'w')
	out_file.write(json.dumps(barcodes))
	out_file.close()
	return 0

right_bcs_file = '/home/anna/bioinformatics/wheat/indexes/right_barcodes.csv'
f = "/home/anna/bioinformatics/htses/katya/indexes_result"
compare_barcodes(f, right_bcs_file)

# files = ['/home/anna/bioinformatics/wheat/indexes/indexes_R1_9', '/home/anna/bioinformatics/wheat/indexes/indexes_R2_9',
# '/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_1_indexes', '/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_2_indexes']

# process_count = 0
# max_processes = 8
# for f in files:
# 	pid = os.fork()
# 	time.sleep(0.1)
# 	if pid == 0:
# 		print "Process started"
# 		compare_barcodes(f, right_bcs_file, dist = 1)
# 		print "Process ended"
# 		os._exit(0)
# 	else:
# 		process_count += 1
# 		if process_count >= max_processes:
# 			os.wait()
# 			process_count -= 1

# for i in range(process_count):
# 	os.wait()
