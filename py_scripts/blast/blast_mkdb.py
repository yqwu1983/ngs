#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast

subj_paths = [
# "/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis.fasta",
]

for subj in subj_paths:
	new_blast = Blast(subj_path=subj, db_type='prot')
	new_blast.makeblastdb()
