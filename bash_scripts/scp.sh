#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/kinetoplastids/pacbio/raw_reads
scp -r 172.18.4.4:/media/4TB3/Tomas_data/Hinxton/RAW_Sequencing_data/PacBio .
