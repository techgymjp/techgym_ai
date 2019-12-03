#AI-TECHGYM-2-9-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

#ファイルがなければ前の問題を実施する
title = "FIFA_data_pre.csv"
if not os.path.exists(title):
    print("Run Previous problem.")
else :
    print(title + " EXIST.")
    df=pd.read_csv('./FIFA_data_pre.csv')

#スタイルの指定
plt.style.use('fivethirtyeight')
sns.set(style = "dark", palette = "colorblind", color_codes = True)

#必要に応じて表示
#display(df.head())
#display(df.columns)

#利き足の数
plt.figure(figsize = (15, 5))
ax = sns.countplot(df['Preferred Foot'], palette = 'pink')
ax.set_title('Most Preferred Foot of the Players', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

#ポジション分布
plt.figure(figsize = (15, 5))
ax = sns.countplot('Position', data = df, palette = 'bone')
ax.set_xlabel(xlabel = 'Different Positions in Football', fontsize = 16)
ax.set_ylabel(ylabel = 'Count of Players', fontsize = 16)
ax.set_title(label = 'Comparison of Positions and Players', fontsize = 20)
plt.tick_params(labelsize = 13)
plt.show()

#背の高さ
plt.figure(figsize = (15, 5))
ax = sns.countplot(x = 'Height', data = df, palette = 'dark')
ax.set_xlabel(xlabel = 'Height in Foot per inch', fontsize = 16)
ax.set_ylabel(ylabel = 'Count', fontsize = 16)
ax.set_title(label = 'Count of players on Basis of Height', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

#特別なスコア
plt.figure(figsize = (15, 5))
ax = sns.distplot(df['Special'], bins = 58, kde = True, color = 'r')
ax.set_xlabel(xlabel = 'Special score range', fontsize = 16)
ax.set_ylabel(ylabel = 'Count of the Players',fontsize = 16)
ax.set_title(label = 'Histogram for the Speciality Scores of the Players', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

#ポテンシャル
plt.figure(figsize = (15, 5))
ax = sns.distplot(df['Potential'], bins = 48, kde = True, color = 'y')
ax.set_xlabel(xlabel = "Player\'s Potential Scores", fontsize = 16)
ax.set_ylabel(ylabel = 'Number of players', fontsize = 16)
ax.set_title(label = 'Histogram of players Potential Scores', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

#年齢
plt.figure(figsize = (15, 5))
ax = sns.distplot(df['Age'], bins = 58, kde = True, color = 'g')
ax.set_xlabel(xlabel = "Player\'s age", fontsize = 16)
ax.set_ylabel(ylabel = 'Number of players', fontsize = 16)
ax.set_title(label = 'Histogram of players age', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

#国別のプレイヤーの数
df['Nationality'].value_counts().head(50).plot.bar(color = 'orange', figsize = (15, 5))
plt.title('Different Nations Participating', fontsize = 20, fontweight = 20)
plt.xlabel('Name of The Country',fontsize = 16)
plt.ylabel('count',fontsize = 16)
plt.tick_params(labelsize = 16)
plt.show()
