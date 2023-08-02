#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(+?[0-9]*)\] \[to:(+?[0-9]*)\] \[flags:(.*?)\]/).join(",")
