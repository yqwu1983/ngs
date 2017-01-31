#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

def get_ogs_from_dict(csv_path, og_dicts, organism, outpath=False):
    print organism
    if not outpath: outpath = csv_path[0:-4] + '_ogs.csv'
    og_dict = og_dicts[organism]
    csv_list = csv_to_list_of_dicts(csv_path)[0]
    i = 0
    for og in og_dict:
        cur_ogs = [x.strip() for x in og_dict[og].rstrip(';').split(';')]
        if i%10000 == 0: print i
        i+=1
        for dic in csv_list:
            seqid = dic['seqid']
            if organism == 'Arabidopsis thaliana': seqid = seqid[0:-2]
            if seqid in cur_ogs:
                dic['og'] = og
    # fieldnames = ['seqid',  'function', 'mitochondrial']
    fieldnames = ['seqid','og','b2go_mito','loc','locrate','b2go function','subj_id','gene_name','alternative name','subj_og','organism','mitochondrial?','subj_function','Function','complex or function','evalue','alen_slen','pident','rev_evalue','rev_pident','rev_alen_qlen','is_best?','best_rev_evalue','best_rev_pident','pident_diff','same_og?','In Perkinsela?','Euglena (Perez et al.)','ortholog count (TriTrypDB v9)','paralog count (T.brucei; TriTrypDB v9)','references/comments','overall_score']
    write_list_of_dicts(csv_list, outpath, fieldnames)
    return 0

def get_homo_ogs(csv_path, og_dicts, ids_to_ccds_path, outpath=False):
    print 'Homo sapiens'
    if not outpath: outpath = csv_path[0:-4] + '_ogs.csv'
    og_dict = og_dicts['Homo sapiens']
    ids_to_ccds = csv_to_dict(ids_to_ccds_path, main_key='Entry')[0]
    csv_list = csv_to_list_of_dicts(csv_path)[0]
    i = 0
    for dic in csv_list:
        if i%100 == 0: print i
        i+=1
        seqid = dic['seqid']
        if seqid in ids_to_ccds.keys():
            ccds = [x.strip() for x in ids_to_ccds[seqid]['CCDS ID'].rstrip(';').split(';')]
            if len(ccds) == 0 or len(ccds[0])==0:
                dic['og'] = ''
            else:
                has_og = False
                for og in og_dict:
                    cur_ogs = [x.strip() for x in og_dict[og].rstrip(';').split(';')]
                    if og_dict[og]:
                        if has_og: break
                        for ccd in ccds:
                            for cur_og in cur_ogs:
                                if ccd == cur_og[0:-2]:
                                    dic['og'] = og
                                    has_og = True
                                    break
    fieldnames = ['seqid', 'og', 'function', 'mitochondrial']
    write_list_of_dicts(csv_list, outpath, fieldnames)
    return 0

def get_ogs(data_paths, og_path, ids_to_ccds_path):
    og_dicts = csv_to_dict_reverse(og_path)
    for organism in data_paths:
        if organism == 'Homo sapiens':
            get_homo_ogs(data_paths[organism], og_dicts, ids_to_ccds_path)
        else:
           get_ogs_from_dict(data_paths[organism], og_dicts, organism)


og_path = '/home/anna/Dropbox/PhD/bioinformatics/genomes/parsed_ortho_groups.csv'

data_paths = {
    'Arabidopsis thaliana': '/home/anna/Dropbox/PhD/bioinformatics/genomes/arabidopsis/data/arabidopsis_mito_ogs.csv,
    # 'Giardia intestinalis': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/giardia/data/giardia_mito.csv',
    # 'Euglena gracilis': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/data/euglena_all_proteins.csv',
    # 'Homo sapiens': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/homo/data/homo_mito.csv',
    # 'Saccharomyces cerevisiae': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/saccharomyces/data/yeast_mito.csv',
    # 'Trichomonas vaginalis': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trichomonas/data/trichomonas_mito.csv',
    # 'Trypanosoma brucei': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trypanosoma/data/trypanosoma_mito.csv'
        }

ids_to_ccds_path = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/homo/data/ids_to_ccds.csv'

get_ogs(data_paths, og_path, ids_to_ccds_path)
