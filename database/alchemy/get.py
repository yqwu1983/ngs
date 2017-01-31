#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *
from py_scripts.helpers.parse_dicts import *

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito_all.db'
engine = create_engine(db_path)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

seqs = session.query(Sequence)
fieldnames = ['seqid', 'og', 'b2go_mito', 'loc', 'locrate', 'function', 'subj_id', 'subj_og', 'organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
default_seq_dict = {}
for name in fieldnames:
    default_seq_dict[name] = ''

    result_table = []
    for seq in seqs:
        if seq.organism == 'Euglena gracilis' and seq.loc='M' and seq.locrate=1:
            seq_dict = default_seq_dict.copy()

            seq_dict['seqid'] = seq.seqid

            bs = seq.best_subject()
            if bs:
                bsseq = bs['sequence']
                seq_dict['subj_id'] = bsseq.seqid
                seq_dict['organism'] = bsseq.organism
                seq_dict['subj_function'] = bsseq.function

                bsh = bs['hit']
                seq_dict['evalue'] = bsh.evalue
                seq_dict['alen_slen'] = bsh.alen_slen
                seq_dict['pident'] = bsh.extra_data['pident']
                reverse_hit = seq.get_reverse_blasthit(bsseq)

                if reverse_hit:
                    seq_dict['rev_evalue'] = reverse_hit['hit'].evalue
                    seq_dict['rev_alen_qlen'] = reverse_hit['hit'].alen_qlen
                    seq_dict['rev_pident'] = reverse_hit['hit'].extra_data['pident']
                    seq_dict['is_best?'] = reverse_hit['is_best']
                    seq_dict['best_rev_evalue'] = reverse_hit['bsh'].evalue
                    seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
            result_table.append(seq_dict)
