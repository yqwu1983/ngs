#!/usr/bin/ruby
folder='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/'
Dir.glob("#{folder}raw_reads/*.fastq").map{ |f| f.split('/').last.gsub(/_[12]\.fastq/, '') }.uniq.each do |name|
    puts name
    file_fw = "#{folder}raw_reads/#{name}_1.fastq"
    file_rv = "#{folder}raw_reads/#{name}_2.fastq"
    merged = "#{folder}merged_reads/reads/#{name}_merged.fastq"
    unmerged_fw = "#{folder}merged_reads/reads/#{name}_unmerged_fw.fastq"
    unmerged_rv = "#{folder}merged_reads/reads/#{name}_unmerged_rv.fastq"
    bbmerge = '/home/nenarokova/tools/bbmap/bbmerge.sh'
    log = "#{folder}merged_reads/logs/#{name}_merged.txt"
    exec = "#{bbmerge} in1=#{file_fw} in2=#{file_rv} out=#{merged} outu1=#{unmerged_fw} outu2=#{unmerged_rv} strict=t qtrim2=t usejni=t > #{log}"
    puts exec
    `exec`
end
