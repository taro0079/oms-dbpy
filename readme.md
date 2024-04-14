# このツールは何
csvをデータベースに流し込むツールです。

# 使い方
## dockerを利用する場合
1. main.pyの中のデータベース設定を変更してください。主にhostの修正が必要かと。
2. 以下のコマンドを実行してください。
```bash
docker compose build
docker compose run --rm python3 python3 main.py -c csv_file.csv -t table_name -p id
```

## dockerを利用しない場合のインストール方法
python 3.12がインストールされていることを前提とします。
```bash
pip install -r requirements.txt
```


# TODO
- [ ]  database configuration
- [ ]  write test
