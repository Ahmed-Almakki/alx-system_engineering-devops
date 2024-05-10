#!/usr/bin/env ruby
puts ARGV[0].scan(/^[\S a-zA-Z\-\.\@\+]{10}/).join
