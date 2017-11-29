#!/usr/bin/python
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.helpers.make_outdir import *
from py_scripts.helpers.parse_csv import *

def load_fasta(session, fasta_path, seqtype, organism='unknown organism', source=False, description_path=False):
    print description_path, organism
    if description_path:
        dict_of_functions = csv_to_dict(description_path, main_key='seqid')[0]
    for record in SeqIO.parse(fasta_path, "fasta"):
        seqid = record.id
        if not source: source = file_from_path(fasta_path, endcut=6)
        new_seq = Sequence(seqid=seqid, seqtype=seqtype, organism=organism, source=source, extra_data={}, len=len(record.seq))
        new_seq.extra_data['sequence'] = str(record.seq)
        new_seq.extra_data['description'] = str(record.description)
        if description_path:
            if organism == 'Arabidopsis thaliana':
                seqid = seqid[0:-2]
            if seqid in dict_of_functions.keys():
                cur_dic = dict_of_functions[seqid]
                new_seq.function = cur_dic['function']
                new_seq.og = cur_dic['og']
                if cur_dic['mitochondrial'] == 'yes': new_seq.mitochondrial=True
                elif cur_dic['mitochondrial'] == 'no': new_seq.mitochondrial=False
                else:
                    print "Error in field 'mitochondrial', seqid", seqid
                    sys.exit(1)
        session.add(new_seq)
    session.commit()
    return 0
