from string import maketrans
from Bio import SeqIO

def reverse(seq):
    complement = maketrans('ATGC', 'TACG')
    reverse = seq.translate(complement)[::-1]
    return reverse

def translate (mRNA):    
    gene_code = dict(UUU = 'F', CUU = 'L', AUU = 'I', GUU = 'V', UUC ='F', CUC = 'L', AUC ='I',
    GUC = 'V', UUA = 'L', CUA = 'L', AUA = 'I', GUA = 'V', UUG = 'L', CUG = 'L', AUG = 'M', GUG = 'V',
    UCU = 'S', CCU = 'P', ACU = 'T', GCU = 'A', UCC = 'S', CCC = 'P', ACC = 'T', GCC = 'A', UCA = 'S',
    CCA = 'P', ACA = 'T', GCA = 'A', UCG = 'S', CCG = 'P', ACG = 'T', GCG = 'A', UAU = 'Y', CAU = 'H',
    AAU = 'N', GAU = 'D', UAC = 'Y', CAC = 'H', AAC = 'N', GAC = 'D', UAA = '!', CAA = 'Q', AAA = 'K',
    GAA = 'E', UAG = '!', CAG = 'Q', AAG = 'K', GAG = 'E', UGU = 'C', CGU = 'R', AGU = 'S', GGU = 'G',
    UGC = 'C', CGC = 'R', AGC = 'S', GGC  = 'G', UGA = '!', CGA = 'R', AGA = 'R', GGA = 'G', UGG = 'W',
    CGG = 'R', AGG = 'R', GGG = 'G')
    peptide = ''
    for first in range (0, len(mRNA), 3):
        last = first + 3
        codon = mRNA[first : last]
        if codon in gene_code:
            peptide = peptide + gene_code[codon]	
    return peptide

f = '/home/anna/Downloads/rosalind_orf.txt'
fDNA = str((SeqIO.read(f, 'fasta')).seq)
rDNA = reverse (fDNA)
ORFs = []
for DNA in (fDNA, rDNA):  
    mRNA = DNA.replace('T', 'U')
    for i in range(3):
        mRNA2 = mRNA[i:-1]
        peptide = translate(mRNA2)
        # print 'peptides'
        # print peptide
        starts = []
        ends = []
        for i in range(len(peptide)):
            if peptide[i] == 'M':
                starts.append(i)
            elif peptide[i] == '!':
                ends.append(i)
        # print "ORFs:"
        for start in starts:
            for end in ends:
                if start < end:
                    ORF = peptide[start:end]
                    if ORF not in ORFs:
                        ORFs.append(ORF)
                    break
for ORF in ORFs:
    print ORF        
                    