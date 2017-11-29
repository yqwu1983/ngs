#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_data.load_seq import *
from database.alchemy.load_data.load_bh import *
from database.alchemy.load_data.update_db import *

def reload_db(db_path, data_paths=False, load_description=True, blast_csv_paths=False, blast_outfmt=False, reload_seq=True, reload_bh=True, targetp_csv_path=False, check_functions=True, exact_ids=True, load_only_functions=False, organism=False):
    engine = create_engine(db_path)
    if reload_seq: Sequence.__table__.drop(engine, checkfirst=True)
    if reload_bh: BlastHit.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if reload_seq:
        for organism in data_paths:
            fasta_path=data_paths[organism]['fasta_path']
            seqtype = data_paths[organism]['seqtype']
            if load_description and ('description_path' in data_paths[organism]):
                description_path=data_paths[organism]['description_path']
                load_fasta(session, fasta_path=fasta_path, seqtype=seqtype, organism=organism, description_path=description_path)
            else:
                load_fasta(session, fasta_path=fasta_path, seqtype=seqtype, organism=organism)
    if reload_bh:
        for blast_csv_path in blast_csv_paths:
            print blast_csv_path, 'is loading'
            load_blast_csv(session, blast_csv_path, custom_outfmt=blast_outfmt)
    if targetp_csv_path:
        load_targetp(session, targetp_csv_path, exact_ids=exact_ids, organism=organism)
    if load_only_functions:
        for organism in data_paths:
            if 'description_path' in data_paths[organism]:
                load_functions(session, data_paths[organism]['description_path'], exact_ids=True, organism=organism)

    return 0

# db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'
db_path = 'sqlite:////home/anna/Dropbox/phd/mitoproteomes/db/perkinsela_mito.db'

# data_paths = {
#     'Arabidopsis thaliana': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis_mito_ogs.csv', 'seqtype': 'prot'},
#     'Euglena gracilis': {'fasta_path':'/home/anna/Dropbox/phd/db/proteomes/euglena/data/euglena_all_proteins.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/euglena/data/euglena_all_proteins_ogs.csv', 'seqtype': 'prot'},
#     'Giardia intestinalis': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito_ogs.csv', 'seqtype': 'prot'},
#     'Homo sapiens': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/homo/data/homo_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/homo/data/homo_mito_ogs.csv', 'seqtype': 'prot'},
#     'Saccharomyces cerevisiae': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito_ogs.csv', 'seqtype': 'prot'},
#     'Trichomonas vaginalis': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas_mito_ogs.csv', 'seqtype': 'prot'},
#     'Trypanosoma brucei': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/trypanosoma/data/trypanosoma_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/trypanosoma/data/trypanosoma_mito_ogs.csv', 'seqtype': 'prot'}
#                 }

data_paths = {
    'Arabidopsis thaliana': {'fasta_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/arabidopsis/data/arabidopsis.fasta', 'description_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/arabidopsis/data/arabidopsis_mito_ogs.csv', 'seqtype': 'prot'},
    'Giardia intestinalis': {'fasta_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/giardia/data/giardia.fasta', 'description_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/giardia/data/giardia_mito_ogs.csv', 'seqtype': 'prot'},
    'Homo sapiens': {'fasta_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/homo/data/homo.fasta', 'description_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/homo/data/homo_mito_ogs.csv', 'seqtype': 'prot'},
    'Saccharomyces cerevisiae': {'fasta_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/saccharomyces/data/yeast.fasta', 'description_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/saccharomyces/data/yeast_mito_ogs.csv', 'seqtype': 'prot'},
    'Trichomonas vaginalis': {'fasta_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trichomonas/data/trichomonas.fasta', 'description_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trichomonas/data/trichomonas_mito_ogs.csv', 'seqtype': 'prot'},
    'Trypanosoma brucei': {'fasta_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trypanosoma/data/trypanosoma.fasta', 'description_path': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trypanosoma/data/trypanosoma_mito_ogs.csv', 'seqtype': 'prot'},
    'Perkinsela amoebae': {'fasta_path':'/home/anna/Dropbox/phd/mitoproteomes/proteomes/perkinsela/perkinsela_prot.fasta', 'seqtype':'prot'}
                }

targetp_csv_path = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/perkinsela/perkinsela_prot_targetp_out.csv'

blast_csv_paths = [
'/home/anna/Dropbox/phd/mitoproteomes/proteomes/perkinsela/perkinsela_prot/blast_reports/reference_proteomes_bl_report.csv',
'/home/anna/Dropbox/phd/mitoproteomes/proteomes/reference_proteomes/reference_proteomes/blast_reports/perkinsela_prot_bl_report.csv'
]

blast_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

reload_db(db_path, data_paths=data_paths, reload_seq=False, reload_bh=False, blast_csv_paths=blast_csv_paths, targetp_csv_path=targetp_csv_path, exact_ids=False, organism='Perkinsela amoebae')