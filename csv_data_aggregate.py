import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#データを集計して、表示する
print("数学の最高点 =", df["数学"].max())
print("数学の最低点 =", df["数学"].min())
print("数学の平均点 =", df["数学"].mean())
print("数学の中央値 =", df["数学"].median())
print("数学の合計点 =", df["数学"].sum())
