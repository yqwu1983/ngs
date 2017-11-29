import os
from Bio import SeqIO

in_file = '/mnt/lustre/nenarokova/wheat/L00000210.BC1D3RACXX.5.fastq'
out_file1 = in_file[0:-6] + '_1.fastq'
out_file2 = in_file[0:-6] + '_2.fastq'
i = 0
out1 = []
out2 = []
out_file1 = open(out_file1, 'w')
out_file2 = open(out_file2, 'w')
for seq_record in SeqIO.parse(in_file, "fastq"):
	if i%2 == 0:
		SeqIO.write(seq_record, out_file1, "fastq")
	else:
		SeqIO.write(seq_record, out_file2, "fastq")
	i+=1

out_file1.close()
out_file2.close()
