import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")

#個別のデータの確認
print("土屋の国語データ =", df.loc[0]["国語"])
print("藤井の数学データ =", df.loc[3]["数学"])
