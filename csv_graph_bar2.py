import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df = pd.read_csv("sample.csv", index_col=0)

#国語と数学の縦棒グラフ
df[["国語","数学"]].plot.bar()
plt.show()
