#!/bin/bash
#applies for sequences stored on Trypka server
working_dir='/home/tomas/CUL13/Virus_search'
genomic_PE='/home/tomas/CUL13/RAW_Illumina/Svobodova_strain/PE/PE_August_trimmed_0.01N1L75.fastq'
genomic_MP='/home/tomas/CUL13/RAW_Illumina/Svobodova_strain/MP/MP_August_trimmed_0.01N1L75.fastq'
transcriptomic_polyA='/home/tomas/CUL13/RAW_Illumina/RNA-Seq/Svobodova_polyA_150bp_0.01_N1_L50.fastq'
transcriptomic_ribominus='/home/tomas/CUL13/RAW_Illumina/RNA-Seq/Svobodova_ribominus_150bp_0.01_N1_L50.fastq'
spec1='Lrv1-1'
spec2='Lrv1-4'
spec3='Pserpens_ssRNA_Narnavirus'
spec4='Scerevisiae_dsRNA_totivirus_La'
ref1=$spec1".fas"
ref2=$spec2".fas"
ref3=$spec3".fas"
ref4=$spec4".fas"
lib1='_PE_mapped'
lib2='_MP_mapped'
lib3='_polyA_mapped'
lib4='_ribominus_mapped'
out1=$spec1$lib1".sam"
out2=$spec1$lib2".sam"
out3=$spec1$lib3".sam"
out4=$spec1$lib4".sam"
out5=$spec2$lib1".sam"
out6=$spec2$lib2".sam"
out7=$spec2$lib3".sam"
out8=$spec2$lib4".sam"
out9=$spec3$lib1".sam"
out10=$spec3$lib2".sam"
out11=$spec3$lib3".sam"
out12=$spec3$lib4".sam"
out13=$spec4$lib1".sam"
out14=$spec4$lib2".sam"
out15=$spec4$lib3".sam"
out16=$spec4$lib4".sam"
outm1=$spec1$lib1"_only.fq"
outm2=$spec1$lib2"_only.fq"
outm3=$spec1$lib3"_only.fq"
outm4=$spec1$lib4"_only.fq"
outm5=$spec2$lib1"_only.fq"
outm6=$spec2$lib2"_only.fq"
outm7=$spec2$lib3"_only.fq"
outm8=$spec2$lib4"_only.fq"
outm9=$spec3$lib1"_only.fq"
outm10=$spec3$lib2"_only.fq"
outm11=$spec3$lib3"_only.fq"
outm12=$spec3$lib4"_only.fq"
outm13=$spec4$lib1"_only.fq"
outm14=$spec4$lib2"_only.fq"
outm15=$spec4$lib3"_only.fq"
outm16=$spec4$lib4"_only.fq"
covstats1=$spec1$lib1"_covstats.txt"
covstats2=$spec1$lib2"_covstats.txt"
covstats3=$spec1$lib3"_covstats.txt"
covstats4=$spec1$lib4"_covstats.txt"
covstats5=$spec2$lib1"_covstats.txt"
covstats6=$spec2$lib2"_covstats.txt"
covstats7=$spec2$lib3"_covstats.txt"
covstats8=$spec2$lib4"_covstats.txt"
covstats9=$spec3$lib1"_covstats.txt"
covstats10=$spec3$lib2"_covstats.txt"
covstats11=$spec3$lib3"_covstats.txt"
covstats12=$spec3$lib4"_covstats.txt"
covstats13=$spec4$lib1"_covstats.txt"
covstats14=$spec4$lib2"_covstats.txt"
covstats15=$spec4$lib3"_covstats.txt"
covstats16=$spec4$lib4"_covstats.txt"
covhist1=$spec1$lib1"_covhist.txt"
covhist2=$spec1$lib2"_covhist.txt"
covhist3=$spec1$lib3"_covhist.txt"
covhist4=$spec1$lib4"_covhist.txt"
covhist5=$spec2$lib1"_covhist.txt"
covhist6=$spec2$lib2"_covhist.txt"
covhist7=$spec2$lib3"_covhist.txt"
covhist8=$spec2$lib4"_covhist.txt"
covhist9=$spec3$lib1"_covhist.txt"
covhist10=$spec3$lib2"_covhist.txt"
covhist11=$spec3$lib3"_covhist.txt"
covhist12=$spec3$lib4"_covhist.txt"
covhist13=$spec4$lib1"_covhist.txt"
covhist14=$spec4$lib2"_covhist.txt"
covhist15=$spec4$lib3"_covhist.txt"
covhist16=$spec4$lib4"_covhist.txt"
basecov1=$spec1$lib1"_basecov.txt"
basecov2=$spec1$lib2"_basecov.txt"
basecov3=$spec1$lib3"_basecov.txt"
basecov4=$spec1$lib4"_basecov.txt"
basecov5=$spec2$lib1"_basecov.txt"
basecov6=$spec2$lib2"_basecov.txt"
basecov7=$spec2$lib3"_basecov.txt"
basecov8=$spec2$lib4"_basecov.txt"
basecov9=$spec3$lib1"_basecov.txt"
basecov10=$spec3$lib2"_basecov.txt"
basecov11=$spec3$lib3"_basecov.txt"
basecov12=$spec3$lib4"_basecov.txt"
basecov13=$spec4$lib1"_basecov.txt"
basecov14=$spec4$lib2"_basecov.txt"
basecov15=$spec4$lib3"_basecov.txt"
basecov16=$spec4$lib4"_basecov.txt"
bincov1=$spec1$lib1"_bincov.txt"
bincov2=$spec1$lib2"_bincov.txt"
bincov3=$spec1$lib3"_bincov.txt"
bincov4=$spec1$lib4"_bincov.txt"
bincov5=$spec2$lib1"_bincov.txt"
bincov6=$spec2$lib2"_bincov.txt"
bincov7=$spec2$lib3"_bincov.txt"
bincov8=$spec2$lib4"_bincov.txt"
bincov9=$spec3$lib1"_bincov.txt"
bincov10=$spec3$lib2"_bincov.txt"
bincov11=$spec3$lib3"_bincov.txt"
bincov12=$spec3$lib4"_bincov.txt"
bincov13=$spec4$lib1"_bincov.txt"
bincov14=$spec4$lib2"_bincov.txt"
bincov15=$spec4$lib3"_bincov.txt"
bincov16=$spec4$lib4"_bincov.txt"
#SAMTOOLS variables
fai1=$ref1".fai"
fai2=$ref2".fai"
fai3=$ref3".fai"
fai4=$ref4".fai"
sorted1=$spec1$lib1".sorted"
sorted2=$spec1$lib2".sorted"
sorted3=$spec1$lib3".sorted"
sorted4=$spec1$lib4".sorted"
sorted5=$spec2$lib1".sorted"
sorted6=$spec2$lib2".sorted"
sorted7=$spec2$lib3".sorted"
sorted8=$spec2$lib4".sorted"
sorted9=$spec3$lib1".sorted"
sorted10=$spec3$lib2".sorted"
sorted11=$spec3$lib3".sorted"
sorted12=$spec3$lib4".sorted"
sorted13=$spec4$lib1".sorted"
sorted14=$spec4$lib2".sorted"
sorted15=$spec4$lib3".sorted"
sorted16=$spec4$lib4".sorted"
bam1=$sorted1".bam"
bam2=$sorted2".bam"
bam3=$sorted3".bam"
bam4=$sorted4".bam"
bam5=$sorted5".bam"
bam6=$sorted6".bam"
bam7=$sorted7".bam"
bam8=$sorted8".bam"
bam9=$sorted9".bam"
bam10=$sorted10".bam"
bam11=$sorted11".bam"
bam12=$sorted12".bam"
bam13=$sorted13".bam"
bam14=$sorted14".bam"
bam15=$sorted15".bam"
bam16=$sorted16".bam"
bai1=$bam1".bai"
bai2=$bam2".bai"
bai3=$bam3".bai"
bai4=$bam4".bai"
bai5=$bam5".bai"
bai6=$bam6".bai"
bai7=$bam7".bai"
bai8=$bam8".bai"
bai9=$bam9".bai"
bai10=$bam10".bai"
bai11=$bam11".bai"
bai12=$bam12".bai"
bai13=$bam13".bai"
bai14=$bam14".bai"
bai15=$bam15".bai"
bai16=$bam16".bai"
pileup1=$spec1$lib1".pileup"
pileup2=$spec1$lib2".pileup"
pileup3=$spec1$lib3".pileup"
pileup4=$spec1$lib4".pileup"
pileup5=$spec2$lib1".pileup"
pileup6=$spec2$lib2".pileup"
pileup7=$spec2$lib3".pileup"
pileup8=$spec2$lib4".pileup"
pileup9=$spec3$lib1".pileup"
pileup10=$spec3$lib2".pileup"
pileup11=$spec3$lib3".pileup"
pileup12=$spec3$lib4".pileup"
pileup13=$spec4$lib1".pileup"
pileup14=$spec4$lib2".pileup"
pileup15=$spec4$lib3".pileup"
pileup16=$spec4$lib4".pileup"
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
#
#SAMTOOLS script start
echo starting SAMTOOLS
#samtools faidx preparing tab delimited file for samtools view
samtools faidx $ref1
samtools faidx $ref2
samtools faidx $ref3
samtools faidx $ref4
samtools view -S -F 0x4 -b -u -t $fai1 $out1 | samtools sort - $sorted1
samtools index $bam1 $bai1
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $bam1 > $pileup1
#rm out1
samtools view -S -F 0x4 -b -u -t $fai1 $out2 | samtools sort - $sorted2
samtools index $bam2 $bai2
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $bam2 > $pileup2
#rm out2
samtools view -S -F 0x4 -b -u -t $fai1 $out3 | samtools sort - $sorted3
samtools index $bam3 $bai3
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $bam3 > $pileup3
#rm out3
samtools view -S -F 0x4 -b -u -t $fai1 $out4 | samtools sort - $sorted4
samtools index $bam4 $bai4
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $bam4 > $pileup4
#rm out4
samtools view -S -F 0x4 -b -u -t $fai2 $out5 | samtools sort - $sorted5
samtools index $bam5 $bai5
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $bam5 > $pileup5
#rm out5
samtools view -S -F 0x4 -b -u -t $fai2 $out6 | samtools sort - $sorted6
samtools index $bam6 $bai6
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $bam6 > $pileup6
#rm out6
samtools view -S -F 0x4 -b -u -t $fai2 $out7 | samtools sort - $sorted7
samtools index $bam7 $bai7
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $bam7 > $pileup7
#rm out7
samtools view -S -F 0x4 -b -u -t $fai2 $out8 | samtools sort - $sorted8
samtools index $bam8 $bai8
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $bam8 > $pileup8
#rm out8
samtools view -S -F 0x4 -b -u -t $fai3 $out9 | samtools sort - $sorted9
samtools index $bam9 $bai9
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $bam9 > $pileup9
#rm out9
samtools view -S -F 0x4 -b -u -t $fai3 $out10 | samtools sort - $sorted10
samtools index $bam10 $bai10
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $bam10 > $pileup10
#rm out10
samtools view -S -F 0x4 -b -u -t $fai3 $out11 | samtools sort - $sorted11
samtools index $bam11 $bai11
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $bam11 > $pileup11
#rm out11
samtools view -S -F 0x4 -b -u -t $fai3 $out12 | samtools sort - $sorted12
samtools index $bam12 $bai12
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $bam12 > $pileup12
#rm out12
samtools view -S -F 0x4 -b -u -t $fai4 $out13 | samtools sort - $sorted13
samtools index $bam13 $bai13
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $bam13 > $pileup13
#rm out13
samtools view -S -F 0x4 -b -u -t $fai4 $out14 | samtools sort - $sorted14
samtools index $bam14 $bai14
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $bam14 > $pileup14
#rm out14
samtools view -S -F 0x4 -b -u -t $fai4 $out15 | samtools sort - $sorted15
samtools index $bam15 $bai15
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $bam15 > $pileup15
#rm out15
samtools view -S -F 0x4 -b -u -t $fai4 $out16 | samtools sort - $sorted16
samtools index $bam16 $bai16
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $bam16 > $pileup16
#rm out16









