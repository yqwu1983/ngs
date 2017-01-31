#!/usr/bin/python
import sqlite3
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.raw_query_to_dict import *
from py_scripts.helpers.parse_csv import *

def select_best_hit(blasthit_dict, needed_keys):
    csv_list = []
    function_list = []

    for query in blasthit_dict:
        is_first = True
        for blasthit in blasthit_dict[query]:
            row = []
            for key in needed_keys:
                row.append(blasthit[key])

            if is_first == True:
                best_row = row
                is_first = False

            is_best = True
            non_specific_functions = [
                     # 'hypothetical',
                     # 'protein of unknown function',
                     # 'parkinson',
                     # 'putative protein',
                     # 'unspecified product',
                     # 'circadian clock',
                     # 'insulin',
                     # 'crystallin',
                     # 'carcinoma',
                     # 'tumor',
                     # 'death',
                     # 'apoptosis',
                     # 'chromosome',
                     # 'growth',
                     # 'heat',
                     # 'prostaglandin',
                     # 'zinc'
                     ]
            for function in non_specific_functions:
                if function in blasthit['function']:
                    is_best = False

            if is_best == True:
                best_row = row
                break

        csv_list.append(best_row)
        function_list.append(best_row[7])

    return csv_list, function_list

def filter_euglena_blasthits(db_path):
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
        AND blasthit.evalue < 0.00001 AND blasthit.alen_slen > 0.3
        AND ( subject.organism = 'Trypanosoma brucei'
            OR  subject.organism = 'Homo sapiens'
            OR (subject.organism = 'Saccharomyces cerevisiae' AND subject.mitoscore = 100))
    """

    rows = exe_query(query, db_path)
    query_dict = dict_list_to_dict(rows, 'query_id')

    bad_functions = [
                     'dynein', 'kinesin', 'tubulin', 'actin', 'myosin', 'formin',
                     'clathrin', 'centrin',
                     'cytosolic coat',
                     'paraflagellar rod component; putative',
                     'williams-beuren',
                     'transposon', 'repeat',
                     'mterf',
                     'small gtp-binding protein rab',
                     'ribosome-associated gtpase ',
                     'ras-like small gtpase',
                     'kinase',
                     'phosphatase',
                     'adenylate cyclase',
                     'adp-ribosylation',
                     'macro domain',
                     'sirtuin',
                     'calmodulin',
                     'angel',
                     'cyclophilin',
                     'insulin-recepror',
                     # 'disulphide',
                     'mrp', 'abc', 'transloc', 'permease', 'atp-binding cassette', 'porter',
                     'regulator of microtubule dynamics',
                     'required for meiotic nuclear division 1 homolog',
                     'gtpase-activating protein',
                     'vesicle membrane protein',
                     'universal minicircle sequence binding protein',
                     'lactamase',
                     'pump',
                     'endosomal integral membrane protein; putative',
                     'stomatin',
                     'chaperon', 'chaperonin',
                     'histon', 'dnaj', 'nucleosome remodeling',
                     'component of the condensin complex',
                     'peptidas', 'protease',
                     'proteasome',
                     'ubiquitin',
                     'dead', 'deah',
                     'rna binding',
                     'poly(a)',
                     'helicase',
                     'ligase',
                     'polymerase',
                     'nuclease',
                     'topoisomerase',
                     'photolyase',
                     'muts', 'mutl',
                     'mrb1-',
                     'kiaa0141'
                     ]

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

    results = {}

    for query in query_dict:
        function_is_good = True
        for hit in query_dict[query]:
            if function_is_good:
                for function in bad_functions:
                    if (function.lower() in hit['subject_function'].lower()) and (query_dict[query][0]['query_loc'] != 'M'):
                        function_is_good = False
                        break
        if function_is_good:
            results[query] = sorted(query_dict[query], key=lambda blasthit: float(blasthit['evalue']))

    print len(results), 'proteins'

    csv_list = []
    i=0
    for query in results:
        for blasthit in results[query]:
            row = []
            for key in needed_keys:
                row.append(blasthit[key])
            csv_list.append(row)
            i+=1
        csv_list.append([])

    csv_list, function_list = select_best_hit(results, needed_keys)
    function_set = set(function_list)
    print len(function_set), 'functions'

    outfile = '/home/anna/bioinformatics/phd/euglena_project/euglena/filtered_results.csv'
    write_list_of_lists(csv_list, outfile, delimiter=',', header=needed_keys)

    csv_list_functions = []

    for function in function_set:
        csv_list_functions.append([function])

    outfile = '/home/anna/bioinformatics/phd/euglena_project/euglena/filtered_set_of_functions.csv'
    write_list_of_lists(csv_list_functions, outfile, delimiter=',')

    # i=0
    # for key in results:
    #     if i<500:
    #         # print key
    #         for blasthit in results[key]:
    #             for k in blasthit.keys():
    #                 print k
    #             exit(0)
    #             print blasthit['subject_function']
    #         print ''
    #     i+=1
    return 0

db_path = "/home/anna/Dropbox/PhD/mitoproteome.db"

filter_euglena_blasthits(db_path)
