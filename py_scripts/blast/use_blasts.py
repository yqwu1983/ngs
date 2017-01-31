#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

query_paths = {
# 'arabidopsis': '/home/anna/bioinformatics/phd/mitoproteomes/arabidopsis/arabidopsis_mito.fasta',
# 'worm': '/home/anna/bioinformatics/phd/mitoproteomes/caenorhabditis/worm_mitoproteins.fasta',
# 'mouse' : '/home/anna/bioinformatics/phd/mitoproteomes/mitocarta/Mouse.MitoCarta2.0.fasta',
# 'human': '/home/anna/bioinformatics/phd/mitoproteomes/mitocarta/Human.MitoCarta2.0.fasta',
# 'yeast' : '/home/anna/bioinformatics/phd/mitoproteomes/yeast/orf_trans_all.fasta',
# 'tetrahymena': '/home/anna/bioinformatics/phd/mitoproteomes/tetrahymena/tetrahymena_mito_gb.fasta',
# 'trypanosoma' : '/home/anna/bioinformatics/phd/mitoproteomes/trypanosoma/trypa_mitoproteins.fasta'
'euglena' : '/home/anna/bioinformatics/phd/euglena_project/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS.fasta'
}

db_paths = {
'arabidopsis': '/home/anna/bioinformatics/phd/mitoproteomes/arabidopsis/arabidopsis_mito/blast_db/arabidopsis_mito.db',
'worm': '/home/anna/bioinformatics/phd/mitoproteomes/caenorhabditis/worm_mitoproteins/blast_db/worm_mitoproteins.db',
'mouse' : '/home/anna/bioinformatics/phd/mitoproteomes/mitocarta/Mouse.MitoCarta2.0/blast_db/Mouse.MitoCarta2.0.db',
'human': '/home/anna/bioinformatics/phd/mitoproteomes/mitocarta/Human.MitoCarta2.0/blast_db/Human.MitoCarta2.0.db',
'yeast' : '/home/anna/bioinformatics/phd/mitoproteomes/saccharomyces/orf_trans_all/blast_db/orf_trans_all.db',
# 'tetrahymena': '/home/anna/bioinformatics/phd/mitoproteomes/tetrahymena/tetrahymena_mito_gb/blast_db/tetrahymena_mito_gb.db',
# 'trypanosoma' : '/home/anna/bioinformatics/phd/mitoproteomes/trypanosoma/trypa_mitoproteins/blast_db/trypa_mitoproteins.db',
# 'euglena' : '/home/anna/bioinformatics/phd/euglena_project/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
}

blast_csv_paths = []
for query in query_paths:
    for db in db_paths:
        new_blast = Blast(query_path=query_paths[query], db_path=db_paths[db], db_type='prot')
        custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
        blast_csv_path = new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)
        print blast_csv_path
        blast_csv_paths.append(blast_csv_path)

for blast_path in blast_csv_paths:
    print blast_path
