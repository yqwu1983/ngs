#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from sqlalchemy import or_
from blast.classes.blast_parser import BlastParser

def load_blast_csv(session, blast_csv_path, custom_outfmt=False):
    if not custom_outfmt:
        custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
    blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()
    i = 0
    for blast_dict in blast_dicts:
        if i%10000==0: print i, 'records have been loaded'
        i+=1
        query_id, subject_id = blast_dict['qseqid'], blast_dict['sseqid']
        evalue, length = blast_dict['evalue'], blast_dict['length']
        qlen, slen = blast_dict['qlen'], blast_dict['slen']
        alen_qlen, alen_slen = float(length/float(qlen)), float(length/float(slen))
        other_features = {}
        for feature in blast_dict:
            if feature not in ['qseqid', 'sseqid', 'evalue', 'length', 'qlen', 'slen']:
                other_features[feature] = blast_dict[feature]

        query_and_subject = session.query(Sequence).filter(or_(Sequence.seqid == query_id, Sequence.seqid == subject_id))
        if query_and_subject:
            for seq in query_and_subject:
                if seq.seqid == query_id:
                    query = seq
                elif seq.seqid == subject_id:
                    subject = seq
                else:
                    print 'Error in BlastHit loading, seqid', seq.seqid
                    sys.exit(1)
        new_bh = BlastHit(query=query, subject=subject, evalue=evalue, length=length,
                        qlen=qlen, slen=slen, alen_qlen=alen_qlen, alen_slen=alen_slen,
                        extra_data=other_features)
        session.add(new_bh)
    session.commit()