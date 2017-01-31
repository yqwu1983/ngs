#!/usr/bin/python
from peewee import *
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.models import *
from py_scripts.helpers.parse_csv import *
import csv

def exclude_bad_functions():
    bad_functions = ['dynein', 'kinesin', 'tubulin', 'actin', 'myosin',
                 'clathrin', 'centrin',
                 'retrotransposon', 'repeat',
                 'mterf',
                 'ras',
                 'rab',
                 'kinase',
                 'phosphatase',
                 'adp-ribosylation',
                 'receptor',
                 'calmodulin',
                 'cyclophilin',
                 'transporter', 'transport', 'carrier', 'translocase', 'translocator', 'ABC',
                 'pump',
                 'chaperon', 'chaperonin',
                 'histone', 'dnaj',
                 'peptidase', 'protease',
                 'proteasome',
                 'ubiquitin',
                 'leucine-rich',
                 'dead', 'deah',
                 'williams-beuren',
                 'heat shock',
                 'zinc-finger', 'zinc finger',
                 'multidrug resistance protein',
                 ]

    functions = " "
    for word in bad_functions:
        not_like = "and" + " lower(subject.function)" + "not like" + " '%" + word + "%'\n"
        functions += not_like

    return functions

def make_count_query(features, verbose=False):
    count_on_blasthits = """
    select count(*) from
    (select * from sequence query
    inner join blasthit on blasthit.query_id = query.id
    inner join sequence as subject on blasthit.subject_id = subject.id
    where query.organism = 'Euglena gracilis'
    """
    group_by_query = " group by query.id) "

    raw_query = count_on_blasthits + features + group_by_query
    if verbose: print raw_query

    cursor = db.execute_sql(raw_query)
    tuples = cursor.fetchall()
    return tuples[0][0]

def make_select_query(features):
    select_on_blasthits = """
    select * from sequence query
    inner join blasthit on blasthit.query_id = query.id
    inner join sequence as subject on blasthit.subject_id = subject.id
    where query.organism = 'Euglena gracilis'
    """
    group_by_query = " group by query.id "
    group_by_function = " group by subject.function "
    raw_query = select_on_blasthits + features + group_by_function
    results = Sequence.raw(raw_query)
    return results

count_euglena = "select count(*) from sequence where query.organism = 'Euglena gracilis'"

tripa = " subject.organism = 'Tripanosoma brucei' "
homo = " subject.organism = 'Homo sapiens' "
yeast_mito = " (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100) "

blast_threshold = " (blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.5) "

functions = exclude_bad_functions()

organisms = [
 "(" + homo + ")",
 "(" + tripa + ")",
 "(" + yeast_mito + ")",
 "(" + homo + "or" + tripa + "or" + yeast_mito + ")",
 "(" + homo + "or" + tripa + ")",
 "(" + tripa + "or" + yeast_mito + ")",
 "(" + homo + "or" + yeast_mito + ")"
  ]


# for organism in organisms:
#     features = "and" + organism + functions + "and" + blast_threshold
#     # print organism
#     print make_count_query(features)

organism = " and " + "(" + homo + "or" + tripa + "or" + yeast_mito + ")"

other_features = [
" and " + " query.loc!='M' " + "and" + " query.mitoscore!=100 ",
" and " + " query.loc!='M' " + "and" + " query.mitoscore=100 ",
" and " + " query.loc='M' "  + "and" + " query.locrate> 2 " + "and" + " query.mitoscore=100 " ,
" and " + " query.loc='M' "  + "and" + " query.locrate<=2 " + "and" + " query.mitoscore=100 " ,
" and " + " query.loc='M' "  + "and" + " query.locrate<=2 " + "and" + " query.mitoscore!=100 " ,
" and " + " query.loc='M' "  + "and" + " query.locrate> 2 " + "and" + " query.mitoscore!=100 "
]

# for other_feature in other_features:
#     features = organism + other_feature + functions + "and" + blast_threshold
#     # print other_feature
#     print make_count_query(features)


organism = "(" + homo + "or" + tripa + "or" + yeast_mito + ")"
features = "and" + organism + functions + "and" + blast_threshold
print make_count_query(features)

seqs = make_select_query(features)

csv_out = []

for seq in seqs:
    csv_out.append([seq.organism, seq.seqid, seq.function, seq.mitoscore, seq.loc, seq.locrate])

csv_out = sorted(csv_out, key=lambda protein: protein[2])

outfile = '/home/anna/bioinformatics/phd/euglena_project/euglena/filtered_functions.csv'

header = ['organism', 'seqid', 'function', 'mitoscore', 'loc', 'locrate']

write_list_of_lists(csv_out, outfile, header=header)
