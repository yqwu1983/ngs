#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
#PBS -l mem=48gb
cd /mnt/results/nenarokova/wheat/L/sum_fastq_re/sorted/
for dir in */
	do
		cd $dir
		cd trim_out
		/home/nenarokova/VelvetOptimiser-2.2.5/VelvetOptimiser.pl -s 33 -e 63 -t 24 -f '-fastq unpaired_out_fw.fastq -fastq unpaired_out_rv.fastq -shortPaired -fastq paired_out_fw.fastq -fastq paired_out_rv.fastq' -o '-min_contig_lgth 200 -cov_cutoff 10'
		cd ../../
	done