# 画像解析サービス
## 動かし方
### GCPアカウント作成
GCP（Google Cloud Platform）のアカウント登録がが必要です。
アカウント登録後、認証用の秘密鍵を生成して環境変数に追加する必要があります。詳しくはドキュメントを参照してください。  
https://cloud.google.com/vision/docs/libraries?hl=ja#setting_up_authentication  
この記事も参考になります。  
https://qiita.com/ysda/items/67c983510f4d7d1c6982

### クローン
このリポジトリをローカルにクローンし、visionブランチをチェックアウトしてください。  
PyCharmのターミナルから以下のコマンドを入力し、必要なライブラリをインストールします。

```
pip install -r requirements.txt
```

DBのマイグレーションを行います。  
※ログイン機能は用意していないので、createsuperuserは不要です。

```
python manage.py makemigrations vision
python manage.py migrate
```

runserverを実行し、[http://127.0.0.1:8000/vision/]()にアクセスする。