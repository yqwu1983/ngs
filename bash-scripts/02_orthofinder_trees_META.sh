#!/bin/bash
#PBS -l select=1:ncpus=60:mem=350gb:scratch_local=350gb
#PBS -l walltime=96:00:00
#PBS -q uv@wagap-pro.cerit-sc.cz
#PBS -j oe
#PBS -N m6A_ortho_add_spec
# initialize the required application
module add orthofinder-2.0.0
module add fasttree-2.1.8
module add mafft-7.305
#NOTE - running on huge nodes uv@wagap-pro.cerit-sc.cz that have limited runtime to 96 hours 
##We wont be using SCRATCH dueing addition of new species - HUGE amnout of data for copy
##using SCRATCHDIR storage which is shared via NFSv4
##DATADIR="/mnt/storage-brno3-cerit/nfs4/home/$LOGNAME/m6a_review/data"
## clean the SCRATCH when job finishes (and data
## are successfully copied out) or is killed
#trap 'clean_scratch' TERM EXIT
#cp -avr $DATADIR $SCRATCHDIR
#cd $SCRATCHDIR
# commands - add another set of proteoms to precomputed smaller set and finnish the whole pipeline up to Trees and Orthologs
DATADIR="/mnt/storage-brno3-cerit/nfs4/home/tskalicky/m6a_review/proteoms/Results_Nov02"
prev_ortho_dir="/mnt/storage-brno3-cerit/nfs4/home/tskalicky/m6a_review/proteoms/Results_Nov02/WorkingDirectory"
new_species="/mnt/storage-brno3-cerit/nfs4/home/tskalicky/m6a_review/proteoms/Results_Nov02/additional_species"
cd $DATADIR
orthofinder -b $prev_ortho_dir -f $new_species -t 60 -a 60 -M msa -oa
tar -cvf Ortho_align_big_set.tar $DATADIR
#
## copy resources from scratch directory back on disk
## field, if not successful, scratch is not deleted
##tar -cvf Orthofinder_alignments.tar $SCRATCHDIR --remove-files
##cp -avr $SCRATCHDIR $DATADIR || export CLEAN_SCRATCH=false
##cd $DATADIR
##tar -xvf Orthofinder_alignments.tar 
echo "Script finished on:"
date +"%d/%m/%Y %H:%M:%S $HOSTNAME"




