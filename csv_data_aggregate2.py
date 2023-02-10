import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#条件に合ったデータの個数を集計する
print("数学が80点以上のデータ件数 =", len(df[df["数学"]>=80]))
