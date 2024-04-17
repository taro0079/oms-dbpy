# このツールは何
csvをデータベースに流し込むツールです。

# 使い方
## dockerを利用する場合
1. .envファイルに接続するdbの設定を書いてください。.env.exampleに例を書いています。
3. 以下のコマンドを実行してください。

```bash
docker compose build
docker compose run --rm python3 python3 main.py -c csv_file.csv -t table_name -p id
```
example
```bash
# 受注テーブルを取り込む場合の例
docker compose run --rm python3 python3 main.py -c trn_order.csv -t trn_order -p id
```

## dockerを利用しない場合のインストール方法
python 3.12がインストールされていることを前提とします。
```bash
pip install -r requirements.txt
```


# TODO
- [ ]  database configuration
- [ ]  write test
