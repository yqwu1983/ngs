from subprocess32 import call
def abacas_scaffold (contigs, reference, outdir, abacas_dir=None):
	if not abacas_dir: abacas_dir = '/home/anna/bioinformatics/bioprograms/Abacas/abacas.pl'
	abacas_out = outdir + 'abacas_out/'
	abacas = ['perl', abacas_dir + 'abacas.pl']
	abacas_options = ['-r', reference, '-q', contigs, '-b', '-c', '-m', '-p', nucmer]
	call(abacas + abacas_options)
	return abacas_out