import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("sample.csv", index_col=0)

#行と列を入れ替えた縦棒グラフ
df.T.plot.bar()
plt.show()
