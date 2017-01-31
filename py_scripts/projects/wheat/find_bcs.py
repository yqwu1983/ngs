#!/usr/bin/python
from string import find
import csv
from Bio import SeqIO
import json
global CLUSTER; CLUSTER = True

def read_csv(csv_f):
	csv_data = []
	csv_f = open(csv_f, 'rb')
	reader = csv.reader(csv_f)
	for row in reader: 
		csv_data.append(row)
	csv_f.close()
	return csv_data

def find_barcodes(seq, barcodes):
	min_bc_position = len(seq)
	right_barcode = None
	for barcode in barcodes:
		cur_bc_position = find(seq, barcode[1])
		if (cur_bc_position != -1) and (cur_bc_position < min_bc_position):
			min_bc_position = cur_bc_position
			right_barcode = list(barcode)
	if right_barcode:
		right_barcode.append(min_bc_position)
	return right_barcode

if CLUSTER: 
	fastq_file = '/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/not_bcs/not_bcs_1.fastq'
	# fastq_file = '/mnt/lustre/nenarokova/wheat/R1_2/sum_fastq_re/not_bsc/not_bsc_1.fastq'
	barcodes_file = '/mnt/lustre/nenarokova/wheat/right_barcodes.csv'
else: 
	fastq_file = '/home/anna/bioinformatics/wheat/L_H8_1/trim_out/unpaired_out_rv.fastq'
	barcodes_file = '/home/anna/bioinformatics/wheat/barcodes/right_barcodes.csv'

barcodes = read_csv(barcodes_file)
out = {}
for seq_record in SeqIO.parse(fastq_file, "fastq"):
	right_bc = find_barcodes(seq_record.seq, barcodes)
	if right_bc != None:
		out[seq_record.id] = right_bc

out_file = fastq_file[0:-6] + '_bcs'
out_file = open(out_file, 'w')
out_file.write(json.dumps(out))
out_file.close()