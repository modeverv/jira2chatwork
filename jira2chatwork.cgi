#! /usr/bin/env ruby
# -*- coding:utf-8 -*-

####################################
#
# CONFIG
#
# QUERY: keyで渡される課題IDを識別するためののキー
# ROOMS: POST対象のChatworkのルームID配列(複数対応)
# ex https://www.chatwork.com/#!rid12345 の場合12345
SETTING = { DEV: {
              QUERY: "DEV",
              ROOMS: ['12345']
            }
          }
# APIKEYは適宜取得して設定してください
APIKEY  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# JIRAのURLを設定してください
# ex) https://example.com/jira/browse/
JIRAURL = "https://example.com/jira/browse/"
####################################

require 'cgi'
require 'uri'
require 'net/http'

print "Content-Type: text/html\n\n"

def get_target_rooms(key)
  SETTING.each do |key,value|
    if key =~ /#{value[:QUERY]}/
      return value[:ROOMS]
    end
  end
  return []
end

####################################
# main
####################################
cgi = CGI.new
params = cgi.params
key = params['key'][0]
rooms = get_target_rooms(key)
message = "body=[info][title]JIRA UPDATE[/title]#{JIRAURL}#{key}[/info]"

rooms.each do |rid|
  uri = URI.parse("https://api.chatwork.com/v2/rooms/#{rid}/messages")
  https = Net::HTTP.new(uri.host, uri.port)
  # https.set_debug_output $stderr
  https.use_ssl = true
  req = Net::HTTP::Post.new(uri.request_uri)
  req["X-ChatWorkToken"] = APIKEY
  req.body = message
  res = https.request(req)
  puts "code:#{res.code} / msg:#{res.message} / body:#{res.body}"
end

puts "<br/>script execution has successfully finished"
