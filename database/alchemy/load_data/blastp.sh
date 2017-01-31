blastp -query /home/nenarokova/blast_proteome/euglena_all_proteins.fasta \
-db /home/nenarokova/blast_proteome/reference_proteomes/blast_db/reference_proteomes.db \
-out /home/nenarokova/blast_proteome/euglena_all_proteins_bl_report.csv \
-outfmt "10  qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send " \
-num_threads 32 -evalue 0.01 -word_size 2
