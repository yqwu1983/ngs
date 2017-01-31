import os
from ntpath import split
from subprocess32 import call
from string import maketrans
from Bio import SeqIO
import csv
import time

global ONLY_FIND; ONLY_FIND = True
global MAX_MISMATCH
# MAX_MISMATCH = 0
# global REPEAT; REPEAT = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
global REP; REP = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
global MAX_PROCESSES; MAX_PROCESSES = 8

def file_from_path(path):
    head, tail = split(path)
    return tail

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

def flash_merge(file_fw, file_rv, outdir, flash_dir = False):
	if not flash_dir: flash_dir = '/home/anna/bioinformatics/bioprograms/FLASH/'
	flash_output = outdir + 'flash_out/'
	if not os.path.exists(flash_output):
	    os.makedirs(flash_output)

	options_flash = ['-d', flash_output, '-O', '-M 250', '-x 0.25']
	flash = flash_dir + './flash'
	flash_merge = [flash] + options_flash + [file_fw, file_rv]
	call(flash_merge)
	return flash_output

def use_fuzznuc (reads, pattern, outdir, max_mismatch, indels = False, name = ''):
	fuzznuc_file = outdir + 'fuzznuc_report' + name
	fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern, '-outfile', fuzznuc_file]
	fuzznuc_options = ['-pmismatch', str(MAX_MISMATCH), '-complement', '-snucleotide1', '-squick1', 
					   '-rformat2', 'excel']
	fuzznuc = fuzznuc + fuzznuc_options
	call(fuzznuc)
	return fuzznuc_file

def find_spacers_fuzznuc(reads, outdir, name = ''):
	fuzznuc_file = use_fuzznuc(reads, REPEAT, outdir, MAX_MISMATCH, name = name)
	fuzznuc_file = open(fuzznuc_file)
	fuzznuc_csv = csv.reader(fuzznuc_file, delimiter='\t')
	repeat_matches = []
	i = 0
	for row in fuzznuc_csv:
		if row[0] != 'SeqName':
			repeat_matches.append({ 'SeqName': row[0], 'Start': row[1], 'End': row[2], 'Strand': row[4], 'Mismatch': row[6] })
			i+=1
	repeats_number = i
	spacers = []
	k = 0
	i = 0
	spacers_number = 0
	statistics_file = outdir + 'statistics_file.txt'
	with open(statistics_file, 'a') as statistics_file:
	   statistics_file.write(str(repeats_number) + ' '+ str(MAX_MISMATCH) + ' ' + REPEAT + '\n')
	statistics_file.closed
	# for seq_record in SeqIO.parse(reads, "fastq"):
	# 	spacers.append([])
	# 	first_repeat = True
	# 	l_matches = len(repeat_matches)
	# 	while (i < l_matches) and (repeat_matches[i]['SeqName'] == seq_record.id):
	# 		if first_repeat:
	# 			spacer_start = int(repeat_matches[i]['End'])
	# 			first_repeat = False
	# 			i+=1
	# 		else:
	# 			spacer_end = int(repeat_matches[i]['Start'])-2
	# 			if repeat_matches[i]['Strand'] == '+':
	# 				spacer = seq_record.seq[spacer_start:spacer_end]
	# 			elif repeat_matches[i]['Strand'] == '-':
	# 				spacer = seq_record.seq.reverse_complement()[spacer_start:spacer_end]
	# 			else: print("Error in find_spacers_fuzznuc")
	# 			if len(spacer) in range (29, 31): 
	# 				spacers[k].append(spacer)
	# 				spacers_number +=1
	# 			spacer_start = int(repeat_matches[i]['End'])
	# 			i+=1
	# 	k+=1

	# print 'MAX_MISMATCH', MAX_MISMATCH,
	# print repeats_number,
	# print 'spacers', spacers_number
	return spacers

def handle_HTS (file_fw, file_rv, outdir, name = ''):

	if ONLY_FIND == True: 
		flash_output = outdir + 'flash_out/'
	else: 
		flash_output = flash_merge(file_fw, file_rv, outdir)

	combined_reads = flash_output + 'out.extendedFrags.fastq'
	find_spacers_fuzznuc(combined_reads, outdir, name = name)
	return 0

def handle_files (workdir, file_fw = False, file_rv = False, HTS_dir = False, HTSes = False, multiproc = False, name = ''):
	if file_fw and file_rv:
		name_reads = file_from_path(file_fw)[0:-6]
		outdir = workdir + name_reads + '/'
		handle_HTS (file_fw, file_rv, outdir, name = name)

	elif HTS_dir and HTSes:
		process_count = 0
		for fw, rv in HTSes:
			file_fw = HTS_dir + fw
			file_rv = HTS_dir + rv
			name_fw = file_from_path(file_fw)
			name_rv = file_from_path(file_rv)
			name_reads = name_fw[0:-6]
			outdir = workdir + name_reads + '/'
			if not os.path.exists(outdir): os.makedirs(outdir)
			if not multiproc:
				if not ONLY_FIND: handle_HTS (file_fw, file_rv, outdir)
				else: handle_HTS (file_fw, file_rv, outdir)
			else:
				pid = os.fork()
				time.sleep(0.1)
				if pid == 0:
					if not ONLY_FIND: handle_HTS (file_fw, file_rv, outdir)
					else: handle_HTS (file_fw, file_rv, outdir)
					os.abort()
				else:
					process_count += 1
					if process_count >= MAX_PROCESSES:
						os.wait()
						process_count -= 1
			
	else: print "Error: handle_HTSes haven't get needed values"
	return 0

workdir = '/home/anna/bioinformatics/HTS/outdirs/'

file_fw = '/home/anna/bioinformatics/HTS/HTSes/CTG_CCGTCC_L001_1.fastq'
file_rv = '/home/anna/bioinformatics/HTS/HTSes/CTG_CCGTCC_L001_2.fastq'

# process_count = 0
# global statistics; statistics = []
# for rep_start in range(0, len(REP)):
# 	global REPEAT 
# 	REPEAT = REP [rep_start: -1]	
# 	for MAX_MISMATCH in range(0, 5):
# 		pid = os.fork()
# 		time.sleep(0.1)
# 		if pid == 0:
# 			handle_files(workdir, file_fw, file_rv, name = REPEAT + str(MAX_MISMATCH))
# 			os.abort()
# 		else:
# 			process_count += 1
# 			if process_count >= MAX_PROCESSES:
# 				os.wait()
# 				process_count -= 1

for MAX_MISMATCH in range(0, 13):
	pid = os.fork()
	time.sleep(0.1)
	if pid == 0:
		handle_files(workdir, file_fw, file_rv, name = REPEAT + str(MAX_MISMATCH))
		os.abort()
	else:
		process_count += 1
		if process_count >= MAX_PROCESSES:
			os.wait()
			process_count -= 1

# HTS_dir = '/home/anna/bioinformatics/HTS/HTSes/'
# HTSes = [('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
# ('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]
# handle_files(workdir, HTS_dir = HTS_dir, HTSes = HTSes, multiproc = True)