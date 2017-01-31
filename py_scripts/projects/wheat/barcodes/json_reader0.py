#!/usr/bin/python
import json
import os
from collections import Counter
from collections import OrderedDict
import distance 

# json_file = "/home/anna/bioinformatics/htses/katya/indexes_result"
# json_file = '/home/anna/bioinformatics/wheat/indexes/L_1_indexes_9'
json_file = '/home/anna/bioinformatics/wheat/indexes/indexes_R1_9'
json_data = open(json_file, 'r')

indexes_counts = json.load(json_data) 
indexes = []
for count in indexes_counts:
	not_in_indexes = True
	if len(indexes) > 0:
		for index in indexes:
			if distance.hamming(count[0], index[0]) == 1:
				index[1] += count[1]
				not_in_indexes = False
	if not_in_indexes:
		indexes.append([count[0], count[1]])
json_data.close

indexes = sorted(indexes,  key=lambda index: index[1], reverse=True)
out_file = json_file + "_dist1"
out_file = open(out_file, 'w')
out_file.write(json.dumps(indexes))