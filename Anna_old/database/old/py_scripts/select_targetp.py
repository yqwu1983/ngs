import sqlite3
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.raw_query_to_dict import *
from py_scripts.helpers.parse_csv import *

db_path = "/home/anna/Dropbox/PhD/mitoproteome.db"
result_blasthits = '/home/anna/bioinformatics/phd/euglena_project/euglena/filtered_results.csv'

def get_available_ids(result_blasthits):
    available_ids = []
    is_first = True
    for row in parse_csv(result_blasthits):
        if is_first:
            is_first = False
        else:
            available_ids.append(row[0])
    return available_ids

def simple_query():
    query = """
        SELECT seqid, function, loc, locrate
        FROM sequence
        WHERE organism = 'Euglena gracilis'
        AND loc = 'M' AND locrate <= 1 AND mitoscore <> 100
    """

    rows = exe_query(query, db_path)

    available_ids = get_available_ids(result_blasthits)
    result = []
    for row in rows:
        if row['seqid'] not in available_ids:
            result.append(row)

    outpath = '/home/anna/bioinformatics/phd/euglena_project/euglena/euglena_targetp_mito.csv'
    write_list_of_dicts(result, outpath)
    return 0

def select_best_hit(blasthit_dict, available_ids):
    needed_keys = [
    "query_id",
    "query_function",
    "query_mitoscore",
    "query_loc",
    "query_locrate",
    "subject_id",
    "subject_organism",
    "subject_function",
    "subject_loc",
    "subject_locrate",
    "evalue",
    "qlen",
    "slen",
    "length",
    "alen_slen",
    "alen_qlen"
    ]

    csv_list = []
    for query in blasthit_dict:
        if 'evalue' in blasthit_dict[query][0].keys():
            blasthits = sorted(blasthit_dict[query], key=lambda blasthit: float(blasthit['evalue']))
            is_first = True
        else:
            best_row = []
            for key in needed_keys:
                print len(blasthit_dict[query])
                print blasthit_dict[query]
                if key in blasthit_dict[query].keys():
                    best_row.append(blasthit[key])
                else:
                    best_row.append('')
        result = []
    if best_row[0] not in available_ids:
        csv_list.append(best_row)
    return csv_list


query = """
    SELECT *,
        query.seqid as query_id,
        subject.seqid as subject_id,
        query.function as query_function,
        subject.function as subject_function,
        query.loc as query_loc,
        subject.loc as subject_loc,
        query.locrate as query_locrate,
        subject.locrate as subject_locrate,
        query.mitoscore as query_mitoscore,
        subject.organism as subject_organism
    FROM sequence query
    LEFT JOIN blasthit ON blasthit.query_id = query.id
    INNER JOIN sequence AS subject ON subject.id = blasthit.subject_id
    WHERE query.organism = 'Euglena gracilis' AND query.loc = 'M' AND query.locrate <= 2 AND query.mitoscore = 100
"""

query = """
    SELECT
        query.seqid as query_id,
        subject.seqid as subject_id,
        evalue
    FROM sequence query
    LEFT JOIN blasthit ON blasthit.query_id = query.id
    INNER JOIN sequence AS subject ON subject.id = blasthit.subject_id
    WHERE query.organism = 'Euglena gracilis' AND query.mitoscore == 100
"""

# rows = exe_query(query, db_path)
# blasthit_dict = dict_list_to_dict(rows, 'query_id')
# for query in blasthit_dict:
#     print query, blasthit_dict[query]
#     print '\n'
# result = select_best_hit(blasthit_dict, available_ids)
# print result
# outpath = '/home/anna/bioinformatics/phd/euglena_project/euglena/euglena_targetp_mito.csv'

simple_query()
