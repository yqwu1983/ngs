#!/usr/bin/python
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Seq import Seq
f = '/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/SS_39_CRISPR/first_10_kb_t5/t5/pT7blue-G8esc_rev/KD263_CRISPR_region/pt7blue-T4/T4_genome/BW25113/BL21/pBad/unaligned.fasta'
result_handle = []
i = 0
for record in SeqIO.parse(f, "fastq"):
	# result_handle.extend(NCBIWWW.qblast("blastn", "nr", record.seq, hitlist_size=1))
	print NCBIWWW.qblast("blastn", "nr", record.seq, hitlist_size=1)
	if i>1:break
out = '/home/anna/bioinformatics/outdirs/unaligned_spacers.xml'
save_file = open(out, "w")
print result_handle
result = ''.join 
save_file.write(result_handle.read())
save_file.close()
result_handle.close()