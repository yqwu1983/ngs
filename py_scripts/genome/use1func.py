#!/usr/bin/python
import os
from subprocess32 import call
from ntpath import split
global ONLY_TRIM; ONLY_TRIM = False
global ONLY_ASSEMBLE; ONLY_ASSEMBLE = True
global ONLY_ANNOTATE; ONLY_ANNOTATE = False
global THREADS; THREADS = 8
global RAM; RAM = 8
from trim import trimc_trim
import assemble
import use_quast
from prokka_annotate import prokka_annotate

def file_from_path (path):
    head, tail = split(path)
    return tail

def cr_outdir(file_fw, workdir):
	name_fw = file_from_path(file_fw)
	name_reads = name_fw[0:-6]
	outdir = workdir + name_reads + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

workdir = '/home/anna/bioinformatics/outdirs/'
file_fw = '/home/anna/bioinformatics/htses/dasha/Ecoli-mut6_trimmed_paired_R1.fastq'
file_rv = '/home/anna/bioinformatics/htses/dasha/Ecoli-mut6_trimmed_paired_R2.fastq'
outdir = cr_outdir(file_fw, workdir)
# use_quast (contigs, reference, outdir)

# # reference = '/home/anna/bioinformatics/hts/stuff/pt7blue-T4.fasta'
# reference = '/home/anna/bioinformatics/output_from_server/contigs.fasta'

# outdir = '/home/anna/bioinformatics/hts/outdirs/'
# prokka_annotate (f, outdir)
trimc_trim (file_fw, file_rv, outdir)
