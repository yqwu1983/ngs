#!/bin/bash
#variables
DATADIR="/Users/tomas/Data/Dropbox/CEITEC_lab/m6A_review/large_set_results/Orthologues_Dec13/"
#
cd $DATADIR
#prvne potreba upravit jmena pridanim znaku, ktere se nevyskytuji mezi beznymi ASCI znaky jako '>[' a ]< a pak udelat nahradu (\w+[0-9]+\.[0-9]) [a-zA-Z0-9 |a-zA-Z0-9_]+ >\[

sed -e 's/"Alligator mississippiensis"/"Amissi"/g' \
-e 's/"Arabidopsis thaliana"/"Athali"/g' \
-e 's/"Bos taurus"/"Btauru"/g' \
-e 's/"Branchiostoma belcheri"/"Bbelch"/g' \
-e 's/"Caenorhabditis elegans"/"Celega"/g' \
-e 's/"Capsaspora owczarzaki ATCC 30864"/"Cowcza"/g' \
-e 's/"Chlamydomonas reinhardtii"/"Creinh"/g' \
-e 's/"Chrysemys picta bellii"/"Cpicta"/g' \
-e 's/"Conidiobolus coronatus NRRL 28638"/"Ccoron"/g' \
-e 's/"Cyanidioschyzon merolae strain 10D"/"Cmerol"/g' \
-e 's/"Danio rerio"/"Drerio"/g' \
-e 's/"Dictyostelium discoideum AX4"/"Ddisco"/g' \
-e 's/"Drosophila melanogaster"/"Dmelan"/g' \
-e 's/"Ectocarpus siliculosus"/"Esilic"/g' \
-e 's/"Emiliania huxleyi CCMP1516"/"Ehuxle"/g' \
-e 's/"Escherichia coli str. K-12 substr. MG1655"/"Escher"/g' \
-e 's/"Exaiptasia pallida"/"Epalli"/g' \
-e 's/"Gallus gallus"/"Ggallu"/g' \
-e 's/"Gekko japonicus"/"Gjapon"/g' \
-e 's/"Giardia_Assemblage_A_isolate_WB"/"Gintes"/g' \
-e 's/"Homo sapiens"/"Hsapie"/g' \
-e 's/"Hydra vulgaris"/"Hvulga"/g' \
-e 's/"Latimeria chalumnae"/"Lchalu"/g' \
-e 's/"Leishmania_major_strain_Friedlin"/"Lmajor"/g' \
-e 's/"Monosiga brevicollis MX1"/"Mbrevi"/g' \
-e 's/"Mus musculus"/"Mmuscu"/g' \
-e 's/"Naegleria gruberi strain NEG-M"/"Ngrube"/g' \
-e 's/"Nanorana parkeri"/"Nparke"/g' \
-e 's/"Nematostella vectensis"/"Nvecte"/g' \
-e 's/"Ophiophagus hannah"/"Ohanna"/g' \
-e 's/"Oryza sativa Japonica Group"/"Osativ"/g' \
-e 's/"Reticulomyxa filosa"/"Rfilos"/g' \
-e 's/"Rhincodon typus"/"Rtypus"/g' \
-e 's/"Saccharomyces cerevisiae S288C"/"Scerev"/g' \
-e 's/"Schizosaccharomyces pombe"/"Spombe"/g' \
-e 's/"Schistosoma mansoni"/"Smanso"/g' \
-e 's/"Tetrahymena thermophila SB210"/"Ttherm"/g' \
-e 's/"Thalassiosira pseudonana CCMP1335"/"Tpseud"/g' \
-e 's/"Toxoplasma gondii ME49"/"Tgondi"/g' \
-e 's/"Trichomonas_vaginalis_G3"/"Tvagin"/g' \
-e 's/"Trichoplax adhaerens"/"Tadhae"/g' \
-e 's/"Trypanosoma_brucei_brucei_TREU927"/"Tbruce"/g' \
-e 's/"Volvox carteri f. nagariensis"/"Vcarte"/g' \
-e 's/"Xenopus laevis"/"Xlaevi"/g' \
-e 's/"Xylella fastidiosa"/"Xfasti"/g' m6A_large_set_Dec13_OGs.txt >m6A_large_set_Dec13_OGs_ren.txt


