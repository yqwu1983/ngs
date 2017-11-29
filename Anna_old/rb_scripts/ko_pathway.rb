#!/usr/bin/ruby
def ko_pathway(file_in, file_out)
    result = {}
    cur_sym = nil
    File.readlines(file_in).each do |l|
      if l =~ /K\d+\n/
        result[cur_sym] ||= []
        result[cur_sym] << l
      else
        cur_sym = l
      end
    end
    a = File.open(file_out, 'w')
    result.each { |k,v| v.each { |val| a.puts "#{val.gsub("\n", '')} #{k}" }  }
end

file_in = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/organellar proteome annotation/Mito/ko_categories.txt'
file_out = '/home/anna/Dropbox/phd/bioinformatics/genomes/euglena/organellar proteome annotation/Mito/ko_categories_out.txt'
