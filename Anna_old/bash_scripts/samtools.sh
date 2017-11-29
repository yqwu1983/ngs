#!/bin/bash
##applies for sequences stored on Trypka server
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
sorted1=$spec1$lib1"_sorted.bam"
sorted2=$spec1$lib2"_sorted.bam"
sorted3=$spec1$lib3"_sorted.bam"
sorted4=$spec1$lib4"_sorted.bam"
sorted5=$spec2$lib1"_sorted.bam"
sorted6=$spec2$lib2"_sorted.bam"
sorted7=$spec2$lib3"_sorted.bam"
sorted8=$spec2$lib4"_sorted.bam"
sorted9=$spec3$lib1"_sorted.bam"
sorted10=$spec3$lib2"_sorted.bam"
sorted11=$spec3$lib3"_sorted.bam"
sorted12=$spec3$lib4"_sorted.bam"
sorted13=$spec4$lib1"_sorted.bam"
sorted14=$spec4$lib2"_sorted.bam"
sorted15=$spec4$lib3"_sorted.bam"
sorted16=$spec4$lib4"_sorted.bam"
bai1=$sorted1".bai"
bai2=$sorted2".bai"
bai3=$sorted3".bai"
bai4=$sorted4".bai"
bai5=$sorted5".bai"
bai6=$sorted6".bai"
bai7=$sorted7".bai"
bai8=$sorted8".bai"
bai9=$sorted9".bai"
bai10=$sorted10".bai"
bai11=$sorted11".bai"
bai12=$sorted12".bai"
bai13=$sorted13".bai"
bai14=$sorted14".bai"
bai15=$sorted15".bai"
bai16=$sorted16".bai"
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
#mapPacBio script starting
cd /home/tomas/CUL13/Virus_search
#SAMTOOLS script start
echo starting SAMTOOLS
samtools faidx $ref1
samtools faidx $ref2
samtools faidx $ref3
samtools faidx $ref4
samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out1 | samtools sort --output-fmt BAM --threads 32 - -o $sorted1
samtools index -b $sorted1
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted1 > $pileup1
#rm out1
samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out2 | samtools sort --output-fmt BAM --threads 32 - -o $sorted2
samtools index -b $sorted2
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted2 > $pileup2
#rm out2
samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out3 | samtools sort --output-fmt BAM --threads 32 - -o $sorted3
samtools index -b $sorted3
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted3 > $pileup3
#rm out3
samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out4 | samtools sort --output-fmt BAM --threads 32 - -o $sorted4
samtools index -b $sorted4
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted4 > $pileup4
#rm out4
samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out5 | samtools sort --output-fmt BAM --threads 32 - -o $sorted5
samtools index -b $sorted5
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted5 > $pileup5
#rm out5
samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out6 | samtools sort --output-fmt BAM --threads 32 - -o $sorted6
samtools index -b $sorted6
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted6 > $pileup6
#rm out6
samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out7 | samtools sort --output-fmt BAM --threads 32 - -o $sorted7
samtools index -b $sorted7
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted7 > $pileup7
#rm out7
samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out8 | samtools sort --output-fmt BAM --threads 32 - -o $sorted8
samtools index -b $sorted8
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted8 > $pileup8
#rm out8
samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out9 | samtools sort --output-fmt BAM --threads 32 - -o $sorted9
samtools index -b $sorted9
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted9 > $pileup9
#rm out9
samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out10 | samtools sort --output-fmt BAM --threads 32 - -o $sorted10
samtools index -b $sorted10
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted10 > $pileup10
#rm out10
samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out11 | samtools sort --output-fmt BAM --threads 32 - -o $sorted11
samtools index -b $sorted11
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted11 > $pileup11
#rm out11
samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out12 | samtools sort --output-fmt BAM --threads 32 - -o $sorted12
samtools index -b $sorted12
samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted12 > $pileup12
#rm out12
samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out13 | samtools sort --output-fmt BAM --threads 32 - -o $sorted13
samtools index -b $sorted13
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted13 > $pileup13
#rm out13
samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out14 | samtools sort --output-fmt BAM --threads 32 - -o $sorted14
samtools index -b $sorted14
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted14 > $pileup14
#rm out14
samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out15 | samtools sort --output-fmt BAM --threads 32 - -o $sorted15
samtools index -b $sorted15
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted15 > $pileup15
#rm out15
samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out16 | samtools sort --output-fmt BAM --threads 32 - -o $sorted16
samtools index -b $sorted16
samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted16 > $pileup16
#rm out16
