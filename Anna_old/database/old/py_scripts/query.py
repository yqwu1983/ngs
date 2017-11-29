#!/usr/bin/python
from peewee import *
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.models import *

i=0


# q = Sequence.select(Sequence, BlastHit).join(BlastHit, on=(BlastHit.query_id == Sequence.id).where
#         (BlastHit.evalue == 0)
#                                     )


# q = Sequence.select(Sequence).where(
#         (Sequence.organism == 'Euglena gracilis') &
#         (Sequence.mitoscore == 100)
#                                     )


raw_qs = "select * from sequence where organism = 'Euglena gracilis' and mitoscore=100"

raw_qs = """
select count(*) from
(select * from sequence query
inner join blasthit on blasthit.query_id = query.id
inner join sequence as subject on blasthit.subject_id = subject.id
where query.organism = 'Euglena gracilis' and subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100
    and blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3
group by query.id) as count_table;
"""
cursor = db.execute_sql(raw_qs)
tuples = cursor.fetchall()
# rq = Sequence.raw(raw_qs)

print tuples[0][0]

