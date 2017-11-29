#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.helpers.parse_dicts import *
from py_scripts.helpers.parse_csv import *

def load_functions(session, csv_path, exact_ids=True, organism=''):
    if organism == 'Arabidopsis thaliana': exact_ids=False
    for dic in csv_to_list_of_dicts(csv_path)[0]:
        seqid = dic['seqid']
        function = dic['function']
        if dic['mitochondrial'] == 'yes': mitochondrial = True
        elif dic['mitochondrial'] == 'no': mitochondrial = False
        else:
            print "Error in field 'mitochondrial' "
            sys.exit(1)

        if exact_ids:
            cur_seq = session.query(Sequence).filter(Sequence.seqid == dic['seqid']).one_or_none()
            if cur_seq:
                cur_seq.function = function
                cur_seq.mitochondrial = mitochondrial
                session.add(cur_seq)
            else: print organism, seqid
        else:
            cur_seqs = session.query(Sequence).filter(Sequence.seqid.like("%" + dic['seqid'] + "%"), Sequence.organism == organism)
            if cur_seqs:
                for seq in cur_seqs:
                    seq.function = function
                    seq.mitochondrial = mitochondrial
                    session.add(seq)
            else:
                print seqid

    session.commit()
    return 0

def load_targetp(session, targetp_csv_path, exact_ids=True, organism=False):
    for dic in csv_to_list_of_dicts(targetp_csv_path)[0]:
        seqid = dic['seqid']
        loc = dic['loc']
        locrate = dic['locrate']
        if exact_ids:
            cur_seq = session.query(Sequence).filter(Sequence.seqid == seqid).one()
        else:
            cur_seq = session.query(Sequence).filter(Sequence.seqid.like(seqid + '%'), Sequence.organism == organism).one_or_none()
        if cur_seq:
            cur_seq.loc = loc
            cur_seq.locrate = locrate
            session.add(cur_seq)
        else:
            print seqid
    session.commit()
    return 0

def load_ogs(session, og_path):
    ogs = csv_to_list_of_dicts(og_path)[0]
    i = 0
    for seq in session.query(Sequence):
        i+=1
        if i%1000 == 0: print i, 'sequences have been loaded'
        seqid = seq.seqid
        organism = seq.organism
        for og in ogs:
            if organism == 'Homo sapiens':
                break
            else:
                if seqid in og[organism]:
                    seq.og = og['OrthoGroup']
                    session.add(seq)
                    break
        else:
            print seqid, 'og has not been loaded'
    session.commit()
    return 0
