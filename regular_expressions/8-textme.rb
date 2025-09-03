#!/usr/bin/env ruby
log = ARGV[0]
regex = /\[FROM:(.*?)\] \[TO:(.*?)\] \[FLAGS:(.*?)\]/
match = log.match(regex)
if match
  puts "#{match[1]},#{match[2]},#{match[3]}"
end
