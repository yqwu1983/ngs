#!/usr/bin/python
import csv
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
global ONLY_ONE_HIT; ONLY_ONE_HIT = False
import sys
from ntpath import split

def file_from_path(path, folder=False):
    head, tail = split(path)
    if folder: return head
    else: return tail

# handle_file = '/home/anna/bioinformatics/wheat/NBS_LRR_new_assembly_blreport.csv'
handle_file = '/mnt/lustre/nenarokova/wheat/NBS_LRR_new_assembly_blreport.csv'
handle_file = open(handle_file)
handle_csv = csv.reader(handle_file, delimiter=',')

if ONLY_ONE_HIT:
	sorted_csv = sorted( handle_csv, key = lambda x: ( x[0], -int(x[3]), -float(x[2]) ) ) 

	results = []
	cur_seq = None
	for row in sorted_csv:
		if row[0] != cur_seq: 
			cur_seq = row[0]
			results.append(row)
	handle_file.close()
else: 
	results = []
	for row in handle_csv:
		results.append(row)
k=0
fasta_file = sys.argv[1]
result_seqs = []
for seq_record in SeqIO.parse(fasta_file, "fasta"):
	for row in results:
		if seq_record.id == row[1]:
			start = int(row[8])
			end = int(row[9])
			if start > end: start, end = end, start
			seq = seq_record.seq[start:end]
			result_seqs.append(SeqRecord(seq=seq, id=seq_record.id.strip() + row[0].strip() + str(k), description=''))
			results.remove(row)
			k+=1

out_folder = '/home/nenarokova/wheat/new_assembly/nbs_lrr_genes/'
out_file = out_folder + file_from_path(fasta_file) + '_nbs_lrr.fasta'
SeqIO.write(result_seqs, out_file, "fasta")
