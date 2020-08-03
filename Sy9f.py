#tech-gym-13-UP-3-Q
#センサーデータ分析

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# 温度データ
df = pd.read_csv("humiduity.csv")
#display(df)

#グラフ化
df = df.set_index('Time')

fig, ax = plt.subplots(figsize=(15, 10))

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, fontsize=10);
ax.scatter(df.index, df['Humidity'])

plt.show()

