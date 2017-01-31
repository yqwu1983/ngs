#!/usr/bin/ruby
require 'thread/pool'

def run_in_pool(processes, threads)
    pool = Thread.pool(threads)
    processes.each do |process|
        pool.process do
            puts "executing #{process}"
            `#{process}`
        end
    end
    pool.shutdown
