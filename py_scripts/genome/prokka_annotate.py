from subprocess32 import call
def prokka_annotate (sequence, outdir, prokka_dir=None):
	if not prokka_dir: prokka_dir = '/home/anna/bioinformatics/bioprograms/prokka-1.10/bin/'
	prokka_out = outdir + 'prokka_out/'
	prokka = prokka_dir + './prokka'
	prokka_options = ['--centre', 'XXX', '--kingdom', 'Bacteria',  '--gram', 'neg', '--addgenes',  '--outdir', prokka_out, '--force', sequence, '--genus', 'Pandoraea']
	prokka_annotate = [prokka] + prokka_options
	call(prokka_annotate)
	return prokka_out



# '--genus', 'Escherichia', '--species',
# 					  'coli',
