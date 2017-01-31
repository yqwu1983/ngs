#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
sys.path.insert(0, "/home/nenarokova/ngs/")
from database.alchemy.models import *
from sqlalchemy.orm import joinedload
from py_scripts.helpers.parse_csv import *

def get_result_table_euglena(db_path, outpath):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    heap_size = 100000
    total_amount = session.query(Sequence).count()
    n_pages = total_amount/heap_size

    fieldnames = ['seqid', 'og', 'b2go_mito', 'loc', 'locrate', 'function', 'subj_id', 'subj_og', 'organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
    default_seq_dict = {}

    for name in fieldnames:
        default_seq_dict[name] = ''
    result_table = []

    print 'total pages: ', (n_pages + 1)
    for page in range(n_pages + 1):
        print 'page ', page
        seqs = session.query(Sequence).order_by('id').limit(heap_size).offset(heap_size*page).options(joinedload('query_blasthits'))
        for seq in seqs:
            if seq.organism == 'Euglena gracilis':
                seq_dict = default_seq_dict.copy()

                seq_dict['seqid'] = seq.seqid
                seq_dict['og'] = seq.og
                seq_dict['b2go_mito'] = seq.mitochondrial
                seq_dict['loc'] = seq.loc
                seq_dict['locrate'] = seq.locrate
                seq_dict['function'] = seq.function

                bs = seq.best_subject()
                if bs:
                    bsseq = bs['sequence']
                    seq_dict['subj_id'] = bsseq.seqid
                    seq_dict['subj_og'] = bsseq.og
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
                if (seq_dict['evalue'] < 0.00001) and (seq_dict['rev_evalue'] < 0.01) and (seq_dict['alen_slen'] >= 0.3) and bsseq.mitochondrial:
                    result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath


def get_result_table_perk(db_path, outpath):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    heap_size = 2500
    total_amount = session.query(Sequence).count()
    n_pages = total_amount/heap_size

    fieldnames = ['seqid', 'loc', 'locrate', 'subj_id','organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
    default_seq_dict = {}

    for name in fieldnames:
        default_seq_dict[name] = ''
    result_table = []

    print 'total pages: ', (n_pages + 1)
    for page in range(n_pages + 1):
        print 'page ', page
        seqs = session.query(Sequence).order_by('id').limit(heap_size).offset(heap_size*page).options(joinedload('query_blasthits'))
        for seq in seqs:
            if seq.organism == 'Perkinsela amoebae':
                seq_dict = default_seq_dict.copy()

                seq_dict['seqid'] = seq.seqid
                seq_dict['loc'] = seq.loc
                seq_dict['locrate'] = seq.locrate

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
                if ((seq_dict['evalue'] < 0.00001) and (seq_dict['rev_evalue'] < 0.01) and (seq_dict['alen_slen'] >= 0.3) and bsseq.mitochondrial) or (seq_dict['loc']=="M"):
                    result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath

def get_targetp_table(db_path, outpath, inlist):
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
    i = 0
    for seq in seqs:
        if seq.organism == 'Euglena gracilis' and seq.loc == 'M' and seq.locrate == 1 and seq.seqid not in inlist:
            i+=1
            print i

            seq_dict = default_seq_dict.copy()
            seq_dict['seqid'] = seq.seqid
            seq_dict['og'] = seq.og
            seq_dict['b2go_mito'] = seq.mitochondrial
            seq_dict['loc'] = seq.loc
            seq_dict['locrate'] = seq.locrate
            seq_dict['function'] = seq.function

            bs = seq.best_subject()
            if bs:
                bsseq = bs['sequence']
                seq_dict['subj_id'] = bsseq.seqid
                seq_dict['subj_og'] = bsseq.og
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
                    seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
            result_table.append(seq_dict)
            fieldnames = []
            default_seq_dict = {}
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath

def get_idlist_table(db_path, outpath, idlist):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    seqs = session.query(Sequence).filter(Sequence.seqid.in_(idlist)).all()
    fieldnames = ['seqid', 'og', 'b2go_mito', 'loc', 'locrate', 'function', 'subj_id', 'subj_og', 'organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
    default_seq_dict = {}
    for name in fieldnames:
        default_seq_dict[name] = ''
    result_table = []
    i = 0
    for seq in seqs:
        i+=1
        print i
        seq_dict = default_seq_dict.copy()
        seq_dict['seqid'] = seq.seqid
        seq_dict['og'] = seq.og
        seq_dict['b2go_mito'] = seq.mitochondrial
        seq_dict['loc'] = seq.loc
        seq_dict['locrate'] = seq.locrate
        seq_dict['function'] = seq.function

        bs = seq.best_subject()
        if bs:
            bsseq = bs['sequence']
            seq_dict['subj_id'] = bsseq.seqid
            seq_dict['subj_og'] = bsseq.og
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
                seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
        result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath

def get_id_table(db_path, outpath, id):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    seq = session.query(Sequence).filter(Sequence.seqid == id).one()
    query_blasthits = seq.query_blasthits
    subject_blasthits = seq.subject_blasthits
    result_table = []
    fieldnames = ['query_id', 'subject_id', 'evalue', 'length', 'alen_qlen', 'alen_slen', 'slen', 'qlen', 'pident']
    for bhs in query_blasthits, subject_blasthits:
        for bh in bhs:
            seq_dict = {}
            seq_dict['query_id'] = bh.query_id
            seq_dict['subject_id'] = bh.subject_id
            seq_dict['evalue'] = bh.evalue
            seq_dict['length'] = bh.length
            seq_dict['alen_qlen'] = bh.alen_qlen
            seq_dict['alen_slen'] = bh.alen_slen
            seq_dict['slen'] = bh.slen
            seq_dict['qlen'] = bh.qlen
            seq_dict['pident'] = bh.extra_data['pident']
            result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath


# db_path = 'sqlite:////home/anna/Dropbox/phd/mitoproteomes/db/perkinsela_mito.db'
db_path = 'sqlite:///home/anna/Dropbox/phd/mitoproteomes/db/mito_all.db'
# db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito1.db'
# db_path = 'sqlite:////home/nenarokova/db/hemistasia_mito.db'

outpath = '/home/anna/Dropbox/phd/mitoproteomes/euglena results/tryp_notin.csv'
# outpath = '/home/anna/Dropbox/phd/db/result_test.csv'
# outpath = '/home/nenarokova/db/result_hemistasia.csv'
# outpath = '/home/anna/Dropbox/phd/mitoproteomes/perkinsela_mito.csv'

id_list = ['EG_transcript_8715','EG_transcript_28800','EG_transcript_2406','EG_transcript_1067','EG_transcript_33059','EG_transcript_36207','EG_transcript_21432','EG_transcript_30305','EG_transcript_42748','EG_transcript_26134','EG_transcript_1284','EG_transcript_11675','EG_transcript_34054','EG_transcript_15107','EG_transcript_7639','EG_transcript_5071','EG_transcript_19610','EG_transcript_4136','EG_transcript_7684','EG_transcript_6652','EG_transcript_7639','EG_transcript_7639','EG_transcript_11675','EG_transcript_19324','EG_transcript_13396','EG_transcript_1431','EG_transcript_18060','EG_transcript_737','EG_transcript_763','EG_transcript_668','EG_transcript_12380','EG_transcript_23965','EG_transcript_4534','EG_transcript_3953','EG_transcript_9521','EG_transcript_13807','EG_transcript_10634','EG_transcript_24482','EG_transcript_3890','EG_transcript_10814','EG_transcript_2814','EG_transcript_22057','EG_transcript_5415','EG_transcript_668','EG_transcript_3096','EG_transcript_1783','EG_transcript_12086','EG_transcript_13673','EG_transcript_14855','EG_transcript_17479','EG_transcript_14010','EG_transcript_10562','EG_transcript_21219','EG_transcript_12166','EG_transcript_20567','EG_transcript_8362','EG_transcript_2901','EG_transcript_2505','EG_transcript_12260','EG_transcript_12260','EG_transcript_30283','EG_transcript_946','EG_transcript_53421','EG_transcript_9483','EG_transcript_8385','EG_transcript_18669','EG_transcript_48180','EG_transcript_8513','EG_transcript_35793','EG_transcript_34325','EG_transcript_7672','EG_transcript_12216','EG_transcript_23555','EG_transcript_9069','EG_transcript_310','EG_transcript_9483','EG_transcript_8722','EG_transcript_14193','EG_transcript_1740','EG_transcript_11675','EG_transcript_19390','EG_transcript_31840','EG_transcript_4750','EG_transcript_19007','EG_transcript_19007','EG_transcript_19007','EG_transcript_39447','EG_transcript_35830','EG_transcript_994','EG_transcript_8443','EG_transcript_16484','EG_transcript_925','EG_transcript_8320','EG_transcript_8319','EG_transcript_10128','EG_transcript_5534','EG_transcript_11375','EG_transcript_263','EG_transcript_12357','EG_transcript_23216','EG_transcript_7825','EG_transcript_22143','EG_transcript_293','EG_transcript_12376','EG_transcript_49190','EG_transcript_50867','EG_transcript_2007','EG_transcript_3304','EG_transcript_26209','EG_transcript_12621','EG_transcript_24958','EG_transcript_704','EG_transcript_10250','EG_transcript_12795','EG_transcript_4312','EG_transcript_41111','EG_transcript_10131','EG_transcript_6189','EG_transcript_51504','EG_transcript_15855','EG_transcript_10351','EG_transcript_20319','EG_transcript_16896','EG_transcript_181','EG_transcript_38453','EG_transcript_12332','EG_transcript_30936','EG_transcript_1161','EG_transcript_15240','EG_transcript_21996','EG_transcript_3806','EG_transcript_13724','EG_transcript_2593','EG_transcript_5327','EG_transcript_2040','EG_transcript_3914','EG_transcript_14503','EG_transcript_13174','EG_transcript_10242','EG_transcript_10242','EG_transcript_14805','EG_transcript_10463','EG_transcript_8907','EG_transcript_4298','EG_transcript_1101','EG_transcript_1330','EG_transcript_25593','EG_transcript_13577','EG_transcript_51563','EG_transcript_16560','EG_transcript_5719','EG_transcript_3289','EG_transcript_21460','EG_transcript_3655','EG_transcript_10972','EG_transcript_14239','EG_transcript_21060','EG_transcript_253','EG_transcript_43548','EG_transcript_3072','EG_transcript_4717','EG_transcript_3914','EG_transcript_41717','EG_transcript_10864','EG_transcript_5361','EG_transcript_30735','EG_transcript_5121','EG_transcript_8197','EG_transcript_3057','EG_transcript_24218','EG_transcript_29710','EG_transcript_5852','EG_transcript_10182','EG_transcript_10182','EG_transcript_5289','EG_transcript_13405','EG_transcript_4309','EG_transcript_2600','EG_transcript_12195','EG_transcript_20574','EG_transcript_11118','EG_transcript_451','EG_transcript_8425','EG_transcript_8425','EG_transcript_796','EG_transcript_8425','EG_transcript_20567','EG_transcript_12587','EG_transcript_15208','EG_transcript_9900','EG_transcript_24642','EG_transcript_39755','EG_transcript_4336','EG_transcript_3065','EG_transcript_13588','EG_transcript_21263','EG_transcript_2884','EG_transcript_6270','EG_transcript_33035','EG_transcript_7994','EG_transcript_7675','EG_transcript_5998','EG_transcript_5998','EG_transcript_9505','EG_transcript_8785','EG_transcript_5384','EG_transcript_25958','EG_transcript_11231','EG_transcript_16283','EG_transcript_6158','EG_transcript_6744','EG_transcript_1396','EG_transcript_2777','EG_transcript_2007','EG_transcript_19383','EG_transcript_13881','EG_transcript_19503','EG_transcript_19427','EG_transcript_29902','EG_transcript_1264','EG_transcript_10194','EG_transcript_10580','EG_transcript_10192','EG_transcript_50540','EG_transcript_28662','EG_transcript_668','EG_transcript_10194','EG_transcript_30891','EG_transcript_2978','EG_transcript_2600','EG_transcript_2600','EG_transcript_27910','EG_transcript_668','EG_transcript_3070','EG_transcript_5917','EG_transcript_9521','EG_transcript_6968','EG_transcript_17880','EG_transcript_5071','EG_transcript_2862','EG_transcript_19552','EG_transcript_52992','EG_transcript_27068','EG_transcript_23455','EG_transcript_12396','EG_transcript_19314','EG_transcript_1196','EG_transcript_19750','EG_transcript_32996','EG_transcript_7356','EG_transcript_27546','EG_transcript_15279','EG_transcript_13428','EG_transcript_12451','EG_transcript_26542','EG_transcript_26428','EG_transcript_22347','EG_transcript_19184','EG_transcript_21174','EG_transcript_43582','EG_transcript_15806','EG_transcript_9355','EG_transcript_26','EG_transcript_23666','EG_transcript_10194','EG_transcript_4771','EG_transcript_9957','EG_transcript_7826','EG_transcript_3890','EG_transcript_196','EG_transcript_2795','EG_transcript_19311','EG_transcript_13070','EG_transcript_22256','EG_transcript_16113','EG_transcript_3093','EG_transcript_28680','EG_transcript_12684','EG_transcript_20241','EG_transcript_35135','EG_transcript_10069','EG_transcript_13768','EG_transcript_4223','EG_transcript_30171','EG_transcript_52782','EG_transcript_5214','EG_transcript_62','EG_transcript_4309','EG_transcript_260','EG_transcript_3890','EG_transcript_19961','EG_transcript_17531','EG_transcript_24391','EG_transcript_8939','EG_transcript_1349','EG_transcript_5667','EG_transcript_10609','EG_transcript_25700','EG_transcript_13224','EG_transcript_13405','EG_transcript_39280','EG_transcript_20241','EG_transcript_9844','EG_transcript_10550','EG_transcript_421','EG_transcript_18163','EG_transcript_2393','EG_transcript_8676','EG_transcript_6492','EG_transcript_53416','EG_transcript_2300','EG_transcript_9456','EG_transcript_14239','EG_transcript_15060','EG_transcript_15548','EG_transcript_19390','EG_transcript_26284','EG_transcript_6432','EG_transcript_833','EG_transcript_20618','EG_transcript_1354','EG_transcript_29483','EG_transcript_18831','EG_transcript_5491','EG_transcript_52520','EG_transcript_16406','EG_transcript_5437','EG_transcript_2492','EG_transcript_2087','EG_transcript_7085','EG_transcript_52704','EG_transcript_21143','EG_transcript_16558','EG_transcript_11592','EG_transcript_29819','EG_transcript_29819','EG_transcript_1772','EG_transcript_3478','EG_transcript_18332','EG_transcript_10777','EG_transcript_33996','EG_transcript_44081','EG_transcript_4382','EG_transcript_7110','EG_transcript_9916','EG_transcript_26962','EG_transcript_15592','EG_transcript_2007','EG_transcript_1173','EG_transcript_29716','EG_transcript_5897','EG_transcript_25242','EG_transcript_3799','EG_transcript_26395','EG_transcript_20603','EG_transcript_10565','EG_transcript_1354','EG_transcript_8517','EG_transcript_18594','EG_transcript_10250','EG_transcript_7155','EG_transcript_10194','EG_transcript_19782','EG_transcript_9942','EG_transcript_49806','EG_transcript_29710','EG_transcript_12795','EG_transcript_5475','EG_transcript_6511','EG_transcript_7667','EG_transcript_26785','EG_transcript_16547','EG_transcript_10541','EG_transcript_908','EG_transcript_24996','EG_transcript_21268','EG_transcript_26790','EG_transcript_9781','EG_transcript_10393','EG_transcript_260','EG_transcript_7320','EG_transcript_21535','EG_transcript_26156','EG_transcript_994','EG_transcript_14405','EG_transcript_7630','EG_transcript_7999','EG_transcript_4390','EG_transcript_29299','EG_transcript_9355','EG_transcript_201','EG_transcript_20574','EG_transcript_60249','EG_transcript_6017','EG_transcript_11102','EG_transcript_15653','EG_transcript_8871','EG_transcript_3467','EG_transcript_11675','EG_transcript_8819','EG_transcript_18914','EG_transcript_15833','EG_transcript_976','EG_transcript_19324','EG_transcript_1099','EG_transcript_19427','EG_transcript_20545','EG_transcript_2232','EG_transcript_5230','EG_transcript_8425','EG_transcript_11772','EG_transcript_11927','EG_transcript_8425','EG_transcript_635','EG_transcript_40714','EG_transcript_37730','EG_transcript_13915','EG_transcript_11767','EG_transcript_661','EG_transcript_2280','EG_transcript_28802','EG_transcript_17851','EG_transcript_10182','EG_transcript_37022','EG_transcript_24218','EG_transcript_11579','EG_transcript_20732','EG_transcript_10851','EG_transcript_2393','EG_transcript_22816','EG_transcript_18272','EG_transcript_524','EG_transcript_9285','EG_transcript_10940','EG_transcript_6180','EG_transcript_13570','EG_transcript_3017','EG_transcript_253','EG_transcript_32266','EG_transcript_61646','EG_transcript_8132','EG_transcript_14769','EG_transcript_15687','EG_transcript_15687','EG_transcript_10397','EG_transcript_10397','EG_transcript_1975','EG_transcript_10412','EG_transcript_8672','EG_transcript_2624','EG_transcript_20956','EG_transcript_43303','EG_transcript_10463','EG_transcript_12653','EG_transcript_8047','EG_transcript_3497','EG_transcript_485','EG_transcript_2238']
get_idlist_table(db_path, outpath, idlist = id_list)
# get_result_table_perk(db_path, outpath)
