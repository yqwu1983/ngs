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

def sseq(fasta_path, out_path):
    seqs = readfasta(fasta_path)
    string = seqs[0]['seq']
    substring = seqs[1]['seq']
    result = []
    start = 0
    for s1 in substring:
        for i, s2 in enumerate(string[start:]):
            if s1 == s2:
                new_start = start + i + 1
                result.append(str(new_start))
                start = new_start
                break
    result = ' '.join(result)
    with open(out_path, 'w') as outf:
        outf.write(result)
        outf.closed
    return 0


fasta_path = '/home/anna/bioinformatics/ngs/rosalind/data/rosalind_sseq.txt'
out_path = '/home/anna/bioinformatics/ngs/rosalind/data/sseq_result.txt'
sseq(fasta_path, out_path)