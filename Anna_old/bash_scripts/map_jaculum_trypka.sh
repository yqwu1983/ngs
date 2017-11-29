#!/bin/bash
folder='/media/4TB1/kinetoplastids_hinxton/jaculum/trimmed_reads/'
cd $folder
alignment='/media/4TB1/kinetoplastids_hinxton/jaculum/jaculum_mapping/alignment.sam'
bt2_base='/media/4TB1/kinetoplastids_hinxton/pyrrhocoris_bt2/leptomonas'

out='/media/4TB1/kinetoplastids_hinxton/jaculum/bw2_stats/18098_1#5_pyrrhocoris.txt'
clean_reads_paired='/media/4TB1/kinetoplastids_hinxton/jaculum/cleaned_reads/18098_1#5_ad_q20_l50_paired_cleaned.fastq'
clean_reads_unpaired='/media/4TB1/kinetoplastids_hinxton/jaculum/cleaned_reads/18098_1#5_ad_q20_l50_unpaired_cleaned.fastq'
paired_fw=$folder'18098_1#5_paired_out_fw_ad_q20_l50.fastq'
paired_rv=$folder'18098_1#5_paired_out_rv_ad_q20_l50.fastq'
unpaired_fw=$folder'18098_1#5_unpaired_out_fw_ad_q20_l50.fastq'
unpaired_rv=$folder'18098_1#5_unpaired_out_rv_ad_q20_l50.fastq'
out='/media/4TB1/kinetoplastids_hinxton/jaculum/jaculum_mapping/18098_1#5.txt'
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 -D 5 -R 1 -N 0 -L 32 -p 32 -x $bt2_base -1 $paired_fw -2 $paired_rv -U $unpaired_fw,$unpaired_rv -S $alignment --un $clean_reads_unpaired --un-conc $clean_reads_paired 2> $out
