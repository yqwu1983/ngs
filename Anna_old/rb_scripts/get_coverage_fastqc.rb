#!/usr/bin/ruby
require 'csv'

def get_read_length(file)
    f = File.open(file, "r")
    total_length = 0
    re_header = /#Length\tCount/
    re_count = /(?<l1>\d+)-(?<l2>\d+)\t(?<n>(\d{2,}\.\d)|(\d\.\d+E\d+))/
    in_len_block = false

    f.each_line do |line|
        if in_len_block
            if line =~ re_count
                match = line.match(re_count)
                avl = (match[:l1].to_f + match[:l2].to_f)/2.0
                total_length += avl * match[:n].to_f
            else
                break
            end

        elsif line =~ re_header
            in_len_block = true
        end
    end
    f.close

    total_length
end

def write_hash_array(data, file, keys=nil)
    CSV.open(file, "wb") do |csv|
        if not keys
            keys = data.first.keys
            csv << keys
        end
        data.each do |element|
            csv << keys.map{ |k| element[k] }
        end
    end
end


# folder = "/media/4TB1/kinetoplastids_hinxton/illumina/miseq/fastqc_results/zip/trimmed_reads"
# results = []
# re_folder = /(?<name>(18021|18098)_\d#\d)_(paired|unpaired)_out_(fw|rv)_(?<params>(?<adapter>(ad_)?)q(?<qual>\d+)_l(?<minlen>\d+)_fastqc)\//
# Dir.chdir(folder)
# Dir.glob('*/').group_by { |e| m = e.match(re_folder); { name: m[:name], adapter: m[:adapter], qual: m[:qual], minlen: m[:minlen] } }.each do |opts, dirs|
#         result = opts
#         result[:read_length] = 0
#         dirs.each do |dir|
#             result[:read_length] += get_read_length("#{dir}/fastqc_data.txt")
#         end
#     results << result
# end
# puts results
# file = '/media/4TB1/kinetoplastids_hinxton/illumina/miseq/fastqc_results/trimmed_miseq_read_length.csv'
# write_hash_array(results, file)

folder = "/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/fastqc_results/zip/trimmed_reads"
results = []
re_folder = /(?<name>(19109_\d#\d)|(E262))_(paired|unpaired)_out_(fw|rv)_(?<params>(?<adapter>(ad_)?)q(?<qual>\d+)_l(?<minlen>\d+)_fastqc)\//
Dir.chdir(folder)

grouped_dirs = Dir.glob('*/').group_by do |e|
    puts "working with #{e}"
    m = e.match(re_folder)
    { name: m[:name], adapter: m[:adapter], qual: m[:qual], minlen: m[:minlen] }
end

grouped_dirs.each do |opts, dirs|
        result = opts
        result[:read_length] = 0
        dirs.each do |dir|
            result[:read_length] += get_read_length("#{dir}/fastqc_data.txt")
        end
    results << result
end
puts results
file = '/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/fastqc_results/trimmed_hiseq_read_length.csv'
write_hash_array(results, file)
