#!/bin/sh
#variables
DATAFILE="/Users/tomas/Data/m6A_review/large_set_results/"
###################################################
cd $DATAFILE
for i in *.fa
do
    FILENAME=${i%.*}
    
    sed -E -e 's/>0_/>Amissi_/g' \
    -e 's/>1_/>Bbelch_/g' \
    -e 's/>2_/>Btauru_/g' \
    -e 's/>3_/>Ccoron_/g' \
    -e 's/>4_/>Celega_/g' \
    -e 's/>5_/>Cmerol_/g' \
    -e 's/>6_/>Cowcza_/g' \
    -e 's/>7_/>Cpicta_/g' \
    -e 's/>8_/>Creinh_/g' \
    -e 's/>9_/>Ddisco_/g' \
    -e 's/>10_/>Drerio_/g' \
    -e 's/>11_/>Ehuxle_/g' \
    -e 's/>12_/>Epalli_/g' \
    -e 's/>13_/>Escher_/g' \
    -e 's/>14_/>Ggallu_/g' \
    -e 's/>15_/>Gintes_/g' \
    -e 's/>16_/>Gjapon_/g' \
    -e 's/>17_/>Hsapie_/g' \
    -e 's/>18_/>Hvulga_/g' \
    -e 's/>19_/>Lchalu_/g' \
    -e 's/>20_/>Lmajor_/g' \
    -e 's/>21_/>Mbrevi_/g' \
    -e 's/>22_/>Ngrube_/g' \
    -e 's/>23_/>Nparke_/g' \
    -e 's/>24_/>Nvecte_/g' \
    -e 's/>25_/>Ohanna_/g' \
    -e 's/>26_/>Rfilos_/g' \
    -e 's/>27_/>Rtypus_/g' \
    -e 's/>28_/>Scerev_/g' \
    -e 's/>29_/>Smanso_/g' \
    -e 's/>30_/>Tadhae_/g' \
    -e 's/>31_/>Tbruce_/g' \
    -e 's/>32_/>Tgondi_/g' \
    -e 's/>33_/>Tpseud_/g' \
    -e 's/>34_/>Ttherm_/g' \
    -e 's/>35_/>Tvagin_/g' \
    -e 's/>36_/>Xfasti_/g' \
    -e 's/>37_/>Dmelan_/g' \
    -e 's/>38_/>Athali_/g' \
    -e 's/>39_/>Esilic_/g' \
    -e 's/>40_/>Mmuscu_/g' \
    -e 's/>41_/>Osativ_/g' \
    -e 's/>42_/>Spombe_/g' \
    -e 's/>43_/>Vcarte_/g' \
    -e 's/>44_/>Xlaevi_/g' \
    -e 's/(\d+)\\n/\1\\t\\n/g' \
    -e 's/\\n//g' \
    -e 's/\\t/\\n/g' <"$i" > $FILENAME"_ren.fst" # need to use "$i" to avoid word splitting on filenames with spaces
done

# sed uses -E for regular expression in OS X, linux uses -r 
# alternative usage for huge amount of files that would exceed the limit of bash:
# find . -type f -name 'co_hledam*' | xargs sed -i 's/asd/dsg/g'
#or:
#Linux: grep -r -l <old> * | xargs sed -i 's/<old>/<new>/g'
#OS X: grep -r -l <old> * | xargs sed -i '' 's/<old>/<new>/g'
#
#For grep:
#    -r recursively searches subdirectories 
#    -l prints file names that contain matches
#For sed:
#    -i extension (Note: An argument needs to be provided on OS X)
