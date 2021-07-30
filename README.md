# flask_api_base

## 環境構築
### DBの起動
```
docker-compose up -d 
```
### パッケージのインストール
```
pipenv sync --dev
```
### migrationファイルの作成
```
pipenv run db_migrate
```
### migrationの実行
```
pipenv run db_upgrade
```
### migrationのrollback
```
pipenv run db_downgrade
```

## その他
### DBへのログイン
```
mysql -u root -h 127.0.0.1 -P 3306 -ppassword
```