#!/usr/bin/python
import csv
import sys

all_features = {
	'qseqid': {'description': 'Query Seq-id', 'type': 'str'},
	'qgi': {'description': 'Query GI', 'type': 'str'},
	'qacc': {'description': 'Query accesion', 'type': 'str'},
	'qaccver': {'description': 'Query accession.version', 'type': 'str'},
	'qlen': {'description': 'Query sequence length', 'type': 'int'},
	'sseqid': {'description': 'Subject Seq-id', 'type': 'str'},
	'sallseqid': {'description': 'All subject Seq-id(s)', 'type': 'str'},
	'sgi': {'description': 'Subject GI', 'type': 'str'},
	'sallgi': {'description': 'All subject GIs', 'type': 'str'},
	'sacc': {'description': 'Subject accession', 'type': 'str'},
	'saccver': {'description': 'Subject accession.version', 'type': 'str'},
	'sallacc': {'description': 'All subject accessions', 'type': 'str'},
	'slen': {'description': 'Subject sequence length', 'type': 'int'},
	'qstart': {'description': 'Start of alignment in query', 'type': 'int'},
	'qend': {'description': 'End of alignment in query', 'type': 'int'},
	'sstart': {'description': 'Start of alignment in subject', 'type': 'int'},
	'send': {'description': 'End of alignment in subject', 'type': 'int'},
	'qseq': {'description': 'Aligned part of query sequence', 'type': 'str'},
	'sseq': {'description': 'Aligned part of subject sequence', 'type': 'str'},
	'evalue': {'description': 'Expect value', 'type': 'float'},
	'bitscore': {'description': 'Bit score', 'type': 'float'},
	'score': {'description': 'Raw score', 'type': 'float'},
	'length': {'description': 'Alignment length', 'type': 'int'},
	'pident': {'description': 'Percentage of identical matches', 'type': 'float'},
	'nident': {'description': 'Number of identical matches', 'type': 'int'},
	'mismatch': {'description': 'Number of mismatches', 'type': 'int'},
	'positive': {'description': 'Number of positive-scoring matches', 'type': 'int'},
	'gapopen': {'description': 'Number of gap openings', 'type': 'int'},
	'gaps': {'description': 'Total number of gaps', 'type': 'int'},
	'ppos': {'description': 'Percentage of positive-scoring matches', 'type': 'float'},
	'frames': {'description': 'Query and subject frames', 'type': 'str'},
	'qframe': {'description': 'Query frame', 'type': 'str'},
	'sframe': {'description': 'Subject frame', 'type': 'str'},
	'btop': {'description': 'Blast traceback operations (BTOP)', 'type': 'str'},
	'staxids': {'description': 'Subject Taxonomy ID(s)', 'type': 'str'},
	'sscinames': {'description': 'Subject Scientific Name(s)', 'type': 'str'},
	'scomnames': {'description': 'Subject Common Name(s)', 'type': 'str'},
	'sblastnames': {'description': 'Subject Blast Name(s)', 'type': 'str'},
	'sskingdoms': {'description': 'Subject Super Kingdom(s)', 'type': 'str'},
	'stitle': {'description': 'Subject Title', 'type': 'str'},
	'salltitles': {'description': 'All Subject Title(s)', 'type': 'str'},
	'sstrand': {'description': 'Subject Strand', 'type': 'str'},
	'qcovs': {'description': 'Query Coverage Per Subject', 'type': 'float'},
	'qcovhsp': {'description': 'Query Coverage Per HSP', 'type': 'float'},
	}

class BlastParser(object):
	def __init__(self, blreport_path, features=False, has_header=False, delimiter=','):
		self.blreport_path = blreport_path
		self.features = features
		self.has_header = has_header
		self.delimiter = delimiter
		if type(self.features) == str: self.features = filter(None, self.features.split(' '))
		default_features = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
		if not self.features and not self.has_header: self.features = default_features
		return None

	def read_hits(self):
		handle_file = open(self.blreport_path)
		handle_csv = csv.reader(handle_file, delimiter=self.delimiter)
		first = True
		hits = []
		for row in handle_csv:
			if first and self.has_header:
				self.features = row
			elif first and (row[0] in self.features): pass
			else:
				hit = {}
				i = 0
				for feature in self.features:
					if all_features[feature]['type'] == 'float':
						hit[feature] = float(row[i])
					elif all_features[feature]['type'] == 'int':
						hit[feature] = int(row[i])
					else:
						hit[feature] = row[i]
					i+=1
			hits.append(hit)
		return hits

