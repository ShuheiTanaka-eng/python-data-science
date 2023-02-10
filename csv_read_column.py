import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#列データの確認
print("国語のデータ\n", df["国語"])
print("理科と社会のデータ\n", df[["理科", "社会"]])
