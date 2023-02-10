import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")

#読み込んだデータの確認
print("データの件数 =", len(df))
print("項目名　　　 =", df.columns.values)
print("インデックス =", df.index.values)
