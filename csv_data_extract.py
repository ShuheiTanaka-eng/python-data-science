import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#条件に合うデータを抽出する
data = df[df["国語"] >= 60]
print("国語が60点以上：\n", data)
data = df[df["数学"] < 90]
print("数学が90点未満：\n", data)
