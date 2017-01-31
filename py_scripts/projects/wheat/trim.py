#!/usr/bin/python
import os
import time
from subprocess import call
from ntpath import split
global CLUSTER; CLUSTER = True
if CLUSTER: 
	THREADS = 24
	global R1_2; R1_2 = False
else: 
	THREADS = 8
global MANY_FILES; MANY_FILES = False
global FASTQC; FASTQC = True

def file_from_path(path, folder=False):
    head, tail = split(path)
    if folder: return head
    else: return tail

def cr_outdir(f, workdir=False):
	name = file_from_path(f)[0:-6]
	if workdir: outdir = workdir + name + '/'
	else: outdir = file_from_path(f, folder=True) + '/' + name + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

def trim(file_fw, file_rv, outdir=False, trimc_dir=None):
	if not trimc_dir: 
		if CLUSTER: trimc_dir = '/home/nenarokova/Trimmomatic-0.33/'
		else: trimc_dir = '/home/anna/bioinformatics/bioprograms/Trimmomatic-0.33/'
	if not outdir:
		outdir = cr_outdir(file_fw)
	trim_out = outdir + 'trim_out/'
	if not os.path.exists(trim_out):
	    os.makedirs(trim_out)

	paired_out_fw = trim_out + 'paired_out_fw' + '.fastq'
	unpaired_out_fw = trim_out + 'unpaired_out_fw' + '.fastq'
	paired_out_rv = trim_out + 'paired_out_rv' + '.fastq'
	unpaired_out_rv = trim_out + 'unpaired_out_rv' + '.fastq'

	if R1_2: adapters_file = trimc_dir + 'adapters/TruSeq2-PE.fa'
	else: adapters_file = trimc_dir + 'adapters/all_trim.fa'


	trimmomatic = ['java', '-jar', trimc_dir + 'trimmomatic-0.33.jar']
	trim_options = ['PE', '-phred33', file_fw, file_rv, 
					paired_out_fw, unpaired_out_fw, paired_out_rv, unpaired_out_rv,
					'ILLUMINACLIP:'+ adapters_file + ':2:30:10', 'LEADING:3', 'TRAILING:3', 'SLIDINGWINDOW:4:20',
					'MINLEN:30' ] 
	trim = trimmomatic + trim_options
	print ' '.join(trim)
	call(trim)

	if FASTQC:
		if CLUSTER:  fastqc_dir = '/home/nenarokova/FastQC/'
		else: fastqc_dir = '/home/anna/bioinformatics/bioprograms/FastQC/'
		fastqc = fastqc_dir + './fastqc'
		call([fastqc, fastq_file1])
		call([fastqc, fastq_file2])
		files = os.listdir(trim_out)
		files = filter(lambda x: x.endswith('.fastq'), files) 
		for f in files:
			fastq_file = trim_out + '/' + f
			call([fastqc, fastq_file])

	return trim_out

if MANY_FILES:
	if CLUSTER: 
		if R1_2: folder = '/home/nenarokova/wheat/R1_2/R1/sum_fastq/fastq/not_trimmed/'
		else: folder = '/home/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1/'
	else:
		folder = '/home/anna/bioinformatics/htses/katya/'	
	files = os.listdir(folder) 

	fastq_files1 = filter(lambda x: x.endswith('1.fastq'), files) 
	fastq_files2 = filter(lambda x: x.endswith('2.fastq'), files) 

	process_count = 0

	for (f1, f2) in zip(fastq_files1, fastq_files2):
		fastq_file1 = folder + f1
		fastq_file2 = folder + f2

		pid = os.fork()
		time.sleep(0.1)
		if pid == 0:
			trim(fastq_file1, fastq_file2)
			os._exit(0)

		else:
			process_count += 1
			if process_count >= THREADS:
				os.wait()
				process_count -= 1

	for i in range(process_count):
		os.wait()

else:
	fastq_file1 = '/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/G4/G4_1.fastq'
	fastq_file2 = '/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/G4/G4_2.fastq'
	trim(fastq_file1, fastq_file2)
	