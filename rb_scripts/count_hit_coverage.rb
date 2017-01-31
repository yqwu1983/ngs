#!/usr/bin/ruby
require 'csv'

blast_csv_path='/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/blasto_kika/scaffolds_tr_bl_report_plants.csv'

def merge_ranges(ranges)
  ranges = ranges.sort_by {|r| r.first }
  *outages = ranges.shift
  ranges.each do |r|
    lastr = outages[-1]
    if lastr.last >= r.first - 1
      outages[-1] = lastr.first..[r.last, lastr.last].max
    else
      outages.push(r)
    end
  end
  outages
end

blast_csv = CSV.read(blast_csv_path)
all_seqs = {}

blast_csv = blast_csv[1..-1]
blast_csv.each do |e|
    all_seqs[e.first] ||= []
    all_seqs[e.first] << { start: e[10].to_i, end: e[11].to_i }
end

result = {}

all_seqs.each do |id, intervals|
    intervals = intervals.map { |i| i[:start]..i[:end] }
    intervals = merge_ranges(intervals)

    result[id] ||= {}
    result[id][:ranges] = merge_ranges(intervals)
    result[id][:size] = intervals.map(&:size).inject(0){ |sum,x| sum + x }
end

result = result.sort
result.each do |key, v|
    puts "#{key},#{v[:size]}"
end
