#!/usr/bin/python
from peewee import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import *
import simplejson as json
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
from py_scripts.helpers.make_outdir import *

db_path = '/home/anna/Dropbox/PhD/mitoproteome.db'
db = SqliteDatabase(db_path)

class SerializedDictField(TextField):
    def db_value(self, value):
        if value == None: return None
        else: return json.dumps(value)

    def python_value(self, value):
        if value == None: return None
        else: return json.loads(value)

class BaseModel(Model):
    class Meta:
        database = db
    extra_data = SerializedDictField(null=True)

class Sequence(BaseModel):
    seqid = CharField()
    seqtype = CharField()
    organism = CharField()
    source = CharField()
    function = TextField(null=True)
    mitoscore = FloatField(null=True)
    loc = CharField(null=True)
    locrate = IntegerField(null=True)

    @staticmethod
    def read_from_f(fasta_path, seqtype, organism='unknown organism', source=False, info_dict=False):
        with db.atomic():
            for record in SeqIO.parse(fasta_path, "fasta"):
                seqid = record.id
                if not source: source = file_from_path(fasta_path, endcut=6)
                new_seq = Sequence(seqid=seqid, seqtype=seqtype, organism=organism, source=source, extra_data={},
                                loc=None, locrate=None, function=None, mitoscore=None)
                new_seq.extra_data['sequence'] = str(record.seq)
                new_seq.extra_data['description'] = str(record.description)
                if info_dict and (seqid in info_dict.keys()):
                    new_seq.function = info_dict[seqid]['function']
                    new_seq.mitoscore = float(info_dict[seqid]['mitoscore'])
                    new_seq.loc = info_dict[seqid]['loc']
                    new_seq.locrate = int(info_dict[seqid]['locrate'])
                    for key in info_dict[seqid]:
                        if key not in ['function', 'mitoscore', 'loc', 'locrate']:
                            new_seq.extra_data[key] = info_dict[seqid][key]
                new_seq.save()

    def to_seqrecord(self):
        if self.seqtype =='dna': alphabet = 'generic_dna'
        elif self.seqtype == 'protein': alphabet = 'generic_protein'
        else:
            print 'Error: Unsupported sequence type'
            return False
        seqrecord = SeqRecord(Seq(self.extra_data['sequence'], alphabet), name='', id = self.seqid, description = '')
        return seqrecord

class BlastHit(BaseModel):
    query = ForeignKeyField(Sequence, related_name='query_hits')
    subject = ForeignKeyField(Sequence, related_name='subject_hits')
    evalue = FloatField()
    length = IntegerField()
    alen_qlen = FloatField()
    alen_slen = FloatField()
    slen = FloatField()
    qlen = FloatField()

    @staticmethod
    def create_from_dicts(blast_dicts):
        with db.atomic():
            for blast_dict in blast_dicts:
                query_id, subject_id = blast_dict['qseqid'], blast_dict['sseqid']
                evalue, length = blast_dict['evalue'], blast_dict['length']
                qlen, slen = blast_dict['qlen'], blast_dict['slen']
                alen_qlen, alen_slen = float(length/float(qlen)), float(length/float(slen))
                other_features = {}
                for feature in blast_dict:
                    if feature not in ['qseqid', 'sseqid', 'evalue', 'length']:
                        other_features[feature] = blast_dict[feature]

                query = Sequence.select().where(Sequence.seqid == query_id).get()
                subject = Sequence.select().where(Sequence.seqid == subject_id).get()
                BlastHit.create(query=query, subject=subject, evalue=evalue, length=length,
                                qlen=qlen, slen=slen, alen_qlen=alen_qlen, alen_slen=alen_slen,
                                extra_data=other_features)
