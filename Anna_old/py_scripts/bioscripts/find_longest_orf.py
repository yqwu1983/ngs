#!/usr/bin/python
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from helpers.make_outdir import file_from_path, make_outdir, new_file
from helpers.lookahead import lookahead

def find_longest_orf(orfs_path, f_out):
	out = []
	i = 0
	is_first = True
	for record, is_last in lookahead(SeqIO.parse(orfs_path, "fasta")):
		i+=1
		trancript_id = record.id.split('_')[2]
		cur_len = len(record.seq)
		if is_first:
			cur_id = trancript_id
			max_len = cur_len
			max_orf = record
			is_first = False
		elif is_last:
			out.append(max_orf)
		else:
			if trancript_id == cur_id:
				if cur_len > max_len:
					max_len = cur_len
					max_orf = record
			else:
				out.append(max_orf)
				cur_id = trancript_id
				max_orf = record
				max_len = cur_len
	return out
