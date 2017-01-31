import os
from ntpath import split
from subprocess32 import call

def flash_merge(file_fw, file_rv, outdir, flash_dir = False):
	if not flash_dir: flash_dir = '/home/anna/bioinformatics/bioprograms/FLASH/'
	flash_out = outdir + 'flash_out/'
	if not os.path.exists(flash_out):
	    os.makedirs(flash_out)

	options_flash = ['-d', flash_out, '-O', '-M 250', '-x 0.25']
	flash = flash_dir + './flash'
	flash_merge = [flash] + options_flash + [file_fw, file_rv]
	call(flash_merge)
	return flash_out