import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")

#国語の点数が高い順にソートする
sort = df.sort_values("国語", ascending=False)
#インデックスとヘッダーを削除して出力する
sort.to_csv("sample_sort.csv", index=False, header=False)
