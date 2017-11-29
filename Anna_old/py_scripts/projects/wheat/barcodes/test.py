#!/usr/bin/python
from Bio import SeqIO
fastq_file1 = '/home/anna/bioinformatics/htses/katya/0sec_ACAGTG_L001_R1_001.fastq'
fastq_file2 = '/home/anna/bioinformatics/htses/katya/0sec_ACAGTG_L001_R2_001.fastq'
a = 0
for (seq_record1, seq_record2) in zip(SeqIO.parse(fastq_file1, "fastq"), SeqIO.parse(fastq_file2, "fastq")):
	if a < 100:
		print seq_record1, seq_record2
	a+=1