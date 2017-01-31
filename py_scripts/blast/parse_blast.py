#!/usr/bin/python
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from helpers.make_outdir import file_from_path, make_outdir

from Bio.Blast import NCBIXML
from Bio import SeqIO
import sys
import csv
import os
import time
from natsort import natsorted
from Bio.SeqRecord import SeqRecord
global ONLY_ONE_HIT; ONLY_ONE_HIT = False


def compare_blast_gbk(reference_gbk, blast_xml_file):
	gb_record = SeqIO.read(reference_gbk, "genbank")
	blast_xml = open(blast_xml_file)
	blast_records = NCBIXML.parse(blast_xml)
	hits = []
	for record in blast_records:
		for alignment in record.alignments:
			for hsp in alignment.hsps:
				hsp_start, hsp_end = hsp.query_start, hsp.query_end
				if hsp_start > hsp_end: hsp_start, hsp_end = hsp_end, hsp_start
				q_start, q_end = hsp.sbjct_start, hsp.sbjct_end
				if q_start > q_end: q_start, q_end = q_end, q_start
				hits.append({'name': str(alignment.title), 'hsp_start': hsp_start, 'hsp_end': hsp_end,
							'q_start': q_start, 'q_end': q_end,
							'align_length': hsp.align_length, 'identities': hsp.identities, 'e_value': hsp.expect})

	hits = sorted(hits, key=lambda k: k['hsp_start'])

	features = gb_record.features

	hit_records = []

	for hit in hits:
		for feature in features:
			if feature.type == 'gene':
				gene_start = feature.location.start
				gene_end = feature.location.end
				if gene_start > hit['hsp_start']:
					right_gene = feature
					break
				else:
					left_gene = feature
					if gene_end >= hit['hsp_end']:
						right_gene = feature
						break
		hit_records.append({'query': hit['name'], 'q_start': hit['q_start'], 'q_end': hit['q_end'],
								    'sbjct_start': hit['hsp_start'], 'sbjct_end': hit['hsp_end'],
								  	'align_length': hit['align_length'], 'identities': hit['identities'], 'e_value': hit['e_value'],
								  	'left_gene': str(left_gene.qualifiers['gene']).translate(None, '[]\"\''), 'lg_start': int(left_gene.location.start), 'lg_end': int(left_gene.location.end),
								  	'right_gene': str(right_gene.qualifiers['gene']).translate(None, '[]\"\''), 'rg_start': int(left_gene.location.start), 'rg_end': int(left_gene.location.end)})
	blast_xml.close()
	return hit_records

file_gb = '/home/anna/bioinformatics/outdirs/BL21.gbk'
workdir = '/home/anna/bioinformatics/outdirs/alignments/contigs/'
outdir = workdir
xml_mut6 = workdir + 'BL21_contigs_mut6_ends.xml'
xml_mut9 = workdir + 'BL21_contigs_mut9_ends.xml'
comparison = []
process_count = 0

for blast_xml_file in (xml_mut6, xml_mut9):
	hit_records = compare_blast_gbk(file_gb, blast_xml_file)

	keys = ['query', 'q_start', 'q_end', 'align_length', 'identities', 'e_value', 'sbjct_start', 'sbjct_end',
		'left_gene', 'lg_start', 'lg_end', 'right_gene', 'rg_start', 'rg_end']

	hit_records = natsorted(hit_records, key = lambda x: (x['query'], -x['align_length'], -x['identities']))

	clean_records = [hit_records[0]]
	for hit_record in hit_records:
		last = clean_records[-1]
		if hit_record['query'] == last['query']:
			if hit_record['q_start'] < last['q_start'] or hit_record['q_end'] > last['q_end']:
				clean_records.append(hit_record)
		else: clean_records.append(hit_record)

	hits_file = outdir + file_from_path(blast_xml_file)[0:-4] + '.csv'

	with open(hits_file , 'wb') as hits_file:
		dict_writer = csv.DictWriter(hits_file, keys)
		dict_writer.writer.writerow(keys)
		dict_writer.writerows(clean_records)
	hits_file.closed


# handle_file = '/home/anna/bioinformatics/wheat/NBS_LRR_new_assembly_blreport.csv'
handle_file = '/mnt/lustre/nenarokova/wheat/NBS_LRR_new_assembly_blreport.csv'
handle_file = open(handle_file)
handle_csv = csv.reader(handle_file, delimiter=',')

if ONLY_ONE_HIT:
	sorted_csv = sorted( handle_csv, key = lambda x: ( x[0], -int(x[3]), -float(x[2]) ) )

	results = []
	cur_seq = None
	for row in sorted_csv:
		if row[0] != cur_seq:
			cur_seq = row[0]
			results.append(row)
	handle_file.close()
else:
	results = []
	for row in handle_csv:
		results.append(row)
k=0
fasta_file = sys.argv[1]
result_seqs = []
for seq_record in SeqIO.parse(fasta_file, "fasta"):
	for row in results:
		if seq_record.id == row[1]:
			start = int(row[8])
			end = int(row[9])
			if start > end: start, end = end, start
			seq = seq_record.seq[start:end]
			result_seqs.append(SeqRecord(seq=seq, id=seq_record.id.strip() + row[0].strip() + str(k), description=''))
			results.remove(row)
			k+=1

out_folder = '/home/nenarokova/wheat/new_assembly/nbs_lrr_genes/'
out_file = out_folder + file_from_path(fasta_file) + '_nbs_lrr.fasta'
SeqIO.write(result_seqs, out_file, "fasta")
