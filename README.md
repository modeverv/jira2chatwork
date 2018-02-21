# JIRA to Chatwork integration cgi via JIRA's webhook
JIRAからChatworkに更新を投げるcgi  
仕事で使いたいからでっちあげた

## USAGE
適当に配備して実行権限

## 設定
```
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
```

## JIRA複数のプロジェクトがある場合
SETTINGにエントリを適宜追加してください
