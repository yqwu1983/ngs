def translateDNA (DNA):    
    gene_code = dict(TTT = 'F', CTT = 'L', ATT = 'I', GTT = 'V', TTC ='F', CTC = 'L', ATC ='I',
    GTC = 'V', TTA = 'L', CTA = 'L', ATA = 'I', GTA = 'V', TTG = 'L', CTG = 'L', ATG = 'M', GTG = 'V',
    TCT = 'S', CCT = 'P', ACT = 'T', GCT = 'A', TCC = 'S', CCC = 'P', ACC = 'T', GCC = 'A', TCA = 'S',
    CCA = 'P', ACA = 'T', GCA = 'A', TCG = 'S', CCG = 'P', ACG = 'T', GCG = 'A', TAT = 'Y', CAT = 'H',
    AAT = 'N', GAT = 'D', TAC = 'Y', CAC = 'H', AAC = 'N', GAC = 'D', TAA = 'Stop', CAA = 'Q', AAA = 'K',
    GAA = 'E', TAG = 'Stop', CAG = 'Q', AAG = 'K', GAG = 'E', TGT = 'C', CGT = 'R', AGT = 'S', GGT = 'G',
    TGC = 'C', CGC = 'R', AGC = 'S', GGC  = 'G', TGA = 'Stop', CGA = 'R', AGA = 'R', GGA = 'G', TGG = 'W',
    CGG = 'R', AGG = 'R', GGG = 'G')
    peptide = ''
    for first in range (0, len(DNA), 3):
        last = first + 3
        codon = DNA[first : last]
        if codon in gene_code:
            if gene_code[codon] == 'Stop': break
            else:
                peptide = peptide + gene_code[codon]
        else:
            print 'no'
    return peptide

def readfasta (fasta):
    input = open(fasta, 'r')
    seqs = {}
    for line in input:
        if line[0] == '>':
            name = line[1:].rstrip()
            seqs[name] = [] 
        else:
            seqs[name].append(line.rstrip())
    for name in seqs:
        seqs[name] = ''.join(seqs[name])
    return seqs

seqs = readfasta('rosalind_splc (3).txt')

gene_name = 'Rosalind_3921'
gene = seqs[gene_name]

introns = []
for name in seqs:
    if name != gene_name :
        introns.append(seqs[name])

for intron in introns:
    gene = gene.replace(intron, "")

peptide = translateDNA(gene)
print peptide