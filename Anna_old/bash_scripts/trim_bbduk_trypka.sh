#!/bin/bash

fw="/media/4TB1/novymonas/raw_reads/wt_S2_L001_R1_001.fastq.gz"
rv="/media/4TB1/novymonas/raw_reads/wt_S2_L001_R2_001.fastq.gz"
trimdir='/media/4TB1/novymonas/trimmed_reads/'
name='wt_S2'
trimmed_fw=$trimdir$name'_adapter_trimmed_1.fq'
trimmed_rv=$trimdir$name'_adapter_trimmed_2.fq'

adapters='/home/nenarokova/tools/bbmap/resources/adapters.fa'
/home/nenarokova/tools/bbmap/bbduk.sh in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe t=20  #only adapter trimming

# /home/nenarokova/tools/bbmap/bbduk.sh in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv qtrim=rl trimq=20 usejni=t 2> $report
# bbduk.sh -Xmx1g in1=read1.fq in2=read2.fq out1=clean1.fq out2=clean2.fq ref=adapters.fa ktrim=r k=23 mink=11 hdist=1 tpe
