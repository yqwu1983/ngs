import os
from subprocess32 import call
global THREADS; THREADS = 8
global RAM; RAM = 7

def spades_assemble(outdir, test=None, spades_dir=None, file_fw=None, file_rv=None, bbduk_out = None, trim_out=None, RAM=RAM):
	if not spades_dir: spades_dir = '/home/anna/bioinformatics/bioprograms/SPAdes-3.1.1-Linux/bin/'

	spades_out = outdir + 'spades_out/'
	spades = spades_dir + './spades.py'

	if test: spades_assemble= [spades, '--test'] # Test SPAdes

	else:

		if trim_out:
			files = {'PEfw' : 'paired_out_fw.fastq', 'PErv' : 'paired_out_rv.fastq', 
					 'UPfw': 'unpaired_out_fw.fastq', 'UPrv': 'unpaired_out_rv.fastq'}
			for key in files:
				files[key] = trim_out + files[key]
				spades_options = ['-1', files['PEfw'], '-2', files['PErv'], '-s', files['UPfw'], '-s', files['UPrv'], 
								  '-o', spades_out, '-m '+ str(RAM), '--careful']
				spades_assemble= [spades] + spades_options

		elif file_fw and file_rv:
			spades_options = ['-o', spades_out, '-m '+ str(RAM), '--only-assembler']
			spades_assemble = [spades, '-1', file_fw, '-2', file_rv] + spades_options

		else: print "Error: spades_assemble haven't get needed values"

		if not os.path.exists(spades_out): os.makedirs(spades_out)
		call(spades_assemble)
		
	print(' '.join(spades_assemble))
	return spades_out

def velvet_assemble(outdir, test=None, velvet_dir=None, file_fw=None, file_rv=None, bbduk_out = None, trim_out=None, RAM=7):
	if not velvet_dir: velvet_dir = '/home/anna/bioinformatics/bioprograms/velvet_1.2.10/'

	velvet_out = outdir + 'velvet_out/'	
	if not os.path.exists(velvet_out): os.makedirs(velvet_out)
	velvet = [velvet_dir + './VelvetOptimiser.pl']
	velvet_options = ['-g', '4.6', '-t', str(THREADS), '-d', velvet_out]
	velvet_assemble = velvet + ['-f', '\'' + '-shortPaired -fastq ' + file_fw + ' -shortPaired2 -fastq ' + file_rv + '\'']

	print ' '.join(velvet_assemble)
	call(velvet_assemble)
	return velvet_out