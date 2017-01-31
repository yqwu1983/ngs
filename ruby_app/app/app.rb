require_relative '../config/application.rb'

(0..10).to_a.map {|e| (0..5).to_a.map{|q| ('A'..'Z').to_a.sample}.join }.each do |name|
    puts "creating #{name}"
    Sequence.create name: name
end
