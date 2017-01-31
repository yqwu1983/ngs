import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, Boolean
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy.types as types
import simplejson as json
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import *

Base = declarative_base()

class SerializedDictField(types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect):
        if value == None: return None
        else: return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value == None: return None
        else: return json.loads(value)

class Sequence(Base):
    __tablename__ = 'sequence'

    id = Column(Integer, primary_key=True)
    seqid = Column(String(255), nullable=False, index=True, unique=True)
    seqtype = Column(String(255), nullable=False)
    organism = Column(String(255), nullable=False)
    len = Column(Integer(), nullable=False)
    source = Column(String(255))
    og = Column(String(255))
    function = Column(Text())
    mitochondrial = Column(Boolean())
    mitoscore = Column(Float())
    loc = Column(String(255))
    locrate = Column(Integer())
    extra_data = Column(SerializedDictField())

    query_blasthits = relationship("BlastHit", foreign_keys="BlastHit.query_id")
    subject_blasthits = relationship("BlastHit", foreign_keys="BlastHit.subject_id")

    queries = relationship('Sequence', secondary='blasthit',
        primaryjoin=("Sequence.id == BlastHit.subject_id"),
        secondaryjoin=("Sequence.id == BlastHit.query_id"))

    subjects = relationship('Sequence', secondary='blasthit',
        primaryjoin=("Sequence.id == BlastHit.query_id"),
        secondaryjoin=("Sequence.id == BlastHit.subject_id"))

    def to_seqrecord(self):
        if self.seqtype =='dna': alphabet = 'generic_dna'
        elif self.seqtype == 'prot': alphabet = 'generic_protein'
        else:
            print 'Error: Unsupported sequence type'
            return False
        seqrecord = SeqRecord(Seq(self.extra_data['sequence'], alphabet), name='', id = self.seqid, description = '')
        return seqrecord

    def best_subject_hit(self):
        hits = []
        for hit in self.query_blasthits:
            mode = 'slen' if self.organism == 'Euglena gracilis' else 'qlen'
            if hit.long_homology(mode):
                hits.append(hit)

        if len(hits) == 0:
            hits = self.query_blasthits

        hits = sorted(hits, key = lambda h: h.evalue)
        return hits[0] if hits else None

    def best_subject(self):
        bsh = self.best_subject_hit()
        return {'sequence': bsh.subject, 'hit': bsh} if bsh else None

    def get_reverse_blasthit(self, subject):
        session = Session.object_session(self)
        all_hits = subject.query_blasthits
        hits = []
        for hit in all_hits:
            if hit.subject_id == self.id:
                hits.append(hit)

        hits = sorted(hits, key = lambda h: h.evalue)
        if len(hits) > 0:
            hit = hits[0]
            bs = subject.best_subject()
            bss = bs['sequence']
            bsh = bs['hit']
        else:
            return None

        if hit:
            if self.id == bss.id:
                return {'hit': hit, 'is_best': True, 'bsh': bsh}
            else:
                return {'hit': hit, 'is_best': False, 'bsh': bsh}

class BlastHit(Base):
    __tablename__ = 'blasthit'

    id = Column(Integer, primary_key=True)
    evalue = Column(Float(), nullable=False)
    length = Column(Integer(), nullable=False)
    alen_qlen = Column(Float(), nullable=False)
    alen_slen = Column(Float(), nullable=False)
    slen = Column(Float(), nullable=False)
    qlen = Column(Float(), nullable=False)
    # pident = Column(Float(), nullable=False)
    extra_data = Column(SerializedDictField())

    query_id = Column(Integer, ForeignKey("sequence.id"))
    query = relationship("Sequence", primaryjoin=(query_id == Sequence.id))

    subject_id = Column(Integer, ForeignKey("sequence.id"))
    subject = relationship("Sequence", primaryjoin=(subject_id == Sequence.id))

    def long_homology(self, mode, len_percent = 0.3):
        if mode == "slen":
            return self.alen_slen >= len_percent
        elif mode == "qlen":
            return self.alen_qlen >= len_percent

    @staticmethod
    def get_by_query_subject(session, query_id, subject_id):
        return session.query(BlastHit) \
            .filter(BlastHit.query_id == query_id) \
            .filter(BlastHit.subject_id == subject_id)
