#!/usr/bin/ruby
require 'thread/pool'
TRIM_EXEC = 'java -jar /home/nenarokova/tools/Trimmomatic-0.36/trimmomatic-0.36.jar'
# ADAPTERS_PATH = '/media/4TB1/kinetoplastids_hinxton/illumina_adapters.fa'
ADAPTERS_PATH = '/home/nenarokova/tools/Trimmomatic-0.36/adapters/all_adapters.fa'
PARAMS = {
    # 1 => { name: 'q15_l30', value: " LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30" },
    # 2 => { name: 'ad_q15_l30', value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:30" },
    # 3 => { name: 'ad_q15_l50', value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:50" },
    # 4 => { name: 'ad_q20_l30', value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30" },
    5 => { name: 'ad_q20_l50', value: "ILLUMINACLIP:#{ADAPTERS_PATH}:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:50" }
}.freeze

def run_program(folder, input_filename, params)
    file_fw = "#{folder}/raw_reads/#{input_filename}_1.fastq"
    file_rv = "#{folder}/raw_reads/#{input_filename}_2.fastq"

    p_out_fw = "#{folder}/trimmed_reads/#{input_filename}_#{params[:name]}_paired_out_fw.fastq"
    u_out_fw = "#{folder}/trimmed_reads/#{input_filename}_#{params[:name]}_unpaired_out_fw.fastq"
    p_out_rv = "#{folder}/trimmed_reads/#{input_filename}_#{params[:name]}_paired_out_rv.fastq"
    u_out_rv = "#{folder}/trimmed_reads/#{input_filename}_#{params[:name]}_unpaired_out_rv.fastq"
    trimming_log = "#{folder}/trimming_logs/#{input_filename}#{params[:name]}_trimming.log"
    output_log = "#{folder}/trimming_logs/#{input_filename}_#{params[:name]}_output.log"

    exec = "#{TRIM_EXEC} PE -threads 1 -trimlog #{trimming_log} #{file_fw} #{file_rv} #{p_out_fw} #{u_out_fw} #{p_out_rv} #{u_out_rv} #{params[:value]}"
    return "#{exec} &> #{output_log}"
end

def process_folders(folders)
    all_processes = []
    folders.each do |folder|
        Dir.glob("#{folder}/raw_reads/*.fastq").map{ |f| f.split('/').last.gsub(/_[12]\.fastq/, '') }.uniq.each do |name|
            PARAMS.each {|k,v| all_processes << run_program(folder, name, v)}
        end
    end
    return all_processes
end

def run_in_pool(processes, threads)
    pool = Thread.pool(threads)
    processes.each do |process|
        pool.process do
            puts "executing #{process}"
            `#{process}`
            puts ' ____________________________ '
        end
    end
    pool.shutdown
end

def perform(folders, threads)
    run_in_pool(process_folders(folders), threads)
end

# folders = [
#     '/media/4TB1/kinetoplastids_hinxton/illumina/miseq',
#     '/media/4TB1/kinetoplastids_hinxton/illumina/hiseq'
#         ]

folders = [
    '/home/nenarokova/contaminants'
]
threads = 16

perform(folders, threads)
