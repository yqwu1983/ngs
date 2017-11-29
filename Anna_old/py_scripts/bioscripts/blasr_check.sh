#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=1

out='/home/nenarokova/kinetoplastids/illumina/assembly/E262_p_apista_pacbio_blasr.out'
python /home/nenarokova/ngs/py_scripts/bioscripts/blasr_check.py > $out
