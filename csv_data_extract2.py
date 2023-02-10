import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#複数の条件を組み合わせて抽出する
data = df[(df["国語"] >= 60) & (df["数学"] < 90)]
print(data)
