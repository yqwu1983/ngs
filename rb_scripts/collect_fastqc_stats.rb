#!/usr/bin/ruby
require 'csv'

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

def get_length(file)
    f = File.open(file, "r")
    total_length = 0
    re_header = /#Length\tCount/
    re_count = /(?<l1>\d+)-(?<l2>\d+)\t(?<n>(\d{2,}\.\d)|(\d\.\d+E\d+))/
    in_len_block = false
    f.each_line do |line|
        if in_len_block
            if re_count =~ line
                match = line.match(re_count)
                avl = (match[:l1].to_f + match[:l2].to_f)/2.0
                total_length += avl * match[:n].to_f
            else
                break
        elsif re_header =~ line
            in_len_block = true
        end
    end
    f.close
    return total_length
end

def analyze_folder(folder, outfile)
    Dir.chdir(folder)
    result = []
    Dir.glob("*output*.log").each do file
        re_name = /(?<name>\S+?)_output_/
        name = file.match(re_name)[:name]
    end
    write_hash_array(result, outfile)
end

folder=''
outfile=''
analyze_folder(folder, outfile)
