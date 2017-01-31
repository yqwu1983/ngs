#!/usr/bin/python
def readfasta(fasta_path):
    input = open(fasta_path, 'r')
    records = []
    for line in input:
        if line[0] == '>':
            name = line[1:].rstrip()
            records.append({'seq_name': name, 'seq':''})
        else:
            records[-1]['seq'] += line.rstrip()
    input.close
    return records

def is_glyc_motif(aa_string):
    if len(aa_string) != 4:
        exit(1)
    if (aa_string[0] == 'N') and (aa_string[1] != 'P') and (aa_string[2] in ('S', 'T')) and (aa_string[3] != 'P'):
        return True
    else:
        return False


def find_glyc_motifs(protein):
    results = []
    motif_len = 4
    for i in range(len(protein)-motif_len+1):
        if is_glyc_motif(protein[i:i+motif_len]):
            results.append(str(i+1))
    results = ' '.join(results)
    return results

def mprt(in_path, fasta_path, out_path):
    with open(in_path) as f:
        seq_names = f.readlines()
        f.close()
    seq_names = map(lambda x: x.rstrip(), seq_names)
    proteins = readfasta(fasta_path)
    results = []
    for i in range(len(seq_names)):
        result = find_glyc_motifs(proteins[i]['seq'])
        if len(result) > 0:
            results.append(seq_names[i])
            results.append(result)
    results = '\n'.join(results)
    with open(out_path, 'w') as outf:
        outf.write(results)
        outf.closed
    return results

in_path = '/home/anna/bioinformatics/ngs/rosalind/data/rosalind_mprt.txt'
fasta_path = '/home/anna/Downloads/uniprot-yourlist%3AM2016020945UBHQEXW1.fasta'
out_path = '/home/anna/bioinformatics/ngs/rosalind/data/mprt_out.fasta'

print mprt(in_path, fasta_path, out_path)