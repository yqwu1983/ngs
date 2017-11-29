from subprocess32 import call
def use_quast (contigs, outdir, reference = None, quast_dir=None):
	if not quast_dir: quast_dir = '/home/anna/bioinformatics/bioprograms/quast-2.3/'
	quast_out = outdir + 'quast_out/'
	quast = quast_dir + './quast.py'
	quast_options = ['-o', quast_out]
	if reference: quast_options = quast_options + ['-R', reference]
	use_quast = [quast] + quast_options + [contigs]
	call(use_quast)
	return quast_out
