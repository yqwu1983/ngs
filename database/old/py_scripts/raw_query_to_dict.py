import sqlite3
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
from py_scripts.helpers.parse_dicts import *

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
