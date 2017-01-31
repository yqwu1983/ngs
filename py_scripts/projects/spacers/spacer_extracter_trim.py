#!/usr/bin/python
import os
import csv
from ntpath import split
import subprocess32
from string import maketrans
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from natsort import natsorted

global ONLY_FIND; ONLY_FIND = False
global ONLY_SPACERS; ONLY_SPACERS = False
global MAX_PROCESSES; MAX_PROCESSES = 8
global REPEAT; REPEAT = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
global USE_BOWTIE2; USE_BOWTIE2 = True
global MULTIPROC; MULTIPROC = False
global THREADS; THREADS = 8

def file_from_path(path):
    head, tail = split(path)
    return tail

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

def flash_merge(file_fw, file_rv, outdir, flash_dir = None):
	if not flash_dir: flash_dir = '/home/anna/bioinformatics/bioprograms/FLASH/'
	flash_output = outdir + 'flash_out/'
	if not os.path.exists(flash_output):
	    os.makedirs(flash_output)

	options_flash = ['-d', flash_output, '-O', '-M 300', '-x 0.10']
	flash = flash_dir + './flash'
	flash_merge = [flash] + options_flash + [file_fw, file_rv]
	subprocess32.call(flash_merge)
	return flash_output

def trimc_trim (file_fw, file_rv, outdir, trimc_dir=None):
	if not trimc_dir: trimc_dir = '/home/anna/bioinformatics/bioprograms/Trimmomatic-0.32/'
	trim_out = outdir + 'trim_out/'
	if not os.path.exists(trim_out):
	    os.makedirs(trim_out)

	trimlog = trim_out +'trimlog'
	paired_out_fw = trim_out + 'paired_out_fw' + '.fastq'
	unpaired_out_fw = trim_out + 'unpaired_out_fw' + '.fastq'
	paired_out_rv = trim_out + 'paired_out_rv' + '.fastq'
	unpaired_out_rv = trim_out + 'unpaired_out_rv' + '.fastq'

	adapters_file = trimc_dir + 'adapters/'+ "illumina.fasta"

	trimmomatic = ['java', '-jar', trimc_dir + 'trimmomatic-0.32.jar']
	trim_options = ['PE', '-threads', str(THREADS), '-phred33', '-trimlog', trimlog, file_fw, file_rv,
					paired_out_fw, unpaired_out_fw, paired_out_rv, unpaired_out_rv,
					'ILLUMINACLIP:'+ adapters_file + ':2:30:10']
	trim = trimmomatic + trim_options
	subprocess32.call(trim)
	return trim_out

def use_fuzznuc (reads, pattern, outdir = None, max_mismatch = 5, stdout = None, indels = None, name = ''):
	if stdout:
		fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern]
		fuzznuc_options = ['-pmismatch', str(max_mismatch), '-complement', '-snucleotide1', '-squick1',
						   '-rformat2', 'excel', '-stdout', '-auto']
		fuzznuc = fuzznuc + fuzznuc_options
		fuzznuc_out = subprocess32.Popen((fuzznuc), stdout=subprocess32.PIPE, bufsize=100)
	else:
		fuzznuc_out = outdir + 'fuzznuc_report' + name
		fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern, '-outfile', fuzznuc_out]
		fuzznuc_options = ['-pmismatch', str(max_mismatch), '-complement', '-snucleotide1', '-squick1',
						   '-rformat2', 'excel']
		fuzznuc = fuzznuc + fuzznuc_options
		subprocess32.call(fuzznuc)

	return fuzznuc_out

def find_spacers_fuzznuc(reads):
	output_pipe = use_fuzznuc(reads, REPEAT, stdout = True).stdout
	spacers = []
	spacers_number = 0
	reads_iter = SeqIO.parse(reads, "fastq")
	read = next(reads_iter)
	last_repeat = None
	for line in iter(output_pipe.readline, ''):
		row = line.split('\t')
		if row[0] != 'SeqName':
			repeat = {'seqid': row[0], 'start': row[1], 'end': row[2], 'strand': row[4]}
			if last_repeat:
				if repeat['seqid'] == last_repeat['seqid']:
					spacer_start = int(last_repeat['end'])-1
					spacer_end = int(repeat['start'])-1
					while repeat['seqid'] != read.id:
						read = next(reads_iter)
					if repeat['strand'] == '+':
						spacer_seq = read.seq[spacer_start:spacer_end]
					elif repeat['strand'] == '-':
						spacer_seq = read.seq.reverse_complement()[spacer_start:spacer_end]
					else: print("Error in find_spacers_fuzznuc")
					if len(spacer_seq) in range (28, 33):
						spacers_number +=1
						cur_spacer_n += 1
						description = 'CRISPR cassette ' + read.id[-11: len(read.id)]
						spacer = SeqRecord(spacer_seq, id = read.id + ' spacer ' + str(cur_spacer_n), description = description)
						spacers.append(spacer)
			last_repeat = repeat
		else: cur_spacer_n = 0
	print str(spacers_number) + ' spacers founded'
	return spacers

