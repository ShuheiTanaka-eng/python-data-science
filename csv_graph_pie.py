import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("sample.csv", index_col=0)

#国語の円グラフ
df["国語"].plot.pie()
plt.show()
