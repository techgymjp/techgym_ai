#AI-TECHGYM-2-11-A-2
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

#カテゴリ変数のみ表示
display(df.select_dtypes(include=object))

#二値変数にする
def face_to_num(df):
    if (df['Real Face'] == 'Yes'):
        return 1
    else:
        return 0
    
#右利きか左利きかで二値変数にする
def right_footed(df):
    if (df['Preferred Foot'] == 'Right'):
        return 1
    else:
        return 0

#ポジションを分類する
def simple_position(df):
    if (df['Position'] == 'GK'):
        return 'GK'
    elif ((df['Position'] == 'RB')  | (df['Position'] == 'LB')  | (df['Position'] == 'CB')  | (df['Position'] == 'LCB') | (df['Position'] == 'RCB') | (df['Position'] == 'RWB') | (df['Position'] == 'LWB') ):
        return 'DF'
    elif ((df['Position'] == 'LDM') | (df['Position'] == 'CDM') | (df['Position'] == 'RDM')):
        return 'DM'
    elif ((df['Position'] == 'LM')  | (df['Position'] == 'LCM') | (df['Position'] == 'CM')  | (df['Position'] == 'RCM') | (df['Position'] == 'RM')):
        return 'MF'
    elif ((df['Position'] == 'LAM') | (df['Position'] == 'CAM') | (df['Position'] == 'RAM') | (df['Position'] == 'LW') | (df['Position'] == 'RW')):
        return 'AM'
    elif ((df['Position'] == 'RS')  | (df['Position'] == 'ST')  | (df['Position'] == 'LS')  | (df['Position'] == 'CF') | (df['Position'] == 'LF') | (df['Position'] == 'RF')):
        return 'ST'
    else:
        return df.Position

#各国の選手の数をカウントして250人以上いる国かどうかを判定する
nat_counts = df.Nationality.value_counts()
nat_list = nat_counts[nat_counts > 250].index.tolist()

#250人以上いるかどうかで二値変数にする
def major_nation(df):
    if (df.Nationality in nat_list):
        return 1
    else:
        return 0

#操作のためにコピーする
df1 = df.copy()

#新しいColumnをつくる
df1['Real_Face'] = df1.apply(face_to_num, axis=1)
df1['Right_Foot'] = df1.apply(right_footed, axis=1)
df1['Simple_Position'] = df1.apply(simple_position,axis = 1)
df1['Major_Nation'] = df1.apply(major_nation,axis = 1)

#文字で分ける
tempwork = df1["Work Rate"].str.split("/ ", n = 1, expand = True)

#分けたものを追加する
df1["WorkRate1"] = tempwork[0]
df1["WorkRate2"] = tempwork[1]

#文字列で分離
Height_num = df1["Height"].str.split("'", n = 1, expand = True)
df1["Height_feet"] = Height_num[0]
df1["Height_inch"] = Height_num[1]

#型変換
df1 = df1.astype({'Height_feet': 'float32', 'Height_inch': 'float32'})

#cmに変換 : 1feet=30.48cm , 1inch=2.54cm
df1["Height_cm"] = df1["Height_feet"] * 30.48 + df1["Height_inch"] * 2.54

#もともとのColumnを除く
df1 = df1.drop(['Height','Height_feet','Height_inch'], axis = 1)
df1 = df1.drop(['Work Rate','Preferred Foot','Real Face','Position','Nationality'], axis = 1)

#目的変数と説明変数の分離
target = df1.Overall
df2 = df1.drop(['Overall'], axis = 1)

#データ分割
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df2, target, test_size=0.2)

#One Hot Encoding
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

#モデル予測値
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#予測結果
print('決定係数(train):{:.3f}'.format(model.score(X_train,y_train)))
print('決定係数(test):{:.3f}'.format(model.score(X_test,y_test)))
print('RMSE :{:.3f} '.format(np.sqrt(mean_squared_error(y_test, predictions))))

#グラフ化
plt.figure(figsize=(15,5))
sns.regplot(predictions,y_test,scatter_kws={'alpha':0.3,'color':'lime'},line_kws={'color':'b','alpha':0.5})
plt.xlabel('Predictions', fontsize = 16)
plt.ylabel('Overall', fontsize = 16)
plt.title("Linear Prediction of Player Rating",fontsize = 20)
plt.show()

