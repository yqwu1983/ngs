import os
import csv
import time
from ntpath import split
from subprocess32 import call
from string import maketrans
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

global ONLY_FIND; ONLY_FIND = True
global ONLY_SPACERS; ONLY_SPACERS = False
global MAX_PROCESSES; MAX_PROCESSES = 8
global REPEAT; REPEAT = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
global USE_BOWTIE2; USE_BOWTIE2 = False

def file_from_path(path):
    head, tail = split(path)
    return tail

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

def flash_merge(file_fw, file_rv, outdir, flash_dir = False):
	if not flash_dir: flash_dir = '/home/anna/bioinformatics/bioprograms/FLASH/'
	flash_out = outdir + 'flash_out/'
	if not os.path.exists(flash_out):
	    os.makedirs(flash_out)

	options_flash = ['-d', flash_out, '-O', '-M 250', '-x 0.25']
	flash = flash_dir + './flash'
	flash_merge = [flash] + options_flash + [file_fw, file_rv]
	call(flash_merge)
	return flash_out

def use_fuzznuc (reads, pattern, outdir, max_mismatch = 0, indels = False, name = ''):
	fuzznuc_file = outdir + 'fuzznuc_report' + name
	fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern, '-outfile', fuzznuc_file]
	fuzznuc_options = ['-pmismatch', str(max_mismatch), '-complement', '-snucleotide1', '-squick1', 
					   '-rformat2', 'excel']
	fuzznuc = fuzznuc + fuzznuc_options
	call(fuzznuc)
	return fuzznuc_file

def crisrpr_start(reads, outdir):
	if not ONLY_SPACERS: fuzznuc_file = use_fuzznuc(reads, REPEAT, outdir)
	else: fuzznuc_file = outdir + 'fuzznuc_report'

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
	spacers_fasta = outdir + 'spacers0.fasta'

	sp_fasta_out = []
	
	for seq_record in SeqIO.parse(reads, "fastq"):
		if (repeat_matches[i]['SeqName'] == seq_record.id):
			cr_start = int(repeat_matches[i]['Start'])

			if repeat_matches[i]['Strand'] == '+':
				seq = SeqRecord(seq_record.seq[spacer_start:spacer_end], id = repeat_matches[i]['SeqName']+' '+str(cur_sp_n), description = '')
			elif repeat_matches[i]['Strand'] == '-':
				seq = SeqRecord(seq_record.seq.reverse_complement()[spacer_start:spacer_end], id = repeat_matches[i]['SeqName']+' '+str(cur_sp_n), description = '')
			else: print("Error in find_spacers_fuzznuc")
			if len(spacer.seq) in range (29, 31): 
				spacers[-1].append(spacer)
				sp_fasta_out.append(spacer)
				spacers_number +=1
				sp_in = True
			else: cur_sp_n-=1
			spacer_start = int(repeat_matches[i]['End'])
			i+=1
		if not sp_in: spacers.pop()
		k+=1

	sp_fasta_out = [f for f in sorted(sp_fasta_out, key=lambda x : str(x.seq))]
	SeqIO.write(sp_fasta_out, spacers_fasta, "fasta")
	return spacers

def use_bowtie2 (spacers_fasta, reference, outdir, bowtie2_dir=False):
	if not bowtie2_dir: bowtie2_dir = '/home/anna/bioinformatics/bioprograms/bowtie2-2.2.3/'
	bowtie2_out = outdir + 'bowtie2_out/'
	if not os.path.exists(bowtie2_out):
	    os.makedirs(bowtie2_out)
	bt2_base = bowtie2_out + 'bt2_base'
	bowtie2_build = [bowtie2_dir + './bowtie2-build', '-q', reference, bt2_base]
	call(bowtie2_build)
	sam_file = bowtie2_out + 'alignment.sam'
	bowtie2 = [bowtie2_dir + './bowtie2', '-x', bt2_base, '-f', '-U', spacers_fasta, '-S', sam_file]
	call(bowtie2)
	return bowtie2_out

def handle_HTS (file_fw, file_rv, outdir, reference = False):

	if ONLY_FIND == True: 
		flash_out = outdir + 'flash_out/'
	else: 
		flash_out = flash_merge(file_fw, file_rv, outdir)

	combined_reads = flash_out + 'out.extendedFrags.fastq'
	not_combined_reads = flash_out + 'out.notCombined_1.fastq'
	spacers1 = find_spacers_fuzznuc(combined_reads, outdir)
	spacers2 = find_spacers_fuzznuc(not_combined_reads, outdir)
	spacers = spacers1 + spacers2

	spacers_file = outdir + 'spacers'
	spacers_out = []

	for line in spacers:
		line_out = []
		for spacer in line:
			line_out.append(str(spacer.seq))
		spacers_out.append(' '.join(line_out))
	spacers_out = '\n'.join(spacers_out)

	with open(spacers_file, 'w') as sp_file:
	   sp_file.write(spacers_out)
	sp_file.closed

	if USE_BOWTIE2 and reference:
		print 'use_bowtie2'
		use_bowtie2 (spacers_fasta, reference, outdir)
	return 0

def handle_files (workdir, file_fw = False, file_rv = False, HTS_dir = False, HTSes = False, multiproc = False, reference = False):
	if file_fw and file_rv:
		name_reads = file_from_path(file_fw)[0:-6]
		outdir = workdir + name_reads + '/'
		handle_HTS (file_fw, file_rv, outdir, reference = reference)

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

workdir = '/home/anna/bioinformatics/outdirs/'

file_fw = '/home/anna/bioinformatics/htses/T4bi_1.fastq'
file_rv = '/home/anna/bioinformatics/htses/T4bi_2.fastq'

reference = '/media/anna/biodata/stuff/pt7blue-T4.fasta'

handle_files (workdir, file_fw, file_rv, reference = reference)

# HTS_dir = '/home/anna/bioinformatics/HTS/HTSes/'
# HTSes = [('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
# ('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]
# handle_files(workdir, HTS_dir = HTS_dir, HTSes = HTSes, multiproc = True)