#!/bin/bash
#applies for sequences stored on Trypka server
working_dir='/home/tomas/CUL13/Virus_search'
genomic_PE='/home/tomas/CUL13/RAW_Illumina/Svobodova_strain/PE/PE_August_trimmed_0.01N1L75.fastq'
genomic_MP='/home/tomas/CUL13/RAW_Illumina/Svobodova_strain/MP/MP_August_trimmed_0.01N1L75.fastq'
transcriptomic_polyA='/home/tomas/CUL13/RAW_Illumina/RNA-Seq/Svobodova_polyA_150bp_0.01_N1_L50.fastq'
transcriptomic_ribominus='/home/tomas/CUL13/RAW_Illumina/RNA-Seq/Svobodova_ribominus_150bp_0.01_N1_L50.fastq'
spec_1='Lrv1-1'
spec_2='Lrv1-4'
spec_3='Pserpens_ssRNA_Narnavirus'
spec_4='Scerevisiae_dsRNA_totivirus_La'
ref1=$spec_1".fas"
ref2=$spec_2".fas"
ref3=$spec_3".fas"
ref4=$spec_4".fas"
lib1='_PE_mapped'
lib2='_MP_mapped'
lib3='_polyA_mapped'
lib4='_ribominus_mapped'
out1=$spec_1$lib1".sam"
out2=$spec_1$lib2".sam"
out3=$spec_1$lib3".sam"
out4=$spec_1$lib4".sam"
out5=$spec_2$lib1".sam"
out6=$spec_2$lib2".sam"
out7=$spec_2$lib3".sam"
out8=$spec_2$lib4".sam"
out9=$spec_3$lib1".sam"
out10=$spec_3$lib2".sam"
out11=$spec_3$lib3".sam"
out12=$spec_3$lib4".sam"
out13=$spec_4$lib1".sam"
out14=$spec_4$lib2".sam"
out15=$spec_4$lib3".sam"
out16=$spec_4$lib4".sam"
outm1=$spec_1$lib1"_only.fq"
outm2=$spec_1$lib2"_only.fq"
outm3=$spec_1$lib3"_only.fq"
outm4=$spec_1$lib4"_only.fq"
outm5=$spec_2$lib1"_only.fq"
outm6=$spec_2$lib2"_only.fq"
outm7=$spec_2$lib3"_only.fq"
outm8=$spec_2$lib4"_only.fq"
outm9=$spec_3$lib1"_only.fq"
outm10=$spec_3$lib2"_only.fq"
outm11=$spec_3$lib3"_only.fq"
outm12=$spec_3$lib4"_only.fq"
outm13=$spec_4$lib1"_only.fq"
outm14=$spec_4$lib2"_only.fq"
outm15=$spec_4$lib3"_only.fq"
outm16=$spec_4$lib4"_only.fq"
covstats1=$spec_1$lib1"_covstats.txt"
covstats2=$spec_1$lib2"_covstats.txt"
covstats3=$spec_1$lib3"_covstats.txt"
covstats4=$spec_1$lib4"_covstats.txt"
covstats5=$spec_2$lib1"_covstats.txt"
covstats6=$spec_2$lib2"_covstats.txt"
covstats7=$spec_2$lib3"_covstats.txt"
covstats8=$spec_2$lib4"_covstats.txt"
covstats9=$spec_3$lib1"_covstats.txt"
covstats10=$spec_3$lib2"_covstats.txt"
covstats11=$spec_3$lib3"_covstats.txt"
covstats12=$spec_3$lib4"_covstats.txt"
covstats13=$spec_4$lib1"_covstats.txt"
covstats14=$spec_4$lib2"_covstats.txt"
covstats15=$spec_4$lib3"_covstats.txt"
covstats16=$spec_4$lib4"_covstats.txt"
covhist1=$spec_1$lib1"_covhist.txt"
covhist2=$spec_1$lib2"_covhist.txt"
covhist3=$spec_1$lib3"_covhist.txt"
covhist4=$spec_1$lib4"_covhist.txt"
covhist5=$spec_2$lib1"_covhist.txt"
covhist6=$spec_2$lib2"_covhist.txt"
covhist7=$spec_2$lib3"_covhist.txt"
covhist8=$spec_2$lib4"_covhist.txt"
covhist9=$spec_3$lib1"_covhist.txt"
covhist10=$spec_3$lib2"_covhist.txt"
covhist11=$spec_3$lib3"_covhist.txt"
covhist12=$spec_3$lib4"_covhist.txt"
covhist13=$spec_4$lib1"_covhist.txt"
covhist14=$spec_4$lib2"_covhist.txt"
covhist15=$spec_4$lib3"_covhist.txt"
covhist16=$spec_4$lib4"_covhist.txt"
basecov1=$spec_1$lib1"_basecov.txt"
basecov2=$spec_1$lib2"_basecov.txt"
basecov3=$spec_1$lib3"_basecov.txt"
basecov4=$spec_1$lib4"_basecov.txt"
basecov5=$spec_2$lib1"_basecov.txt"
basecov6=$spec_2$lib2"_basecov.txt"
basecov7=$spec_2$lib3"_basecov.txt"
basecov8=$spec_2$lib4"_basecov.txt"
basecov9=$spec_3$lib1"_basecov.txt"
basecov10=$spec_3$lib2"_basecov.txt"
basecov11=$spec_3$lib3"_basecov.txt"
basecov12=$spec_3$lib4"_basecov.txt"
basecov13=$spec_4$lib1"_basecov.txt"
basecov14=$spec_4$lib2"_basecov.txt"
basecov15=$spec_4$lib3"_basecov.txt"
basecov16=$spec_4$lib4"_basecov.txt"
bincov1=$spec_1$lib1"_bincov.txt"
bincov2=$spec_1$lib2"_bincov.txt"
bincov3=$spec_1$lib3"_bincov.txt"
bincov4=$spec_1$lib4"_bincov.txt"
bincov5=$spec_2$lib1"_bincov.txt"
bincov6=$spec_2$lib2"_bincov.txt"
bincov7=$spec_2$lib3"_bincov.txt"
bincov8=$spec_2$lib4"_bincov.txt"
bincov9=$spec_3$lib1"_bincov.txt"
bincov10=$spec_3$lib2"_bincov.txt"
bincov11=$spec_3$lib3"_bincov.txt"
bincov12=$spec_3$lib4"_bincov.txt"
bincov13=$spec_4$lib1"_bincov.txt"
bincov14=$spec_4$lib2"_bincov.txt"
bincov15=$spec_4$lib3"_bincov.txt"
bincov16=$spec_4$lib4"_bincov.txt"
#
#
cd /home/tomas/CUL13/Virus_search
#To map with super-high sensitivity (useful for very-low-quality data, or remote homologies) with statistics:
#mapPacBio.sh in=reads.fq out=mapped.sam outm=mapped.fq vslow k=8 maxindel=200 minratio=0.1 covstats=covstats.txt covhist=covhist1.txt basecov=basecov.txt bincov=bincov.txt
#To map with high sensitivity with mapped reads in fastaq and statistics:
bbmap.sh in=$genomic_PE ref=$ref1 nodisk out=$out1 outm=$outm1 slow k=12 covstats=$covstats1 covhist=$covhist1 basecov=$basecov1 bincov=$bincov1
bbmap.sh in=$genomic_MP ref=$ref1 nodisk out=$out2 outm=$outm2 slow k=12 covstats=$covstats2 covhist=$covhist2 basecov=$basecov2 bincov=$bincov2
bbmap.sh in=$transcriptomic_polyA ref=$ref1 nodisk out=$out3 outm=$outm3 slow k=12 covstats=$covstats3 covhist=$covhist3 basecov=$basecov3 bincov=$bincov3
bbmap.sh in=$transcriptomic_ribominus ref=$ref1 nodisk out=$out4 outm=$outm4 slow k=12 covstats=$covstats4 covhist=$covhist4 basecov=$basecov4 bincov=$bincov4
#
bbmap.sh in=$genomic_PE ref=$ref2 nodisk out=$out5 outm=$outm5 slow k=12 covstats=$covstats5 covhist=$covhist5 basecov=$basecov5 bincov=$bincov5
bbmap.sh in=$genomic_MP ref=$ref2 nodisk out=$out6 outm=$outm6 slow k=12 covstats=$covstats6 covhist=$covhist6 basecov=$basecov6 bincov=$bincov6
bbmap.sh in=$transcriptomic_polyA ref=$ref2 nodisk out=$out7 outm=$outm7 slow k=12 covstats=$covstats7 covhist=$covhist7 basecov=$basecov7 bincov=$bincov7
bbmap.sh in=$transcriptomic_ribominus ref=$ref2 nodisk out=$out8 outm=$outm8 slow k=12 covstats=$covstats8 covhist=$covhist8 basecov=$basecov8 bincov=$bincov8
#
bbmap.sh in=$genomic_PE ref=$ref3 nodisk out=$out9 outm=$outm9 slow k=12 covstats=$covstats9 covhist=$covhist9 basecov=$basecov9 bincov=$bincov9
bbmap.sh in=$genomic_MP ref=$ref3 nodisk out=$out10 outm=$outm10 slow k=12 covstats=$covstats10 covhist=$covhist10 basecov=$basecov10 bincov=$bincov10
bbmap.sh in=$transcriptomic_polyA ref=$ref3 nodisk out=$out11 outm=$outm11 slow k=12 covstats=$covstats11 covhist=$covhist11 basecov=$basecov11 bincov=$bincov11
bbmap.sh in=$transcriptomic_ribominus ref=$ref3 nodisk out=$out12 outm=$outm12 slow k=12 covstats=$covstats12 covhist=$covhist12 basecov=$basecov12 bincov=$bincov12
#
bbmap.sh in=$genomic_PE ref=$ref4 nodisk out=$out13 outm=$outm13 slow k=12 covstats=$covstats13 covhist=$covhist13 basecov=$basecov13 bincov=$bincov13
bbmap.sh in=$genomic_MP ref=$ref4 nodisk out=$out14 outm=$outm14 slow k=12 covstats=$covstats14 covhist=$covhist14 basecov=$basecov14 bincov=$bincov14
bbmap.sh in=$transcriptomic_polyA ref=$ref4 nodisk out=$out15 outm=$outm15 slow k=12 covstats=$covstats15 covhist=$covhist15 basecov=$basecov15 bincov=$bincov15
bbmap.sh in=$transcriptomic_ribominus ref=$ref4 nodisk out=$out16 outm=$outm16 slow k=12 covstats=$covstats16 covhist=$covhist16 basecov=$basecov16 bincov=$bincov16

