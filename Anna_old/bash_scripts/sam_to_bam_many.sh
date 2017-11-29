#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=1

head_folder='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted/'
cd $head_folder
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
for f in *.sam
	do
		echo $f
		bamfile=$f'.bam'
		samtools view -bS $f > $bamfile
		samtools sort $bamfile $f'_sorted'
		sorted_bam=$f'_sorted.bam'
		samtools index $sorted_bam $f'_sorted.bam.bai'
	done
