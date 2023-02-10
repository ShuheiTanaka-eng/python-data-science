import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("sample.csv", index_col=0)

#土屋の円グラフ
df.loc["土屋"].plot.pie()
plt.show()
