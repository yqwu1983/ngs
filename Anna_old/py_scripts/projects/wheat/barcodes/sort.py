#!/usr/bin/python
import json
import os
from collections import Counter
from collections import OrderedDict
import distance 

json_file = '/home/anna/bioinformatics/wheat/indexes/indexes_R1_9_3'
json_data = open(json_file, 'r')
indexes_counts = json.load(json_data) 
json_data.close
