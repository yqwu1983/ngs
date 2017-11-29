#!/bin/bash
#!/bin/bash
folder='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/'
adapters='/home/nenarokova/tools/bbmap/resources/adapters.fa'

fw=$folder'18021_1_7_unmerged_fw.fq'
rv=$folder'18021_1_7_unmerged_rv.fq'
trimmed_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18021_1_7_unmerged_trimmed_fw.fq'
trimmed_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18021_1_7_unmerged_trimmed_rv.fq'

/home/nenarokova/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv minlen=50 qtrim=rl trimq=20 ktrim=r k=25 mink=11 ref=$adapters hdist=1


fw=$folder'18098_1_7_unmerged_fw.fq'
rv=$folder'18098_1_7_unmerged_rv.fq'
trimmed_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18098_1_7_unmerged_trimmed_fw.fq'
trimmed_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18098_1_7_unmerged_trimmed_rv.fq'

/home/nenarokova/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv minlen=50 qtrim=rl trimq=20 ktrim=r k=25 mink=11 ref=$adapters hdist=1
