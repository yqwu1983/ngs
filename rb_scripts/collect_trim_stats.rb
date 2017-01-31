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

def extract_stats(file)
    f = File.open(file, "r")
    re_name = /(?<name>\S+?)_output_/
    name = file.match(re_name)[:name]
    stats = {'name' => name}
    re_params = /-threads (.+?)(?<adapters>ILLUMINACLIP:(.+))?LEADING:\d+ TRAILING:\d+ SLIDINGWINDOW:\d+:(?<quality>\d+) MINLEN:(?<minlen>\d+)/
    re_reads = /Input Read Pairs: (?<total>\d+) Both Surviving: (?<both>\d+) \((?<both%>\d+.\d+)%\) Forward Only Surviving: (?<forward>\d+) \((?<forward%>\d+.\d+)%\) Reverse Only Surviving: (?<reverse>\d+) \((?<reverse%>\d+.\d+)%\) Dropped: (?<dropped>\d+) \((?<dropped%>\d+.\d+)%\)/

    f.each_line do |line|
        if re_params =~ line
            match = line.match(re_params)
            param_stats = Hash[ match.names.zip( match.captures ) ]
            stats.merge!(param_stats)
        elsif re_reads =~ line
            match = line.match(re_reads)
            trim_stats = Hash[ match.names.zip( match.captures ) ]
            stats.merge!(trim_stats)
        end
    end
    f.close
    return stats
end

def analyze_folder(folder, outfile)
    Dir.chdir(folder)
    result = []
    Dir.glob("*output*.log").each{ |f| result << extract_stats(f) }
    write_hash_array(result, outfile)
end

folder='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/trimming_logs/short_logs'
outfile='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/trimming_logs/analysis.csv'
analyze_folder(folder, outfile)
