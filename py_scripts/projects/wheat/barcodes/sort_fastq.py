#!/usr/bin/python
import json
import os
import time
import distance 
import csv
from Bio import SeqIO
from ntpath import split
from itertools import izip
from Bio.SeqRecord import SeqRecord
global adapter; adapter = 'AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT'

def file_from_path(path, folder=False):
    head, tail = split(path)
    if folder: return head + '/'
    else: return tail

def cr_outdir(f, workdir=False):
	name = file_from_path(f)[0:-6]
	if workdir: outdir = workdir + name + '/'
	else: outdir = file_from_path(f, folder=True) + name + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

def read_csv(csv_f):
	csv_data = []
	csv_f = open(csv_f, 'rb')
	reader = csv.reader(csv_f)
	for row in reader: 
		csv_data.append(row)
	csv_f.close()
	return csv_data

def dump(sorted_fastq, not_bsc1, not_bsc2, outdir):
	for key in sorted_fastq:
		out_f1 = outdir + key + '_1' + '.fastq'
		with open(out_f1, "a") as handle:
			SeqIO.write(sorted_fastq[key][0], handle, "fastq")

		out_f2 = outdir + key + '_2' + '.fastq'
		with open(out_f2, "a") as handle:
			SeqIO.write(sorted_fastq[key][1], handle, "fastq")

	out_miss_f1 = outdir + 'not_bsc' + '_1' + '.fastq'
	with open(out_miss_f1, "a") as handle:
		SeqIO.write(not_bsc1, handle, "fastq")

	out_miss_f2 = outdir + 'not_bsc' + '_2' + '.fastq'
	with open(out_miss_f2, "a") as handle:
		SeqIO.write(not_bsc2, handle, "fastq")
	return 0

def sort_records(fastq_file1, fastq_file2, right_bcs_file, dist=0, test=False, first_n=0):
	outdir = cr_outdir(fastq_file1)
	right_bcs = read_csv(right_bcs_file)

	chunk_size = 100000
	i = 0

	sorted_fastq = {}
	not_bsc1 = []
	not_bsc2 = []
	for (seq_record1, seq_record2) in izip(SeqIO.parse(fastq_file1, "fastq"), SeqIO.parse(fastq_file2, "fastq")):
		in_bcs = False
		for right_bc in right_bcs:
			bc_len = len(right_bc[1])
			cur_bc = str(seq_record1.seq[first_n : first_n+bc_len])
			if (right_bc[1] == cur_bc):
				in_bcs = True
				if not (right_bc[0] in sorted_fastq):
					sorted_fastq[right_bc[0]] = [[],[]]
				if test: sorted_fastq[right_bc[0]][0].append(seq_record1)]
				else sorted_fastq[right_bc[0]][0].append(seq_record1[(bc_len):len(seq_record1)])
				sorted_fastq[right_bc[0]][1].append(seq_record2)
				break
		if not in_bcs:
			not_bsc1.append(seq_record1)
			not_bsc2.append(seq_record2)

		if i == chunk_size:
			dump(sorted_fastq, not_bsc1, not_bsc2, outdir)

			sorted_fastq = {}
			not_bsc1 = []
			not_bsc2 = []
			i = 0
		else:
			i += 1

	dump(sorted_fastq, not_bsc1, not_bsc2, outdir)
	return 0

def sort_fastq():
	right_bcs_file = '/home/anna/bioinformatics/wheat/indexes/right_barcodes.csv'

	many_files = False
	shift = True

	if not many_files:
		fastq_file1 = '/home/anna/bioinformatics/htses/katya/0sec_ACAGTG_L001_R1_001.fastq'
		fastq_file2 = '/home/anna/bioinformatics/htses/katya/0sec_ACAGTG_L001_R2_001.fastq'

		if not shift:
			sort_records(fastq_file1, fastq_file2, right_bcs_file)

		if shift:
			sort_records(fastq_file1, fastq_file2, right_bcs_file, first_n=1)

	if many_files:
		folder1 = '/home/anna/bioinformatics/htses/katya/1/'
		folder2 = '/home/anna/bioinformatics/htses/katya/2/'
		files1 = os.listdir(folder1) 
		files2 = os.listdir(folder2) 
		fastq_files1 = filter(lambda x: x.endswith('.fastq'), files1) 
		fastq_files2 = filter(lambda x: x.endswith('.fastq'), files2) 

		process_count = 0
		max_processes = 24

		for (f1, f2) in zip(fastq_files1, fastq_files2):
			fastq_file1 = folder1 + f1
			fastq_file2 = folder2 + f2
			pid = os.fork()
			time.sleep(0.1)
			if pid == 0:
				print "Process started"
				sort_records(fastq_file1, fastq_file2, right_bcs_file)
				print "Process ended"
				os._exit(0)

			else:
				process_count += 1
				if process_count >= max_processes:
					os.wait()
					process_count -= 1

		for i in range(process_count):
			os.wait()
	return 0



