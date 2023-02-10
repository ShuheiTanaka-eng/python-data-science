import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#行データの確認
print("加藤のデータ\n", df.loc[2])
print("鈴木と坂本のデータ\n", df.loc[[1, 4]])
