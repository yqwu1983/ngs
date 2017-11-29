import sqlite3
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
from py_scripts.helpers.parse_dicts import *
import csv

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def exe_query(query, db_path):
    con = sqlite3.connect(db_path)
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    rows = []
    for row in cur:
        rows.append(row)
    return rows

db_path = "/home/anna/Dropbox/PhD/mitoproteome.db"

query = """
    SELECT *,
        query.id as query_id,
        subject.id as subject_id,
        query.function as query_function,
        subject.function as subject_function
    FROM sequence query
    INNER JOIN blasthit ON blasthit.query_id = query.id
    INNER JOIN sequence AS subject ON subject.id = blasthit.subject_id
    WHERE query.organism = 'Euglena gracilis'
    AND blasthit.evalue < 0.00001 AND blasthit.alen_slen > 0.3
    AND (subject.organism = 'Tripanosoma brucei'
        OR  subject.organism = 'Homo sapiens'
        OR (subject.organism = 'Saccharomyces cerevisiae' AND subject.mitoscore = 100))
"""

rows = exe_query(query, db_path)
 = dict_list_to_dict(rows, 'query_id')

very_bad_functions =
                ['dynein', 'kinesin', 'tubulin', 'actin', 'myosin',
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
                 'transporter', 'transport', 'carrier', 'transloc', 'ABC',
                 'pump',
                 'chaperon', 'chaperonin',
                 'histone', 'dnaj',
                 'peptidase', 'protease',
                 'proteasome',
                 'ubiquitin',
                 'leucine-rich',
                 'dead', 'deah',
                 'williams-beuren',
                 ]

bad_functions = [
                 'heat',
                 'zinc-finger', 'zinc finger',
                 'multidrug resistance protein',
                 'binding',
                 'hypothetical',
                 'protein of unknown function',
                 'putative protein',
                 'unspecified product'
                 ]
