#!/bin/bash
#PBS -l select=1:ncpus=1:mem=100gb:scratch_local=80gb:os=debian9
#PBS -l walltime=48:00:00
#PBS -q default@wagap-pro.cerit-sc.cz
#PBS -j oe
#PBS -N m6A_packing
# initialize the required application
cd /mnt/storage-brno3-cerit/nfs4/home/tskalicky/m6a_review/proteoms
#just tar all files without compressing with gzip -zcvf option
tar -cvf Results_Dec05.tar /mnt/storage-brno3-cerit/nfs4/home/tskalicky/m6a_review/proteoms/Results_Nov02/
