import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#行データの追加
df.loc[0] = ["木村", 95, 83, 77, 62, 89]
print(df)
