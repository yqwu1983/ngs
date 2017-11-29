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

def lexf_rec(alphabet, n, strings):
    n = n - 1
    result = []
    for l in alphabet:
        for s in strings:
            result.append(l + s)
    if n > 0:
        result = lexf_rec(alphabet, n, result)
    return result


def lexf(alphabet, n):
    alphabet = alphabet.replace(" ", "")
    strings = ['']
    result = lexf_rec(alphabet, n, strings)
    return result

def kmer(fasta_path, out_path):
    alphabet = 'A C G T'
    k = 4
    kmers = lexf(alphabet, k)
    kmer_statistics = []
    for kmer in kmers:
        kmer_statistics.append([kmer, 0])
    dna_string = readfasta(fasta_path)[0]['seq']
    for i in range(len(dna_string)-k+1):
        for kmer_stat in kmer_statistics:
            if kmer_stat[0] == dna_string[i:i+k]:
                kmer_stat[1] += 1
    result = []
    for kmer_stat in kmer_statistics:
        result.append(str(kmer_stat[1]))
    result = ' '.join(result)
    with open(out_path, 'w') as outf:
        outf.write(result)
        outf.closed
    return result

fasta_path = '/home/anna/bioinformatics/ngs/rosalind/data/rosalind_kmer.txt'
out_path = '/home/anna/bioinformatics/ngs/rosalind/data/kmer_out.txt'

kmer(fasta_path, out_path)