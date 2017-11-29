import os
import subprocess32
global THREADS
global CLUSTER; CLUSTER=False
if CLUSTER: THREADS = 24
else: THREADS = 8
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

def use_bowtie2 (bt2_base, outdir, keep_unaligned=True):
	bowtie2_out = outdir + 'bowtie2_out_' +  file_from_path(reference)[0:-6] + file_from_path(unpaired)[0:-6] + '/'
	sam_file = bowtie2_out + 'alignment.sam'
	options = ['-p', str(THREADS), '--reorder', '-x', bt2_base, '-1', paired1, '-2', paired2, '-f', '-U', unpaired1, unpaired2, '-S', sam_file]
	if keep_unaligned: 
		unaligned = bowtie2_out + 'unaligned.fasta'
		options = ['--un', unaligned] + options
	call_bowtie2 = ['bowtie2', options]
	subprocess32.call(call_bowtie2)
	return bowtie2_out

bt2_base = ''