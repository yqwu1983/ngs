#!/usr/bin/python
from Bio import Entrez
from Bio import SeqIO

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

global EMAIL; EMAIL = 'a.nenarokova@gmail.com'
global FEW_GENES; FEW_GENES = False

Entrez.email = EMAIL


if FEW_GENES == True:
	query = "((Triticum[Organism]) OR (Aegilops[Organism])) AND (NBS OR RGA) AND cds NOT BAC NOT PAC NOT scaffold NOT contig"
	handle = Entrez.esearch(db="nucleotide", term=query, retmax=7000)
	record = Entrez.read(handle)

	idlist = ",".join(record["IdList"])
	result = Entrez.efetch(db="nuccore", id=idlist, rettype="fasta", retmode="text")
	fasta = result.read()
	# out_file = '/home/anna/bioinformatics/wheat/NBS_LRR_wheat.fasta'
	out_file = '/home/nenarokova/wheat/NBS_LRR_all_plants.fasta'
	out = open(out_file, 'w')
	out.write(fasta)
	out.close()
else:
	# query = "((Triticum[Organism]) OR (Aegilops[Organism])) AND (NBS OR RGA) AND cds NOT BAC NOT PAC NOT scaffold NOT contig"
	query = 'NBS-LRR AND cds NOT BAC NOT PAC NOT scaffold NOT contig'
	handle = Entrez.esearch(db="nucleotide", term=query, retmax=7000)
	record = Entrez.read(handle)

	# out_file = '/home/anna/bioinformatics/wheat/NBS_LRR_wheat.fasta'
	out_file = '/home/nenarokova/wheat/NBS_LRR_all_plants.fasta'
	out = open(out_file, "a")

	genes_chunks = chunks(record["IdList"], 100)
	for genes_chunk in genes_chunks:
		idlist = ",".join(genes_chunk)
		print idlist
		result = Entrez.efetch(db="nuccore", id=idlist, rettype="fasta", retmode="text")
		fasta = result.read()
		out.write(fasta)
		
	out.close()
	
	
	