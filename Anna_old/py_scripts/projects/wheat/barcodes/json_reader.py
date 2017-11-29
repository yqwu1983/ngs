#!/usr/bin/python
import json
import os
from collections import Counter
from collections import OrderedDict

json_file = '/home/anna/bioinformatics/wheat/indexes_result_R2_2'
json_data = open(json_file, 'r')
indexes_counts = json.load(json_data)
print type(indexes_counts)
json_data.close

# out_file = folder + "indexes_result"
# out_file = open(out_file, 'w')
# out_file.write(str(indexes_counts))
