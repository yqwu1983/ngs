#!/bin/bash
in1="/media/4TB1/novymonas/merged_reads/azi_S1_adapter_trimmed_unmerged_1.fq"
in2="/media/4TB1/novymonas/merged_reads/azi_S1_adapter_trimmed_unmerged_2.fq"
out1="/media/4TB1/novymonas/trimmed_reads/azi_S1_unmerged_trimmed_1.fq"
out2="/media/4TB1/novymonas/trimmed_reads/azi_S1_unmerged_trimmed_2.fq"
/home/nenarokova/tools/bbmap/bbduk.sh in1=$in1 in2=$in2 out1=$out1 out2=$out2 qtrim=r trimq=20 overwrite=true
