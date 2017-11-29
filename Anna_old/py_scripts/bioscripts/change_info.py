#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from helpers.make_outdir import *
from helpers.lookahead import *
from helpers.parse_csv import *

def add_functions(self, path, delimiter):

    self.write_blast_csv(outfile_path=outfile_path, hits=hits, header=True)
    return outfile_path

targetp_csv_path = '/home/anna/bioinformatics/euglena_project/mitocarta/first_130_targetp_out.csv'
function_path = ''
csv_to_dict(csv_path)
