#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast_parser import BlastParser
from database.models import *
from py_scripts.bioscripts.seq_info_to_dict import *

Sequence.drop_table()
db.create_table(Sequence)

fasta_path = '/home/anna/bioinformatics/euglena_project/trypanosoma/tr_proteins.fasta'
info_csv = '/home/anna/bioinformatics/euglena_project/trypanosoma/triponasoma_info.csv'
info_dict = seq_info_to_dict(info_csv)
Sequence.read_from_f(fasta_path, seqtype='protein', organism='Trypanosoma brucei', source='T. brucei table',  info_dict=info_dict)

fasta_path = '/home/anna/bioinformatics/euglena_project/yeast/yeast_orf_trans_all.fasta'
info_csv = '/home/anna/bioinformatics/euglena_project/yeast/yeast_all.csv'
info_dict = seq_info_to_dict(info_csv)
Sequence.read_from_f(fasta_path, seqtype='protein', organism='Saccharomyces cerevisiae', source='yeast_orf_trans_all', info_dict=info_dict)

fasta_path = '/home/anna/bioinformatics/euglena_project/mitocarta/Human.MitoCarta2.0.fasta'
info_csv = '/home/anna/bioinformatics/euglena_project/mitocarta/Human.MitoCarta.2.0.csv'
info_dict = seq_info_to_dict(info_csv)
Sequence.read_from_f(fasta_path, seqtype='protein', organism='Homo sapiens', source='Human.MitoCarta2.0')

fasta_path = '/home/anna/bioinformatics/euglena_project/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS.fasta'
info_csv = '/home/anna/bioinformatics/euglena_project/euglena/all_euglena_proteins/euglena_info.csv'
info_dict = seq_info_to_dict(info_csv)
Sequence.read_from_f(fasta_path, seqtype='protein', organism='Euglena gracilis', source='E_gracilis_transcriptome_final.PROTEINS', info_dict=info_dict)
