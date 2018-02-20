#! /usr/bin/env ruby
# -*- coding:utf-8 -*-

####################################
#
# CONFIG
#
# 対象roomidを設定してください
# 例) https://www.chatwork.com/#!rid12345 の場合6012345
ROOMIDS = ['xxxxx']
# APIKEYは適宜取得して設定してください
APIKEY  = "xxxxxx"
####################################

require 'cgi'

cgi = CGI.new
params = cgi.params
key = params['key'][0]
url = "https://hoge.com/#{key}"
message = "[info][title]JIRA UPDATE[/title]#{url}[/info]"

print "Content-Type: text/html\n\n"

ROOMIDS.each do |rid|
  command = "curl -X POST -H \"X-ChatWorkToken: #{APIKEY}\" -d \"body=#{message}\" \"https://api.chatwork.com/v2/rooms/#{rid}/messages\""
  `#{command}`
end

puts "webhook has successfully finished"
