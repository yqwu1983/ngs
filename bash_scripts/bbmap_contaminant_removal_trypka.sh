#!/bin/bash
##applies for sequences stored on Trypka server
working_dir='/media/4TB3/Tomas_data/Pconfusum_filtered_reads_wo_H10_contamination/RNAseq_bbmap'
#genomic_PE=''
#genomic_MP=''
transcriptomic_polyA='/media/4TB3/Tomas_data/Pconfusum_filtered_reads_wo_H10_contamination/RNAseq_bbmap/CUL13MS_polyA_clean_wo_H10_contamination.fq'
transcriptomic_ribominus='/media/4TB3/Tomas_data/Pconfusum_filtered_reads_wo_H10_contamination/RNAseq_bbmap/CUL13MS_ribominus_clean_wo_H10_contamination.fq'
spec1='H10_contaminant'
spec2='CUL13MS'
#spec3=''
#spec4=''
ref1='Lpyr_ass_v6.fa'
ref2='Paratrypanosoma_PE_MP_Newbler_500bp_up_v1.fa'
#ref3=$spec3".fas"
#ref4=$spec4".fas"
#lib1='_PE'
#lib2='_MP'
lib3='_polyA'
lib4='_ribominus'
#out1=$spec1$lib1".sam"
#out2=$spec1$lib2".sam"
#out3=$spec1$lib3".sam"
#out4=$spec1$lib4".sam"
out5=$spec2$lib3".sam"
out6=$spec2$lib4".sam"
#outm1=$spec1$lib1"_mapped_only.fq"
#outm2=$spec1$lib2"_mapped_only.fq"
#outm3=$spec1$lib3"_mapped_only.fq"
#outm4=$spec1$lib4"_mapped_only.fq"
outm5=$spec2$lib3"_mapped_only.fq"
outm6=$spec2$lib4"_mapped_only.fq"
#outu1=$spec1$lib1"_unmapped_only.fq"
#outu2=$spec1$lib2"_unmapped_only.fq"
#outu3=$spec1$lib3"_unmapped_only.fq"
#outu4=$spec1$lib4"_unmapped_only.fq"
outu5=$spec2$lib3"_unmapped_only.fq"
outu6=$spec2$lib4"_unmapped_only.fq"
#covstats1=$spec1$lib1"_covstats.txt"
#covstats2=$spec1$lib2"_covstats.txt"
#covstats3=$spec1$lib3"_covstats.txt"
#covstats4=$spec1$lib4"_covstats.txt"
covstats5=$spec2$lib3"_covstats.txt"
covstats6=$spec2$lib4"_covstats.txt"
#covhist1=$spec1$lib1"_covhist.txt"
#covhist2=$spec1$lib2"_covhist.txt"
#covhist3=$spec1$lib3"_covhist.txt"
#covhist4=$spec1$lib4"_covhist.txt"
covhist5=$spec2$lib3"_covhist.txt"
covhist6=$spec2$lib4"_covhist.txt"
#basecov1=$spec1$lib1"_basecov.txt"
#basecov2=$spec1$lib2"_basecov.txt"
#basecov3=$spec1$lib3"_basecov.txt"
#basecov4=$spec1$lib4"_basecov.txt"
basecov5=$spec2$lib3"_basecov.txt"
basecov6=$spec2$lib4"_basecov.txt"
#bincov1=$spec1$lib1"_bincov.txt"
#bincov2=$spec1$lib2"_bincov.txt"
#bincov3=$spec1$lib3"_bincov.txt"
#bincov4=$spec1$lib4"_bincov.txt"
bincov5=$spec2$lib3"_bincov.txt"
bincov6=$spec2$lib4"_bincov.txt"
#SAMTOOLS variables
fai1=$ref1".fai"
fai2=$ref2".fai"
fai3=$ref3".fai"
fai4=$ref4".fai"
sorted1=$spec1$lib1".sorted"
sorted2=$spec1$lib2".sorted"
sorted3=$spec1$lib3".sorted"
sorted4=$spec1$lib4".sorted"
bam1=$sorted1".bam"
bam2=$sorted2".bam"
bam3=$sorted3".bam"
bam4=$sorted4".bam"
bai1=$bam1".bai"
bai2=$bam2".bai"
bai3=$bam3".bai"
bai4=$bam4".bai"
pileup1=$spec1$lib1".pileup"
pileup2=$spec1$lib2".pileup"
pileup3=$spec1$lib3".pileup"
pileup4=$spec1$lib4".pileup"
##
#echo starting bbmap mappings
cd $working_dir
#To map with super-high sensitivity (useful for very-low-quality data, or remote homologies) with statistics:
#mapPacBio.sh in=reads.fq out=mapped.sam outm=mapped.fq vslow k=8 maxindel=200 minratio=0.1 covstats=covstats.txt covhist=covhist1.txt basecov=basecov.txt bincov=bincov.txt
#To map with high sensitivity with mapped reads in fastaq and statistics:
#bbmap.sh in=$genomic_PE ref=$ref1 nodisk out=$out1 outm=$outm1 slow k=12 covstats=$covstats1 covhist=$covhist1 basecov=$basecov1 bincov=$bincov1
#bbmap.sh in=$genomic_MP ref=$ref1 nodisk out=$out2 outm=$outm2 slow k=12 covstats=$covstats2 covhist=$covhist2 basecov=$basecov2 bincov=$bincov2
#To map quickly with very high precision and lower sensitivity, as when removing contaminant reads specific to a genome without risking false-positives:
#bbmap.sh in=$transcriptomic_polyA ref=$ref1 nodisk out=$out3 outm=$outm3 outu=$outu3 minratio=0.9 maxindel=3 bwr=0.16 bw=12 fast minhits=2 qtrim=r trimq=10 untrim idtag printunmappedcount kfilter=25 maxsites=1 k=14 covstats=$covstats3 covhist=$covhist3 basecov=$basecov3 bincov=$bincov3
#bbmap.sh in=$transcriptomic_ribominus ref=$ref1 nodisk out=$out4 outm=$outm4 outu=$outu4 minratio=0.9 maxindel=3 bwr=0.16 bw=12 fast minhits=2 qtrim=r trimq=10 untrim idtag printunmappedcount kfilter=25 maxsites=1 k=14 covstats=$covstats4 covhist=$covhist4 basecov=$basecov4 bincov=$bincov4
#
bbmap.sh in=$transcriptomic_polyA ref=$ref2 nodisk out=$out5 outm=$outm5 outu=$outu5 minratio=0.9 maxindel=3 bwr=0.16 bw=12 fast minhits=2 qtrim=r trimq=10 untrim idtag printunmappedcount kfilter=25 maxsites=1 k=14 covstats=$covstats5 covhist=$covhist5 basecov=$basecov5 bincov=$bincov5
bbmap.sh in=$transcriptomic_ribominus ref=$ref2 nodisk out=$out6 outm=$outm6 outu=$outu6 minratio=0.9 maxindel=3 bwr=0.16 bw=12 fast minhits=2 qtrim=r trimq=10 untrim idtag printunmappedcount kfilter=25 maxsites=1 k=14 covstats=$covstats6 covhist=$covhist6 basecov=$basecov6 bincov=$bincov6
##SAMTOOLS script start
#echo starting SAMTOOLS
#cd $working_dir
##samtools faidx preparing tab delimited file for samtools view
samtools faidx $ref1
samtools faidx $ref2
#samtools faidx $ref3
#samtools faidx $ref4
#samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out1 | samtools sort --output-fmt BAM --threads 32 - -o $sorted1
#samtools index -b $sorted1
#samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted1 > $pileup1
##rm out1
#samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out2 | samtools sort --output-fmt BAM --threads 32 - -o $sorted2
#samtools index -b $sorted2
#samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted2 > $pileup2
##rm out2
samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out3 | samtools sort --output-fmt BAM --threads 32 - -o $sorted3
samtools index -b $sorted3
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted3 > $pileup3
rm out3
samtools view -@ 32 -F 0x4 -b -u -t $fai1 $out4 | samtools sort --output-fmt BAM --threads 32 - -o $sorted4
samtools index -b $sorted4
samtools mpileup -u -f $ref1 -P solexa -F 0.1 $sorted4 > $pileup4
rm out4
samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out5 | samtools sort --output-fmt BAM --threads 32 - -o $sorted5
samtools index -b $sorted5
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted5 > $pileup5
rm out5
samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out6 | samtools sort --output-fmt BAM --threads 32 - -o $sorted6
samtools index -b $sorted6
samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted6 > $pileup6
rm out6
#samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out7 | samtools sort --output-fmt BAM --threads 32 - -o $sorted7
#samtools index -b $sorted7
#samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted7 > $pileup7
##rm out7
#samtools view -@ 32 -F 0x4 -b -u -t $fai2 $out8 | samtools sort --output-fmt BAM --threads 32 - -o $sorted8
#samtools index -b $sorted8
#samtools mpileup -u -f $ref2 -P solexa -F 0.1 $sorted8 > $pileup8
##rm out8
#samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out9 | samtools sort --output-fmt BAM --threads 32 - -o $sorted9
#samtools index -b $sorted9
#samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted9 > $pileup9
##rm out9
#samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out10 | samtools sort --output-fmt BAM --threads 32 - -o $sorted10
#samtools index -b $sorted10
#samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted10 > $pileup10
##rm out10
#samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out11 | samtools sort --output-fmt BAM --threads 32 - -o $sorted11
#samtools index -b $sorted11
#samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted11 > $pileup11
##rm out11
#samtools view -@ 32 -F 0x4 -b -u -t $fai3 $out12 | samtools sort --output-fmt BAM --threads 32 - -o $sorted12
#samtools index -b $sorted12
#samtools mpileup -u -f $ref3 -P solexa -F 0.1 $sorted12 > $pileup12
##rm out12
#samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out13 | samtools sort --output-fmt BAM --threads 32 - -o $sorted13
#samtools index -b $sorted13
#samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted13 > $pileup13
##rm out13
#samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out14 | samtools sort --output-fmt BAM --threads 32 - -o $sorted14
#samtools index -b $sorted14
#samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted14 > $pileup14
##rm out14
#samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out15 | samtools sort --output-fmt BAM --threads 32 - -o $sorted15
#samtools index -b $sorted15
#samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted15 > $pileup15
##rm out15
#samtools view -@ 32 -F 0x4 -b -u -t $fai4 $out16 | samtools sort --output-fmt BAM --threads 32 - -o $sorted16
#samtools index -b $sorted16
#samtools mpileup -u -f $ref4 -P solexa -F 0.1 $sorted16 > $pileup16
##rm out16









