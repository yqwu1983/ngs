#!/usr/bin/python
import json
import os
from collections import Counter
from collections import OrderedDict
folder = '/home/nenarokova/wheat/R1/'
files = os.listdir(folder) 
indexes_count_files = filter(lambda x: x.endswith('_indexes'), files) 
indexes_counts = Counter({})
for f in indexes_count_files:
	json_file = folder + f
	json_data=open(json_file, 'r')
	indexes_counts = indexes_counts + Counter(json.load(json_data))
	json_data.close

out_file = folder + "indexes_result"
out_file = open(out_file, 'w')
out_file.write(str(indexes_counts))
