#!/usr/bin/python
import os
import time
from subprocess import call
from Bio import SeqIO
from ntpath import split
global THREADS
global CLUSTER; CLUSTER = False
if CLUSTER: THREADS = 24
else: THREADS = 8

def file_from_path(path, folder=False):
    head, tail = split(path)
    if folder: return head
    else: return tail

def cr_outdir(f, workdir=False):
	name = file_from_path(f)[0:-6]
	if workdir: outdir = workdir + name
	else: outdir = file_from_path(f, folder=True) + '/' + name + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

def convert(fastq_file):
	fasta_file = fastq_file[0:-1] + 'a'
	SeqIO.convert(fastq_file, "fastq", fasta_file, "fasta")
	return fasta_file

def makeblastdb(fasta_file, outdir=False):
	if not outdir:
		outdir = cr_outdir(fastq_file)
	db_folder = outdir + 'db_folder/'
	if not os.path.exists(db_folder):
	    os.makedirs(db_folder)
	blast_db = db_folder + file_from_path(fastq_file)[0:-6] + '.db'
	makeblastdb = ['makeblastdb', '-in', fasta_file, '-parse_seqids', '-dbtype', 'nucl', '-out', blast_db]
	call(makeblastdb)
	return blast_db

def blast_fastq(query, f, fasta=False, outdir=False):
	if not outdir:
		outdir = cr_outdir(fastq_file)
	if not fasta: fasta_file = convert(fastq_file)
	blast_db = makeblastdb(fasta_file, outdir)
	name1 = file_from_path(query)[0:-6]
	name2 = file_from_path(fastq_file)[0:-6]
	outfile = outdir + str(name1 + '_' + name2 + '.csv') 
	blastn = ['blastn', '-query', query, '-db', blast_db, '-out', outfile, '-outfmt', '10', '-task', 'blastn-short', '-num_threads', str(THREADS)]
	call(blastn)
	return 0

if not CLUSTER:
	# fastq_file = '/home/anna/bioinformatics/wheat/H7_1.fastq'
	fastq_file = '/home/anna/bioinformatics/htses/ERR015599/not_bsc_1/not_bsc_1.fastq'
	adapters = '/home/anna/bioinformatics/wheat/adapter.fasta'
	# trim_out = '/home/anna/bioinformatics/wheat/H7_1/trim_out/'
else:
	fastq_file = '/mnt/lustre/nenarokova/wheat/R1/sum_fastq/not_bsc/not_bsc_1.fastq'
	# fastq_file = '/mnt/lustre/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1/not_bsc/not_bsc_1.fastq'
	adapters = '/mnt/lustre/nenarokova/wheat/wheat_adapter.fasta'

blast_fastq(adapters, fastq_file)

many_files = False
if many_files:
	files = os.listdir(trim_out)
	files = filter(lambda x: x.endswith('.fastq'), files) 

	process_count = 0

	for f in files:
		fastq_file = trim_out + f
		pid = os.fork()
		time.sleep(0.1)
		if pid == 0:
			print "Process started"
			blast_fastq(adapters, fastq_file)
			print "Process ended"
			os._exit(0)

		else:
			process_count += 1
			if process_count >= THREADS:
				os.wait()
				process_count -= 1

	for i in range(process_count):
		os.wait()