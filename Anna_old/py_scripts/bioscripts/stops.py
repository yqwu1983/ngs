#!/usr/bin/python
from Bio import SeqIO
cds="/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/blastocrithidia/Lpyr_CDs.fa"
uga=0
uag=0
uaa=0
other=0

for record in SeqIO.parse(cds, "fasta"):
    seq=record.seq
    stop=seq[-3:len(seq)]
    if stop == "tga":
        uga += 1
    elif stop == "tag":
        uag += 1
    elif stop == "taa":
        uaa += 1
    else:
        other+=1

print "uga", uga
print "uag", uag
print "uaa", uaa
print "other", other



