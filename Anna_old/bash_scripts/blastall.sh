#!/bin/bash
subj_path="/home/nenarokova/genomes/blasto/blastocrithidia/genome/p57_scaffolds.fa"
dbtype="nucl"
formatdb -i $subj_path -o T -p F

db_path="/home/nenarokova/genomes/blasto/blastocrithidia/genome/cysteine_synthases.fasta"
query="/home/nenarokova/genomes/blasto/blastocrithidia/genome/p57_scaffolds_concatenated.fa"
report="/home/nenarokova/genomes/blasto/blastocrithidia/genome/blastreport_test.txt"

blastall -i $query -d $db_path -p blastx -m 8 -e 0.01 -o $report -a 31
