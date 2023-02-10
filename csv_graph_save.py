import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("sample.csv", index_col=0)

#縦棒グラフを画像ファイルとして出力する
df.T.plot.bar()
plt.savefig("bargraph.png")
