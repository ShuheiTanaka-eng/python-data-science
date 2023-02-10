import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")

#国語の点数が高い順にソートする
sort = df.sort_values("国語", ascending=False)
#文字コードを指定してCSVファイルに出力する
sort.to_csv("sample_sort.csv", encoding="utf_8_sig")
