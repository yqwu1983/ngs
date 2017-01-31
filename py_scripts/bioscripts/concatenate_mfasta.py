#!/usr/bin/python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

fasta_file = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/blastocrithidia/p57_scaffolds.fa'
outfile = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/blastocrithidia/p57_scaffolds_concatenated.fa'
id="p57_scaffolds_concatenated"
handle = open(fasta_file, 'r')

whole_seq=''

for record in SeqIO.parse(handle, "fasta"):
    cur_seq = record.seq
    whole_seq += cur_seq

result_record = SeqRecord(whole_seq,
        id=id, name='',
        description='')
SeqIO.write(result_record, open(outfile, 'w'), "fasta")
