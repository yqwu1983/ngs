#!/usr/bin/python
import json
import os
import time
import distance 
import csv

def compare_barcodes(b_counts_file, barcodes_file, dist=0):
	b_counts = json.load(open(b_counts_file, 'r')) 
	b_counts_file.close()

	all_barcodes = 0
	for b_count in b_counts:
		all_barcodes += b_count[1]
		
	b_reader = csv.reader(open(barcodes_file, 'rb'))
	for row in b_reader: 
		barcodes.append(row.append(0))
	barcodes_file.close()

	

	indexes = []
	i = 0
	for barcode in barcodes:
		indexes.append(barcode)
		for indexes_count in indexes_counts:
			if dist == 0:
				if barcode[1] == indexes_count[0]:
					indexes[i][2] += indexes_count[1]
					indexes_counts.remove(indexes_count)
			else:
				if distance.hamming(barcode[1], indexes_count[0][0:-2]) <= dist:
					indexes[i][2] += indexes_count[1]
					indexes_counts.remove(indexes_count)
		i += 1
	json_data.close

	right_indexes = 0
	for index in indexes:
		right_indexes += index[2]
	print json_file
	print "all ", all_indexes, "right_barcodes", right_indexes
	indexes = sorted(indexes,  key=lambda index: index[2], reverse=False)
	out_file = json_file + "_right_barcodes_dist1"
	out_file = open(out_file, 'w')
	out_file.write(json.dumps(indexes))
	return 0

files = ['/home/anna/bioinformatics/wheat/indexes/indexes_R1_9', '/home/anna/bioinformatics/wheat/indexes/indexes_R2_9',
'/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_1_indexes', '/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_2_indexes']
barcodes_long = ''
barcodes_short = ''

for json_file in files:
	json_data = open(json_file, 'r')
	indexes_counts = json.load(json_data) 

	all_indexes = 0
	n_indexes = 0
	for indexes_count in indexes_counts:
		all_indexes += indexes_count[1]
		if "N" in indexes_count[0]:
			n_indexes += indexes_count[1]
