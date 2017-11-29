#!/usr/bin/python
import re
from ntpath import split
import csv
import glob
from natsort import natsorted

def get_positions(filename):
	f = open(filename, 'r')
	result = {}
	for line in f.readlines():
		if line[0] != '#':
			s_line = line.split('\t')
			position = ' '.join(s_line[0:2])
			ref = s_line[3]
			alt = s_line[4]
			result[position] = { 'alt': alt, 'ref': ref }
	f.close()
	return result

def get_index(filename, dataset):
	number = re.match('.*new_assembly_nbs_lrr_ids_(.*)_filtered.*', filename).group(1)
	return '_'.join([dataset, number])

path = "/home/anna/bioinformatics/wheat/snps/"

data = {}

for dataset in ['L', 'R']:
	local_path = path + dataset + '/'
	files = glob.glob(local_path + '*')
	for filename in files:
		data[get_index(filename, dataset)] = get_positions(filename)

all_positions = {}

for file_index, file_hash in data.iteritems():
	for position, snp in file_hash.iteritems():
		all_positions[position] = snp['ref']

result = {}

for file_index, file_hash in data.iteritems():
	result[file_index] = {}
	for position, ref in all_positions.iteritems():
		if position in file_hash:
			result[file_index][position] = file_hash[position]['alt']
		else:
			result[file_index][position] = '-'

result['ref'] = {}
for position, ref in all_positions.iteritems():
	result['ref'][position] = ref


## OUTPUT ##

outfilename = '/home/anna/bioinformatics/wheat.result.csv'
with open(outfilename , 'w') as outfile:
	keys = natsorted(result.keys())
	keys.remove('ref')
	dict_writer = csv.DictWriter(outfile, ['pos'] + keys + ['ref'])
	dict_writer.writeheader()

	for position, ref in all_positions.iteritems():
		row = {}
		for file_index, file_hash in result.iteritems():
			row[file_index] = file_hash[position]
		row['pos'] = position
		dict_writer.writerow(row)

	# dict_writer.writerows(result)