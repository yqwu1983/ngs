from Bio import SeqIO
def find_genes(record, outdir):
	seq = record.seq
	rev_seq = seq.reverse_complement()
	for gene_name in ['pep', 'yej', 'omp', 'rim', 'pdf', 'sbm', 'asp', 'def']:
		genes = []
		for feature in record.features:
			if feature.type == 'gene':
				if 'gene' in feature.qualifiers:
					gene_name_gb = str(feature.qualifiers['gene'])
					if gene_name in gene_name_gb:
						start = feature.location.start
						end = feature.location.end
						if feature.location.strand == 1:
							seq_name = gene_name_gb.translate(None, '!@#$[]')
							gene = SeqIO.SeqRecord(seq[start:end], id = seq_name)
							genes.append(gene)
						elif feature.location.strand == -1:
							seq_name = gene_name_gb	.translate(None, '!@#$[]')
							gene = SeqIO.SeqRecord(rev_seq[start:end], id = seq_name)
							genes.append(gene)
						else: print 'Error'

		file_out = outdir + gene_name + '.fasta'
		genes = [f for f in sorted(genes, key=lambda x : str(x.id))]
		SeqIO.write(genes, file_out, "fasta")

file_gb = '/home/anna/bioinformatics/outdirs/BL21.gbk'
outdir = '/home/anna/bioinformatics/outdirs/genes_bl/'
record = SeqIO.read(file_gb, "genbank")
find_genes(record, outdir)

file_mut = '/home/anna/bioinformatics/outdirs/mut6/prokka_out/PROKKA_10052014.gbk'
outdir = '/home/anna/bioinformatics/outdirs/genes_mut6/'
records = []
for gene in ['pep', 'yej', 'omp', 'rim', 'sbm', 'asp']:
		genes = []
		for record in SeqIO.parse(file_mut, "genbank"):
			seq = record.seq
			rev_seq = seq.reverse_complement()
			for feature in record.features:
				if feature.type == 'gene':
					if 'gene' in feature.qualifiers:
						gene_name = str(feature.qualifiers['gene'])
						if gene in gene_name:
							start = feature.location.start
							end = feature.location.end
							if feature.location.strand == 1:
								genes.append(SeqIO.SeqRecord(seq[start:end], id = gene_name))
							elif feature.location.strand == -1:
								genes.append(SeqIO.SeqRecord(rev_seq[start:end], id =  gene_name))
							else: print 'Error'
		genes = [f for f in sorted(genes, key=lambda x : str(x.id))]
		file_out = outdir + gene + '.fasta'
		SeqIO.write(genes, file_out, "fasta")

