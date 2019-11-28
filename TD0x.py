#AI-TECHGYM-2-11-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

#ファイルがなければ前の問題を実施する
title = "FIFA_data_pre2.csv"
if not os.path.exists(title):
    print("Run Previous problem.")
else :
    print(title + " EXIST.")
    df=pd.read_csv('./FIFA_data_pre2.csv')

#スタイル指定
plt.style.use('fivethirtyeight')
sns.set(style = "dark", palette = "colorblind", color_codes = True)

#不要な列を削除する
drop_cols = df.columns[28:54]
df = df.drop(drop_cols, axis = 1)
df = df.drop(['Unnamed: 0','Unnamed: 0.1','ID','Jersey Number','Joined','Loaned From',
              'Body Type', 'Release Clause','Contract Valid Until','LS','ST',
              'Value','Name','Club'], axis = 1)

#作成した特徴量
df_p = df[['Defending','General','Mental','Passing','Mobility','Power','Shooting','Overall']]

target = df_p['Overall']
df_t = df_p.drop(['Overall'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(df_t, target, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#結果の表示
print('決定係数(train):{:.3f}'.format(model.score(X_train,y_train)))
print('決定係数(test):{:.3f}'.format(model.score(X_test,y_test)))
print('RMSE :{:.3f} '.format(np.sqrt(mean_squared_error(y_test, predictions))))
