#!/usr/bin/python
# db_types: 'nucl', 'prot'
# bl_types: 'blastn', 'blastp', 'psiblast', 'blastx', 'tblastn', 'tblastx'
from subprocess import call
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
sys.path.insert(0, "/home/nenarokova/ngs/")
from py_scripts.helpers.make_outdir import file_from_path, make_outdir, dir_from_path
# from py_scripts.bioscripts.convert import fastq_fasta
from os.path import exists
from os import makedirs

class Blast(object):
    def __init__(self, query_path=False, subj_path=False, ref_type='fasta', db_type=False, db_path=False, outdir=False, threads=8):
        self.subj_path = subj_path
        self.ref_type = ref_type
        if self.ref_type == 'fastq':
            self.subj_path = fastq_fasta(self.subj_path)
        self.db_type = db_type
        self.db_path = db_path
        self.query_path = query_path
        self.outdir = outdir
        self.threads = threads
        if not self.outdir and db_path:
            self.outdir = dir_from_path(db_path, lift=1)
        return None

    def makeblastdb(self):
        if not self.outdir:
            self.outdir = make_outdir(self.subj_path)
        db_folder = self.outdir + 'blast_db/'
        db_path = db_folder + file_from_path(self.subj_path, endcut=6) + '.db'
        make_blast_db = ['makeblastdb', '-in', self.subj_path, '-parse_seqids', '-dbtype', self.db_type, '-out', db_path]
        call(make_blast_db)
        return db_path

    formats = {
    'pairwise': {'#':'0', 'ext':'.txt'},
    'query_anchored_identities': {'#':'1', 'ext':'.txt'},
    'query_anchored_no_identities': {'#':'2', 'ext':'.txt'},
    'flat_query_anchored_identities': {'#':'3', 'ext':'.txt'},
    'flat_query_anchored_no_identities': {'#':'4', 'ext':'.txt'},
    'xml': {'#':'5', 'ext':'.xml'},
    'tabular': {'#':'6', 'ext':'.csv'},
    'tabular_comment_lines': {'#':'7', 'ext':'.txt'},
    'text_asn': {'#':'8', 'ext':'.txt'},
    'binary_asn': {'#':'9', 'ext':'.txt'},
    'comma_values': {'#':'10', 'ext':'.csv'},
    'blast_archive': {'#':'11', 'ext':'.txt'},
    }

    def blast(self, bl_type='blastn', outfmt='comma_values', custom_outfmt='False', word_size=False, blastn_short=False, evalue=10, outfile=False):
        if not self.query_path:
            sys.exit("Error: No query")

        self.custom_outfmt = custom_outfmt

        if not self.db_path:
            if not self.subj_path:
                sys.exit("Error: No subject")
            else:
                self.db_path = self.makeblastdb()

        query_name = file_from_path(self.query_path, endcut=6)

        blreports_dir = self.outdir + "blast_reports/"
        if not exists(blreports_dir):
            makedirs(blreports_dir)
        outfile = blreports_dir + str(query_name + "_bl_report" + self.formats[outfmt]['ext'])

        outfmt = self.formats[outfmt]['#']
        if custom_outfmt:
            outfmt = outfmt + " ' " + custom_outfmt + " ' "

        blast_call = [bl_type, '-query', self.query_path, '-db', self.db_path, '-out', outfile, '-outfmt', outfmt, '-num_threads', str(self.threads), '-evalue', str(evalue)]

        if word_size:
            blast_call.extend(['-word_size', str(word_size)])

        is_prot_bl_type = (bl_type in ['blastp', 'psiblast', 'blastx'])
        is_nucl_bl_type = (bl_type in ['blastn', 'tblastn'])

        if not ((is_nucl_bl_type and self.db_type == 'nucl') or (is_prot_bl_type and self.db_type == 'prot')):
            sys.exit('Error: Incompatible options')
            return False

        if blastn_short:
            if not (bl_type == 'blastn' and self.db_type == 'nucl'):
                sys.exit('Error: Incompatible options')
                return False
            else: blast_call.extend(['-task', 'blastn-short'])

        print 'Blast is running'
        print blast_call
        call(blast_call)
        self.bl_report = outfile
        return outfile
