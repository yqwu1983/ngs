#!/bin/bash

trimc_dir='/home/nenarokova/tools/Trimmomatic-0.36/'

trim='java -jar '$trimc_dir'trimmomatic-0.36.jar'

adapters='/media/4TB1/kinetoplastids_hinxton/illumina_adapters.fa'
threads=1

file_dir='/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/raw_reads/'
trim_dir='/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/trimmed_reads/'
log_dir='/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/trimming_logs/'

cd file_dir

for f in *_1.fastq:
    name = $f
    p_out_fw=$trim_dir$name'_trimmed_paired_out_fw.fastq'
    u_out_fw=$trim_dir$name'_trimmed_unpaired_out_fw.fastq'
    p_out_rv=$trim_dir$name'_trimmed_paired_out_rv.fastq'
    u_out_rv=$trim_dir$name'_trimmed_unpaired_out_rv.fastq'

    log=$log_dir$name'_trimming.log'

    file_fw=$file_dir$name'_1.fastq'
    file_rv=$file_dir$name'_2.fastq'
    illuminaclip='ILLUMINACLIP:'$adapters':2:30:10'

    $trim PE -threads $threads $file_fw $file_rv $p_out_fw $u_out_fw $p_out_rv $u_out_rv $illuminaclip LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30
