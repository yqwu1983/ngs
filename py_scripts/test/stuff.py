from Bio import SeqIO

def find_spacers_fuzzysearch(repeat_fw, seq, max_distance, spacers_array):
	spacers = []
	repeat_rv = reverse(repeat_fw)
	repeat_matches_fw = find_near_matches(repeat_fw, seq, max_l_dist = max_distance)
	repeat_matches_rv = find_near_matches(repeat_rv, seq, max_l_dist = max_distance)
	if not (len(repeat_matches_fw) <= 0 and len(repeat_matches_rv) <= 0): 
		if len(repeat_matches_fw) >= len(repeat_matches_rv):
			for i in range(len(repeat_matches_fw)-1):
				spacer_start = repeat_matches_fw[i].end + 1
				spacer_end = repeat_matches_fw[i+1].start
				spacer = seq[spacer_start : spacer_end]
		 		if len(spacer) in range (28, 31): 
		 			spacers.append(spacer)
		else:
			seq = reverse(seq)
			for i in range(len(repeat_matches_rv)-1):
				spacer_start = repeat_matches_rv[i].end + 1
				spacer_end = repeat_matches_rv[i+1].start
				spacer = seq[spacer_start : spacer_end]
		 		if len(spacer) in range (29, 31): 
		 			spacers.append(spacer)
		if len(spacers)>0 : spacers_array.append(spacers)
	return 0
	
# print spacers_array

# 	merge_by_flash(work_dir, file_fw, file_rv, outdir)

# for output_flash in ('.extendedFrags.fastq', '.notCombined_1.fastq', '.notCombined_2.fastq'):
#     file_fastq = outdir + 'FlashOutput/' + name_reads +  output_flash
#     file_fasta = file_fastq[0:-1] + 'a'
#     SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# for f in (name_fw, name_rv):
# 	file_fastq = work_dir + '/' + f
# 	file_fasta = outdir + '/' + f[0:-1] + 'a'
# 	SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# seqs = ('CGGCATCACCTTTGGCTTCGGCTGCGGTTTCTCCCCGCTGGCGCGGGGAACTCTGCGTAAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGTGGTTTATCCTCGCTGGTGCGGGGAACTCTCTAAAAGCTTACATTTGTTCTTAAAGCATTTTTTTCCATAAAAACAACCCATCAACCTTAGATCGGAAGAGCAC',
#  	'NAGGTTGGTGGGTTGTTTTTATGGGATAAAATGCTTTAAGAACAAATGTATACTTTTAGAGAGTTCCCCGCGCCAGCGGGGATAAACCGTTGTCTTTCGCTGCTGAGGGTGACGATCCCGCGAGTTCCCTGCGCCAGGGGGGATAAACCGCTTTCGCAGACGCGCGGCGATACGCTCACGCAGAGTTGCCCGCGCCAGCGGGGATCAACCGCAGCCGAAGGCAAAGGTGATGACGAGATTGGAAGAGCGG',
#  	'CCGTCCGCGCGCTTCCGATCTCGGCATCACCTTTGGCTTCGGCTGCGGTTTATCCCCGCTGGCGCGGGGAACTCTGCGTGAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGCGGTTTATCCCCGCTGGCGCGGGGAACTCTCTAAAAGTATACATTTGTTCTTAAAGCATTTTTTCCCATAAAAACAACCCACCAACCTTAGATCGGAAGAGCAC')

# for seq in seqs:
# 	for max_distance in range(3, 5):
#  		find_spacers(repeat_fw, seq, max_distance, spacers_array)

# file_fasta = outdir + '/' + name_reads + '.notCombined_2.fasta'

# SeqIO.write(records, rev_comp, "fasta")

# cd ~/BRIG-0.95-dist && java -jar /home/anna/BRIG-0.95-dist/BRIG.jar #open BRIG

# reads = '/home/anna/bioinformatics/HTS-all/HTSes/CTG_CCGTCC_L001_1.fastq'
# for seq_record in SeqIO.parse(reads, "fastq"):
# 	seq_record_rv = seq_record.seq.reverse_complement()
# 	print seq_record_rv[9:60]
# # for f in (name_fw, name_rv):
# # 	file_fastq = work_dir + '/' + f
# # 	file_fasta = outdir + '/' + f[0:-1] + 'a'
# # 	SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")
# file_fastq = '/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/flash_out/out.extendedFrags.fastq'
# # file_fasta = file_fastq[0:-1] + 'a'
# # SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# def get_length(inputStr):
#         return len(inputStr)
# f = open("/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/statistics_file.txt", "r+")
# f_sort = open("/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/statistics_sort.txt", 'w')
# lines = f.readlines()
# print lines
# # lines.sort()
# # print lines
# # f_sort.write(lines)
# # f.close()
# # f_sort.close()

# f = open("/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/statistics_file.txt", "r")
# lines = f.readlines()
# print lines

