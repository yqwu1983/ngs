#!/usr/bin/python
# -*- coding: cp1251 -*-

import re
import csv
global CSV_FILE; CSV_FILE = '/home/anna/bioinformatics/wheat/result_my_fav.csv'
import itertools

aegilops = ["A.bicornis", "A.caudata", "A.longissima", "A.mutica", "A.sharonensis", "A.speltoides", "A.tauschii", "A.umbellulata", "A.uniaristata", "A.variabilis"]
triticum = ["T.aestivum", "T.aethiopicum", "T.araraticum", "T.boeoticum", "T.compactum", "T.dicoccoides", "T.dicoccum", "T.durum", "T.ispahanicum", "T.jakubzineri", "T.karamyshevii", "T.macha", "T.monococcum", "T.persicum", "T.polonicum", "T.sinskajae", "T.spelta", "T.sphaerococcum", "T.timopheevii", "T.turanicum", "T.turgidum", "T.urartu", "T.vavilovii"]

def read_csv_file(csv_file):
	csv_data = []
	with open(csv_file, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			csv_data.append(row)
		csvfile.close()
	return csv_data

def normalize_snp(snp):
	return map(lambda x: x.upper(), snp.replace(' ', '').split(','))

def extract_columns(indexes, csv_data = None):
	csv_data = csv_data or read_csv_file(CSV_FILE)

	result = []

	for index, row in enumerate(csv_data):
		if row[0][:8] == 'Scaffold' or row[0] in ['Index', 'Species', 'Genome', 'Ploidy', 'Wild/Cultivated']:
			cols = []
			for ind in range(0, len(row)):
				if ind in indexes:
					cols.append(row[ind])
			result.append(cols)

	transposed = [list(x) for x in zip(*result)] # transpose

	samples = []
	for sample in transposed:
		snps = {}
		for index, cell in enumerate(sample[5:]):
			if cell != '-':
				snps[index] = normalize_snp(cell)

		features = {}
		features['index'] = sample[0]
		features['species'] = sample[1]
		features['genome'] = sample[2]
		features['ploidy'] = sample[3]
		features['type'] = sample[4]
		features['snp_data'] = sample[5:]
		features['snps'] = snps
		features['snps_count_by_ploidy'] = len(features['snps'])/float(features['ploidy'])
		samples.append(features)
	return samples

def extract_column_ids(rules, csv_data = None):
	csv_data = csv_data or read_csv_file(CSV_FILE)
	column_ids = [x for x in range(2, len(csv_data[0]))] # all columns by default

	# Gathering column indexes
	for index, row in enumerate(csv_data):
		if index in rules:
			ids = []
			for column_id, cell in enumerate(row):
				if cell in rules[index]:
					ids.append(column_id)
			column_ids = list(set(column_ids).intersection(ids))

	exclusion_column_ids = list(set([x for x in range(2, len(csv_data[0]))]) - set(column_ids))

	return { 'inclustion_ids': column_ids, 'exclusion_ids': exclusion_column_ids }

def get_unique_snps(heap):
	snps = {}
	for sample in heap:
		for k, v in sample['snps'].iteritems():
			if k in snps:
				snps[k] += v
			else:
				snps[k] = v
	return snps

def count_unique(first_heap, second_heap):
	first_snps = get_unique_snps(first_heap)
	second_snps = get_unique_snps(second_heap)

	snps = first_snps.values()
	snps = sum(snps, [])
	first_snps_count = len(snps)

	snps = second_snps.values()
	snps = sum(snps, [])
	second_snps_count = len(snps)

	non_unique_count = 0

	non_unique = {}

	first_unique_count = 0
	for pos, snps in first_snps.iteritems():
		if pos in second_snps:
			snps_set = set(snps)
			second_snps_set = set(second_snps[pos])

			common = snps_set.intersection(second_snps_set)
			non_unique_count += len(common)
			first_unique_count += (len(snps_set) - len(common))
			if len(snps_set - common) > 0:
				non_unique[pos] = list(snps_set - common)
		else:
			first_unique_count += len(set(snps))
			non_unique[pos] = snps

	second_unique_count = 0
	for pos, snps in second_snps.iteritems():
		if pos in first_snps:
			snps_set = set(snps)
			first_snps_set = set(first_snps[pos])

			common = snps_set.intersection(first_snps_set)
			second_unique_count += len(snps_set) - len(common)
		else:
			second_unique_count += len(set(snps))

	return {
		'first_unique': first_unique_count,
		'second_unique': second_unique_count,
		'non_unique': non_unique_count,
		'first_snps_count': first_snps_count,
		'second_snps_count': second_snps_count
	}

## append data to results, LOL X_x
def append_snp_data(results_arr, inc_samples, exc_samples, col_name):
	inc_samples_count = len(inc_samples)
	exc_samples_count = len(exc_samples)

	av_inclusion = sum(map(lambda x: x['snps_count_by_ploidy'], inc_samples))/float(inc_samples_count)
	av_exclusion = sum(map(lambda x: x['snps_count_by_ploidy'], exc_samples))/float(exc_samples_count)

	av_inc_ploidy = sum(map(lambda x: int(x['ploidy']), inc_samples))/float(inc_samples_count)
	av_exc_ploidy = sum(map(lambda x: int(x['ploidy']), exc_samples))/float(exc_samples_count)

	unique_snps_count = count_unique(inc_samples, exc_samples)
	av_unique_snps_inc = unique_snps_count['first_unique']/float(inc_samples_count)/float(av_inc_ploidy)
	av_unique_snps_exc = unique_snps_count['second_unique']/float(exc_samples_count)/float(av_exc_ploidy)

	values = [col_name, # Species
		inc_samples_count, # Number of samples for the species
		exc_samples_count, # Number of samples for the other species
		av_inclusion, # Average SNPs count for the species per sample per subgenome
		av_exclusion, # Average SNPs count for the other species per sample per subgenome
		unique_snps_count['non_unique'], # Common SNPs count for the species and for the other species
		unique_snps_count['first_unique'], # Unique SNPs count for the species
		unique_snps_count['second_unique'], # Unique SNPs count for the other species
		av_unique_snps_inc, # Average unique SNPs count for the species per sample per subgenome
		av_unique_snps_exc, # Average unique SNPs count for the other species per sample per subgenome
		av_inc_ploidy, # Average ploidy for the species
		av_exc_ploidy, # Average ploidy for the other species
		unique_snps_count['first_snps_count'],
		unique_snps_count['second_snps_count']
	]

	for index, value in enumerate(values):
		results[index].append(value)

	return 0

data = read_csv_file(CSV_FILE)

results = [
	['Species'],
	['Number of samples for the species'],
	['Number of samples for the other species'],
	['Average SNPs count for the species per sample per subgenome'],
	['Average SNPs count for the other species per sample per subgenome'],
	['Common SNPs count for the species and for the other species'],
	['Unique SNPs count for the species'],
	['Unique SNPs count for the other species'],
	['Average unique SNPs count for the species per sample per subgenome'],
	['Average unique SNPs count for the other species per sample per subgenome'],
	['Average ploidy for the species'],
	['Average ploidy for the other species'],
	['Count of snps'],
	['Count of other snps']
]

aegilops_ids = extract_column_ids({ 1: aegilops }, data)
aegilops_inc = extract_columns(aegilops_ids['inclustion_ids'], data)
aegilops_exc = extract_columns(aegilops_ids['exclusion_ids'], data)
append_snp_data(results, aegilops_inc, aegilops_exc, 'All Aegilops')

all_ids = extract_column_ids({ 4: ['wild'] }, data)
all_inc = extract_columns(all_ids['inclustion_ids'], data)
all_exc = extract_columns(all_ids['exclusion_ids'], data)
append_snp_data(results, all_inc, all_exc, 'All wild')

wild_triticum_ids = extract_column_ids({ 1: triticum, 4: ['wild'] }, data)
cultivated_triticum_ids = extract_column_ids({ 1: triticum, 4: ['cultivated'] }, data)
wild_triticum = extract_columns(wild_triticum_ids['inclustion_ids'], data)
cultivated_triticum = extract_columns(cultivated_triticum_ids['inclustion_ids'], data)
append_snp_data(results, wild_triticum, cultivated_triticum, 'Triticum wild/cultivated')

for species in (aegilops + triticum):
	species_ids = extract_column_ids({ 1: [species] }, data)
	species_inc = extract_columns(species_ids['inclustion_ids'], data)
	species_exc = extract_columns(species_ids['exclusion_ids'], data)
	append_snp_data(results, species_inc, species_exc, species)


## Calculating number of all snps
results.append([''])

all_ids = extract_column_ids({ 1: aegilops + triticum }, data)
all_columns = extract_columns(all_ids['inclustion_ids'], data)
snps = map(lambda x: x.values(), map(lambda x: x['snps'], all_columns))
snps = sum(sum(snps, []), []) # flatten
unique_snps = list(set(snps))

results.append(['Snps count', len(snps)])
results.append(['Snps types count', len(unique_snps), ', '.join(unique_snps)])

all_snps_by_pos = get_unique_snps(all_columns)
unique_snps_by_pos_count = 0 # сумма уникальных snps в позицях: [a, a, t, g] => 2
non_unique_snps_by_pos_count = 0 # сумма неуникальныйх snps в позициях: [a, a, t, g] => 1
all_snps_by_pos_count = 0 # сумма всех snps в позициях: [a, a, t, g] => 3

for position, snps in all_snps_by_pos.iteritems():
	unique = filter(lambda x: snps.count(x) == 1, snps)
	unique_snps_by_pos_count += len(unique)
	non_unique = list(set(filter(lambda x: snps.count(x) > 1, snps)))
	non_unique_snps_by_pos_count += len(non_unique)
	all_snps_by_pos_count += len(set(snps))

results.append(['Unique snps count by positions', unique_snps_by_pos_count])
results.append(['Non unique snps count by positions', non_unique_snps_by_pos_count])
results.append(['All snps count by positions', all_snps_by_pos_count])


## writing to file

outfilename = 'snps_stat_by_species.csv'
with open(outfilename , 'w') as outfile:
	dict_writer = csv.writer(outfile, delimiter=',')
	dict_writer.writerows(results)
