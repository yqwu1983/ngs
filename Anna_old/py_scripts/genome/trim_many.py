#!/usr/bin/python
import os
import time
from subprocess import call
from ntpath import split
global THREADS; THREADS = 8
global CLUSTER; CLUSTER = False
global MANY_FILES; MANY_FILES = False

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
		print outdir
	trim_out = outdir + 'trim_out/'
	if not os.path.exists(trim_out):
	    os.makedirs(trim_out)

	trimlog = trim_out +'trimlog'
	paired_out_fw = trim_out + 'paired_out_fw' + '.fastq'
	unpaired_out_fw = trim_out + 'unpaired_out_fw' + '.fastq'
	paired_out_rv = trim_out + 'paired_out_rv' + '.fastq'
	unpaired_out_rv = trim_out + 'unpaired_out_rv' + '.fastq'

	adapters_file = trimc_dir + 'adapters/adapters.fa'

	trimmomatic = ['java', '-jar', trimc_dir + 'trimmomatic-0.33.jar']
	trim_options = ['PE', '-phred33', '-threads', str(THREADS), '-trimlog', trimlog, file_fw, file_rv, 
					paired_out_fw, unpaired_out_fw, paired_out_rv, unpaired_out_rv,
					'ILLUMINACLIP:'+ adapters_file + ':2:20:10', 'LEADING:3', 'TRAILING:3', 'SLIDINGWINDOW:4:30',
					'MINLEN:30' ] 
	trim = trimmomatic + trim_options
	print ' '.join(trim)
	call(trim)
	return trim_out

if MANY_FILES:
	if CLUSTER: folder = '/home/nenarokova/wheat/R1/sum_fastq1/'
	else: folder = '/home/anna/bioinformatics/htses/ERR015599_1/'

	files = os.listdir(folder) 
	fastq_files1 = filter(lambda x: x.endswith('1.fastq'), files) 
	fastq_files2 = filter(lambda x: x.endswith('2.fastq'), files) 

	process_count = 0
	max_processes = 24

	for (f1, f2) in zip(fastq_files1, fastq_files2):
		fastq_file1 = folder + f1
		fastq_file2 = folder + f2

		pid = os.fork()
		time.sleep(0.1)
		if pid == 0:
			print "Process started"
			trim (fastq_file1, fastq_file2)
			print "Process ended"
			os._exit(0)

		else:
			process_count += 1
			if process_count >= max_processes:
				os.wait()
				process_count -= 1

	for i in range(process_count):
		os.wait()

else:
	fastq_file1 = '/home/anna/bioinformatics/wheat/A10_1.fastq'
	fastq_file2 = '/home/anna/bioinformatics/wheat/A10_2.fastq'
	trim (fastq_file1, fastq_file2)