#!/usr/bin/python
from peewee import *
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast_parser import BlastParser
from database.models import *
from py_scripts.helpers.parse_csv import *

raw_query = """
select * from sequence
where organism = 'Euglena gracilis' and loc='M'
"""

seqs = Sequence.raw(raw_query)
result = []
for seq in seqs:
    result.append(seq.to_seqrecord())

out_file = '/home/anna/bioinformatics/euglena_project/euglena/mito_loc/all_mito.fasta'
print len(result)
SeqIO.write(result, out_file, "fasta")
