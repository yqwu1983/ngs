#!/bin/bash

dir_raw='/media/4TB1/novymonas/trimmed_reads/'

fw=$dir_raw'azi_S1_adapter_trimmed_fw.fq'
rv=$dir_raw'azi_S1_adapter_trimmed_rv.fq'

dir_merged='/media/4TB1/novymonas/merged_reads/'
name='azi_S1_adapter_trimmed'
merged=$dir_merged$name'_merged.fq'
unmerged_fw=$dir_merged$name'_unmerged_1.fq'
unmerged_rv=$dir_merged$name'_unmerged_2.fq'
report=$dir_merged$name'.txt'
ihist=$dir_merged$name'_hist.txt'
extra1=$dir_raw"E262_1_trimmed.fastq"
extra2=$dir_raw"E262_2_trimmed.fastq"
extra3=$dir_raw"wt_S2_L001_unmerged_trimmed_1.fq"
extra4=$dir_raw"wt_S2_L001_unmerged_trimmed_2.fq"
/home/nenarokova/tools/bbmap/bbmerge-auto.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t rem extend2=50 k=62 extra=$extra1,$extra2,$extra3,$extra4 2> $report
