import sqlite3
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.raw_query_to_dict import *
from py_scripts.helpers.parse_csv import *

result_blasthits = '/home/anna/bioinformatics/phd/euglena_project/euglena/filtered_results.csv'
available_ids = []
is_first = True
for row in parse_csv(result_blasthits):
    if is_first:
        is_first = False
    else:
        available_ids.append(row[0])

db_path = "/home/anna/Dropbox/PhD/mitoproteome.db"

query = """
    SELECT seqid, function, loc, locrate
    FROM sequence
    WHERE organism = 'Euglena gracilis'
    AND mitoscore = 100
"""

rows = exe_query(query, db_path)

bad_function = 'double-stranded DNA binding;regulation of transcription'
result = []
for row in rows:
    if (bad_function not in row['function']) and (row['seqid'] not in available_ids):
        result.append(row)

outpath = '/home/anna/bioinformatics/phd/euglena_project/euglena/euglena_b2go_mito.csv'
write_list_of_dicts(result, outpath)
