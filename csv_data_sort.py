import pandas as pd

#CSVファイルを読み込む
df = pd.read_csv("sample.csv")
pd.set_option('display.unicode.east_asian_width', True)

#理科の点数が高い順にソートする
sort1 = df.sort_values("理科", ascending=False)
print("理科の点数が高い順にソート\n", sort1)
#理科の点数が同点の場合にはさらに社会の点数が高い順にソートする
sort2 = df.sort_values(["理科","社会"], ascending=[False,False])
print("さらに社会の点数が高い順にソート\n", sort2)
