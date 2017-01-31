#!/usr/bin/python
import json
import os
import time
from collections import Counter
from collections import OrderedDict
import distance 
import csv
files = ['/home/anna/bioinformatics/wheat/indexes/indexes_R1_9', '/home/anna/bioinformatics/wheat/indexes/indexes_R2_9',
'/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_1_indexes', '/home/anna/bioinformatics/wheat/indexes/L00000210.BC1D3RACXX.5_2_indexes']

for json_file in files:
	json_data = open(json_file, 'r')
	indexes_counts = json.load(json_data) 

	all_indexes = 0
	n_indexes = 0
	for indexes_count in indexes_counts:
		all_indexes += indexes_count[1]
		if "N" in indexes_count[0]:
			n_indexes += indexes_count[1]

	print "all ", all_indexes, "n_barcodes", n_indexes