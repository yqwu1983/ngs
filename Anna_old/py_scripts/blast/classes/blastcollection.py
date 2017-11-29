#!/usr/bin/python
from BCBio import GFF
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from helpers.make_outdir import file_from_path, make_outdir, new_file
from helpers.lookahead import lookahead
from helpers.parse_csv import parse_csv

class BlastHitsCollection(object):
	def __init__(self, hits=False, blreport_path=False, features_string=False, features=False, header=False):
		pass

	def add_len_ratio(self):
		hits_with_ratio = BlastParser(hits=self.hits, features=self.features)
		allen_index = hits_with_ratio.features.index('length')
		hits_with_ratio.features.insert(allen_index+1, 'allen/qlen')
		for hit in hits_with_ratio.hits:
			hit['allen/qlen'] = float(hit['length']/float(hit['qlen']))
		return hits_with_ratio

	def change_hits_ids(self, ids_csv_path, ids_csv_delimiter=','):
		ids_csv = parse_csv(ids_csv_path, delimiter=ids_csv_delimiter)
		ids_substitutes = {}
		for row in ids_csv: ids_substitute[row[0]] = row[1]
		new_ids_hits = BlastParser(hits=self.hits, features=self.features)
		for hit in new_ids_hits.hits:
			hit['qseqid'] = ids_substitutes[hit['qseqid']]
		return new_ids_hits

	def write_blast_csv(self, outfile_path, hits=False, header=False):
		if not hits: hits = self.hits
		with open(outfile_path, 'wb') as outfile:
			csv_writer = csv.writer(outfile, delimiter=self.delimiter)
			if header:
				csv_writer.writerow(self.features)
			for hit in hits:
				row = []
				for feature in self.features:
					row.append(hit[feature])
				csv_writer.writerow(row)
			outfile.close()
		return outfile_path

	def add_functions(self, q_path,  q_delimiter, s_path, s_delimiter, hits=False):
		q_info = parse_csv(q_path, delimiter=q_delimiter)
		s_info = parse_csv(s_path, delimiter=s_delimiter)
		if not hits: hits = self.hits
		for hit in hits:
			for row in q_info:
				if hit['qseqid'] == row[0]:
					hit['q_function'] = row[1]
			for row in s_info:
				if hit['sseqid'] == row[0]:
					hit['s_function'] = row[1]
					hit['s_GO_terms'] = row[2]

		qseqid_index = self.features.index('qseqid')
		self.features.insert(qseqid_index+1, 'q_function')
		sseqid_index = self.features.index('sseqid')
		self.features.insert(sseqid_index+1, 's_GO_terms')
		self.features.insert(sseqid_index+1, 's_function')

		outfile_path = new_file(self.blreport_path, new_end='_with_functions.csv')
		self.write_blast_csv(outfile_path=outfile_path, hits=hits, header=True)
		return hits

