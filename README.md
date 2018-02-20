# JIRA to Chatwork webhook integration cgi
JIRAからChatworkに更新を投げるcgi  
仕事で使いたいからでっちあげた

## USAGE
- 適当に配備して実行権限
## 設定
- ポスト先ルームidの設定(複数ルームへの投稿に対応している)
```
ROOMIDS = ['xxx','xxx']
```
- APIキー(適宜取得して設定)
```
APIKEY = "xxxxx"
```
  
## 複数JIRAのプロジェクトがある場合
適当にcgiの名前変えて配備すればよろし
