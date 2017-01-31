#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from subprocess32 import call
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.make_outdir import *
from py_scripts.helpers.lookahead import lookahead
from subprocess import Popen, PIPE, STDOUT
import csv

def is_targetp_info(targetp_line):
	garbage_starts = ['### ta', 'Number', 'Cleava', 'Using ', 'Name  ', '------', 'cutoff']
	if targetp_line[:6] in garbage_starts: return False
	else: return True

def use_targetp(f_path, outf_path=False, is_plant=False, cleavage_sites=False, txt_out=False):
	targetp_path = '/home/anna/bioinformatics/bioprograms/targetp-1.1/'
	targetp_path += 'targetp'
	if is_plant: targetp_call = [targetp_path, '-P']
	else: targetp_call = [targetp_path, '-N']
	if cleavage_sites: targetp_call.append('-c')
	out_data = []
	seq_batch = []
	i = 0
	k = 0
	for seqrecord, is_last in lookahead(SeqIO.parse(f_path, "fasta")):
		seq_batch.append(seqrecord.format("fasta"))
		i+=1
		if i == 1000 or is_last:
			k+=1
			print 'Batch #', k
			seq_batch = '\n'.join(seq_batch)
			targetp = Popen(targetp_call, stdout=PIPE, stdin=PIPE, stderr=PIPE)
			out_data.extend(targetp.communicate(input=seq_batch))
			seq_batch = []
			i = 0

	if txt_out:
		if not outf_path: outf_path = new_file(f_path, new_end='_targetp_out.txt')
		with open(outf_path, 'w') as outf:
			outf.writelines(out_data)
			outf.closed

	csv_out = []
	for s in out_data:
		lines = filter(is_targetp_info, s.split('\n'))
		for line in lines:
			line = line.split()
			if line: csv_out.append(line)

		if not outf_path: outf_path = new_file(f_path, new_end='_targetp_out.csv')
		with open(outf_path, 'w') as outf:
		    csv_writer = csv.writer(outf)
		    if is_plant:
		    	header = ['seqid', 'length', 'chloro_score', 'mito_score', 'secret_score', 'other_score', 'loc', 'locrate']
		    else:
		    	header = ['seqid', 'length', 'mito_score', 'secret_score', 'other_score', 'loc', 'locrate']
		    if cleavage_sites: header.append(['cleavage_site'])
		    csv_writer.writerow(header)
		    csv_writer.writerows(csv_out)

	return outf_path

# f_paths = [
# '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS_M_cut.fasta'
# ]
# for f_path in f_paths:
# 	use_targetp(f_path, is_plant=False)
# 	use_targetp(f_path, is_plant=True)
f_path = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS_M_cut.fasta'
outf_path = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS_M_cut_targetp_not_chloro.csv'
use_targetp(f_path, outf_path, is_plant=False)
f_path = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS_M_cut.fasta'
outf_path = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS_M_cut_targetp_chloro.csv'
use_targetp(f_path, outf_path, is_plant=True)
