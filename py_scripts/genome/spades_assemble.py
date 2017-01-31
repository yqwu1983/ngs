import os
from subprocess32 import call
def spades_assemble(outdir, test=None, reads = None, file_fw=None, file_rv=None, spades_dir=None, bbduk_out = None, trimc_out=None, RAM=6):
	if not spades_dir: spades_dir = '/home/anna/bioinformatics/bioprograms/SPAdes-3.1.1-Linux/bin/'

	spades_out = outdir + 'spades_out/'
	spades = spades_dir + './spades.py'

	if test: spades_assemble= [spades, '--test'] # Test SPAdes

	else:

		if trimc_out:
			files = {'PEfw' : 'paired_out_fw.fastq', 'PErv' : 'paired_out_rv.fastq', 
					 'UPfw': 'unpaired_out_fw.fastq', 'UPrv': 'unpaired_out_rv.fastq'}
			for key in files:
				files[key] = trimc_out + files[key]
				spades_options = ['-1', files['PEfw'], '-2', files['PErv'], '-s', files['UPfw'], '-s', files['UPrv'], 
								  '-o', spades_out, '-m '+ str(RAM), '--careful']
				spades_assemble= [spades] + spades_options

		elif file_fw and file_rv:
			spades_options = ['-o', spades_out, '-m '+ str(RAM), '--careful', '--only-assembler']
			spades_assemble = [spades, '-1', file_fw, '-2', file_rv] + spades_options

		elif reads: 
			spades_options = ['-o', spades_out, '-m '+ str(RAM), '--only-assembler']
			spades_assemble = [spades, '-s', reads] + spades_options

		else: print "Error: spades_assemble haven't get needed values"

		if not os.path.exists(spades_out): os.makedirs(spades_out)
		call(spades_assemble)

	return spades_out

outdir = '/home/anna/bioinformatics/HTS/outdirs'
reads = '/home/anna/bioinformatics/HTS/outdirs/T4ai_AGTTCC_L001_1/spacers0.fasta'
spades_assemble(outdir, reads = reads)
	