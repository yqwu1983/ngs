#!/usr/bin/ruby
f_path = '/home/anna/Dropbox/PhD/bioinformatics/genomes/reference_proteomes/ogs_mito.csv'
l = IO.readlines(f_path)
puts l.uniq.length
l.uniq.each { |e| puts "#{e} - #{l.count(e)}" }
