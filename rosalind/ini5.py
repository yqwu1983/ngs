file1 = open('rosalind_ini5.txt', 'r')
file2 = open('ini5.txt', 'a')
counter = 1
for line in file1:
    if counter % 2 == 0:
        file2.write(line) 
    counter = counter + 1
file1.close
file2.close
