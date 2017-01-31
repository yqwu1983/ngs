#!/usr/bin/python
import sqlite3
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.raw_query_to_dict import *
from py_scripts.helpers.parse_csv import *

db_path = "/home/anna/Dropbox/PhD/mitoproteome.db"

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
    INNER JOIN blasthit ON blasthit.query_id = query.id
    INNER JOIN sequence AS subject ON subject.id = blasthit.subject_id
    WHERE query.organism = 'Euglena gracilis'

    AND subject.seqid in ("Tb927.11.7900", "Tb927.11.8400","Tb927.11.1710","Tb927.11.13280","Tb927.9.4360","Tb927.1.3030","Tb927.1.1690","Tb927.10.5440","Tb927.10.5320","Tb927.2.2470","Tb927.10.8210","Tb927.8.620","Tb927.10.5110","Tb927.8.680","Tb927.10.5120","Tb927.11.2990","Tb927.11.940","Tb927.3.3990","Tb927.9.5630","Tb927.8.5690","Tb927.7.3950","Tb927.7.1550","Tb927.7.1070","Tb927.10.3570","Tb927.1.1330","Tb927.11.8870","Tb927.4.1500","Tb11.02.5390","Tb927.11.16860","Tb927.11.9140","Tb927.6.1680","Tb927.4.4150","Tb927.8.8180","Tb927.8.8170","Tb927.6.2230","Tb927.2.1860","Tb927.4.4160","Tb927.10.10830","Tb927.7.2570","Tb927.10.11870","Tb927.5.3010","Tb927.3.1590","Tb927.2.6070","Tb927.3.1820","Tb927.7.800","Tb927.2.3800","Tb927.10.380","Tb927.11.15850","Tb927.2.3180","Tb927.11.14380")
    GROUP BY subject.seqid
"""
needed_keys = [
        "query_id",
        "query_function",
        "query_mitoscore",
        "query_loc",
        "query_locrate",
        "subject_id",
        "subject_organism",
        "subject_function",
        "evalue",
        "qlen",
        "slen",
        "length",
        "alen_slen",
        "alen_qlen"
    ]

# rows = exe_query(query, db_path)
# query_dict = dict_list_to_dict(rows, 'query_id')

# print len(query_dict)

# results = {}

# for query in query_dict:
#     results[query] = sorted(query_dict[query], key=lambda blasthit: float(blasthit['evalue']))

# print len(results)
# print ''

# csv_list = []
# i=0
# for query in results:
#     for blasthit in results[query]:
#         row = []
#         for key in needed_keys:
#             row.append(blasthit[key])
#         csv_list.append(row)
#         i+=1

# print i

# outfile = '/home/anna/bioinformatics/euglena_project/euglena/editing_proteins.csv'
# write_list_of_lists(csv_list, outfile, delimiter=',', header=needed_keys)

common_query = """
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
    INNER JOIN blasthit ON blasthit.query_id = query.id
    INNER JOIN sequence AS subject ON subject.id = blasthit.subject_id
    WHERE query.organism = 'Euglena gracilis'
    AND blasthit.evalue < 0.00001 AND blasthit.alen_slen > 0.3
    AND subject.seqid = """

editing_ids = ("Tb927.11.7900", "Tb927.11.8400","Tb927.11.1710","Tb927.11.13280","Tb927.9.4360","Tb927.1.3030","Tb927.1.1690","Tb927.10.5440","Tb927.10.5320","Tb927.2.2470","Tb927.10.8210","Tb927.8.620","Tb927.10.5110","Tb927.8.680","Tb927.10.5120","Tb927.11.2990","Tb927.11.940","Tb927.3.3990","Tb927.9.5630","Tb927.8.5690","Tb927.7.3950","Tb927.7.1550","Tb927.7.1070","Tb927.10.3570","Tb927.1.1330","Tb927.11.8870","Tb927.4.1500","Tb11.02.5390","Tb927.11.16860","Tb927.11.9140","Tb927.6.1680","Tb927.4.4150","Tb927.8.8180","Tb927.8.8170","Tb927.6.2230","Tb927.2.1860","Tb927.4.4160","Tb927.10.10830","Tb927.7.2570","Tb927.10.11870","Tb927.5.3010","Tb927.3.1590","Tb927.2.6070","Tb927.3.1820","Tb927.7.800","Tb927.2.3800","Tb927.10.380","Tb927.11.15850","Tb927.2.3180","Tb927.11.14380")


csv_list = []
for seqid in editing_ids:
    query = common_query + '"' + seqid + '"'
    blasthits = exe_query(query, db_path)
    blasthits = sorted(blasthits, key=lambda blasthit: float(blasthit['evalue']))
    if len(blasthits) > 0:
        row = [seqid, len(blasthits)]
        for key in needed_keys:
            row.append(blasthits[0][key])
        csv_list.append(row)

outfile = '/home/anna/bioinformatics/phd/euglena_project/euglena/editing_proteins_results.csv'

header = ['seqid', 'blasthits_number']
header.extend(needed_keys)
write_list_of_lists(csv_list, outfile, delimiter=',', header=header)
