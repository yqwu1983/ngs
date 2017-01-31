import os
import subprocess32
global THREADS; THREADS = 8
from ntpath import split

def file_from_path(path):
    head, tail = split(path)
    return tail

def cr_outdir(file_fw, reference, workdir):
	name_reads = file_from_path(file_fw)[0:-6]
	name_ref = file_from_path(reference)[0:-6]
	outdir = workdir + name_reads + '_' + name_ref + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

def use_bowtie2 (reference, outdir, unpaired=False, reads1=False, reads2=False, keep_unaligned=False, bowtie2_dir=False):
	if not bowtie2_dir: bowtie2_dir = '/home/anna/bioinformatics/bioprograms/bowtie2-2.2.3/'
	bowtie2_out = outdir + file_from_path(reference)[0:-6] + '/'
	if not os.path.exists(bowtie2_out): os.makedirs(bowtie2_out)
	bt2_base = bowtie2_out + 'bt2_base'
	bowtie2_build = [bowtie2_dir + './bowtie2-build', '-q', reference, bt2_base]
	subprocess32.call(bowtie2_build)
	bowtie2 = [bowtie2_dir + './bowtie2']
	if reads1 and reads2:
		# bowtie2_out = outdir + 'bowtie2_out_' +  file_from_path(reference)[0:-6] + file_from_path(reads1)[0:-6] + file_from_path(reads2)[0:-6] + '/'
		sam_file = bowtie2_out + 'alignment.sam'
		options = ['-p', str(THREADS), '--reorder', '-x', bt2_base, '-1', reads1, '-2', reads2, '-S', sam_file]
	elif unpaired:
		bowtie2_out = outdir + 'bowtie2_out_' +  file_from_path(reference)[0:-6] + file_from_path(unpaired)[0:-6] + '/'
		sam_file = bowtie2_out + 'alignment.sam'
		options = ['-p', str(THREADS), '--reorder', '-x', bt2_base, '-f', '-U', unpaired, '-S', sam_file]
	else: print "Error. Function use_bowtie2: wrong set of arguments"
	if keep_unaligned: 
		unaligned = bowtie2_out + 'unaligned.fasta'
		# , '--no-mixed', '--no-discordant'
		options = ['--un', unaligned] + options
	call_bowtie2 = bowtie2 + options
	subprocess32.call(call_bowtie2)
	return bowtie2_out

# reference = '/home/anna/bioinformatics/outdirs/mut6/contigs_mut6.fasta'
# reference = '/home/anna/bioinformatics/references/pBad.fasta'
reference = '/home/anna/bioinformatics/references/BL21.fasta'
outdir = '/home/anna/bioinformatics/outdirs/mut6/'
reads1 = '/home/anna/bioinformatics/htses/dasha/Ecoli-mut6_trimmed_paired_R1.fastq'
reads2 = '/home/anna/bioinformatics/htses/dasha/Ecoli-mut6_trimmed_paired_R2.fastq'
use_bowtie2 (reference, outdir, reads1=reads1, reads2=reads2, keep_unaligned=True)