def use_bowtie2 (reference, outdir, unpaired=None, reads1=None, reads2=None, keep_unaligned=None, bowtie2_dir=None):
	if not bowtie2_dir: bowtie2_dir = '/home/anna/bioinformatics/bioprograms/bowtie2-2.2.3/'
	bowtie2_out = outdir + file_from_path(reference)[0:-6] + '/'
	if not os.path.exists(bowtie2_out): os.makedirs(bowtie2_out)
	bt2_base = bowtie2_out + 'bt2_base'
	bowtie2_build = [bowtie2_dir + './bowtie2-build', '-q', reference, bt2_base]
	subprocess32.call(bowtie2_build)
	sam_file = bowtie2_out + 'alignment.sam'
	bowtie2 = [bowtie2_dir + './bowtie2']
	if reads1 and reads2:
		options = ['-p', str(THREADS), '--reorder', '--local', '-x', bt2_base, '-1', reads1, '-2', reads2, '-S', sam_file]
	elif unpaired:
		options = ['-p', str(THREADS), '--reorder', '--local','-x', bt2_base, '-f', '-U', unpaired, '-S', sam_file]
	else: print "Error. Function use_bowtie2: wrong set of arguments"
	if keep_unaligned:
		unaligned = bowtie2_out + 'unaligned.fasta'
		options = ['--un', unaligned] + options
		call_bowtie2 = bowtie2 + options
		subprocess32.call(call_bowtie2)
		return bowtie2_out, unaligned
	else:
		call_bowtie2 = bowtie2 + options
		subprocess32.call(call_bowtie2)
		return bowtie2_out

def handle_hts (file_fw, file_rv, outdir, reference = None):
	trim_out = trimc_trim(file_fw, file_rv, outdir)
	trimmed_fw = trim_out + 'paired_out_fw.fastq'
	trimmed_rv = trim_out + 'paired_out_rv.fastq'
	flash_out = flash_merge(file_fw, file_rv, outdir)
	files_trim = ['unpaired_out_fw.fastq', 'unpaired_out_rv.fastq']
	files_flash = ['out.extendedFrags.fastq', 'out.notCombined_1.fastq', 'out.notCombined_2.fastq']
	files = []
	for f in files_trim:
		files.append(trim_out + f)
	for f in files_flash:
		files.append(flash_out + f)
	spacers = []
	for f in files:
		spacers.extend(find_spacers_fuzznuc(f))
	spacers_file = outdir + 'spacers.fasta'
	SeqIO.write(spacers, spacers_file, "fasta")

	if USE_BOWTIE2 and reference:
		bowtie2_out, unaligned = use_bowtie2 (reference, outdir, unpaired=spacers_file, keep_unaligned=True)
		return bowtie2_out, unaligned
	return 0

def handle_files (workdir, file_fw = None, file_rv = None, hts_dir = None, htses = None,
				  ref_dir = None, reference = None, references=None):
	if file_fw and file_rv:
		if references:
			name_reads = file_from_path(file_fw)[0:-6]
			outdir = workdir + name_reads + '/'
			i = 0
			for ref in references:
				reference = ref_dir + ref
				if i == 0: align_dir, unaligned = handle_hts (file_fw, file_rv, outdir, reference)
				else: align_dir, unaligned = use_bowtie2 (reference, align_dir, unpaired=unaligned, keep_unaligned=True)
				i = i+1


	elif hts_dir and htses:
		process_count = 0
		for fw, rv in htses:
			file_fw = hts_dir + fw
			file_rv = hts_dir + rv
			name_fw = file_from_path(file_fw)
			name_rv = file_from_path(file_rv)
			name_reads = name_fw[0:-6]
			outdir = workdir + name_reads + '/'
			if not os.path.exists(outdir): os.makedirs(outdir)
			if not MULTIPROC:
				if not ONLY_FIND: handle_hts (file_fw, file_rv, outdir)
				else: handle_hts (file_fw, file_rv, outdir)
			else:
				pid = os.fork()
				time.sleep(0.1)
				if pid == 0:
					if not ONLY_FIND: handle_hts (file_fw, file_rv, outdir)
					else: handle_hts (file_fw, file_rv, outdir)
					os.abort()
				else:
					process_count += 1
					if process_count >= MAX_PROCESSES:
						os.wait()
						process_count -= 1

	else: print "Error: handle_htses haven't get needed values"
	return 0

file_fw = '/home/anna/bioinformatics/htses/T5adapt_ACTTGA_L001_R1_001.fastq'
file_rv = '/home/anna/bioinformatics/htses/T5adapt_ACTTGA_L001_R2_001.fastq'
workdir = '/home/anna/bioinformatics/outdirs/'
ref_dir = '/home/anna/bioinformatics/references/'
references = ['SS_39_CRISPR.fasta', 'first_10_kb_t5.fasta', 't5.fasta', 'pT7blue-G8esc_rev.fasta', 'KD263_CRISPR_region.fasta',
			  'pt7blue-T4.fasta', 'T4_genome.fasta', 'BW25113.fasta', 'BL21.fasta', 'pBad.fasta']

handle_files (workdir, file_fw=file_fw, file_rv=file_rv, ref_dir = ref_dir, references=references)
