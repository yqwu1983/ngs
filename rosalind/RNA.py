forward = 'CATCTCGACATCTTGATCGGACCCATACGACTTAGCTCTGTTAGGATAGACCTGGCGACGAACACGCCCCACATTATCTGCCACACGAGTGCCAGTCTTCAAAAGACTATGCAAGCCTTGTCGAGGAGCTAGCACGTTCGAGAATAATCATAAGTAGTAAATCACGCATGTGGCCCTCGACCAGCCGAATTCTGTCGGGTCGTTTATCCCGAACCCAGTTTGCGATTTTTAAGCGTACGGAGCCGTCTCGGATAGGAAGTATCCTCGTTAAGCTACTGCAACTGTGAGCACATCGTTTTCGGATCTGGATGCGCAACGTGGCGGCAGCGAATTCAATGTACGATTGCAACAGGTACGTCCTCGGGCGCGGAACATCCTGAATCATTGCCCTTCGATAGTCTACCACATTCAAAGAATGTTTTTTGACTGATTCCGGGTATAATGTTGCTGCAAACGGGACTCCTGGCTACAAGACGCGAGCGTTCTCATATGTGGAATATTCCAATCGCCCAATCGGTGACAATATATACACCATCGGTGCGTCGTTCTATCGCACTTATATAAGTTCTGTCGGTGACAGTTTTGAAGTCATAGGGTGCGGGTTCGCGGATTAAAGGCCAGGCTTGTTGGTACTAGGCCAAGATGTATGACTATGCCGGAATAGCTGCATCCGGTCCCTGAACTTCGTCGCCGTCGTTGACCAAAACTCGGCTGAAACTCGTAGACATTCGAAAACTCCCCATTACGTGCACAACCATTGCTGTCTGCACTTATTATCGCACATAGTTATGGTGTAACCATAGTCCCAGTATGAACAATGCAACACCGACCGATACGCATGGCGAAAATCGTCGGAAAATCGCTGCCGAGTCAATTAATGCCCACGAATAGCCGTATTTTGACCTTCCACAATCTTGGTGACAATAAACAAGGGGCGTGTTAGTGCTAGCGTGTGGGTTGCGCGTCACCATGCGTGTTCTAAGT'
from string import maketrans
complement = maketrans('ATGC', 'TACG')
reverse = forward.translate(complement)[::-1]
print reverse
