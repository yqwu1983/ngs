#!/usr/bin/python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

long_fasta = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_all_proteins.fasta'

handle = open(long_fasta, 'r')
records = list(SeqIO.parse(handle, "fasta"))
record = records[0]

for pos, chunk in enumerate(chunks(record.seq.tostring(), 5000)):
    chunk_record = SeqRecord(Seq(
        chunk, record.seq.alphabet),
        id=record.id, name=record.name,
        description=record.description)
    outfile = "/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/data/euglena_proteins_splitted/euglena_proteins_group_%d.fasta" % pos
    SeqIO.write(chunk_record, open(outfile, 'w'), "fasta")
