import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#行データの追加
df.loc[5] = ["斉藤", 79, 91, 85, 87, 74]
#列データの削除
df = df.drop("理科", axis=1)
print(df)
