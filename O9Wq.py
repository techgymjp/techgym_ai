#AI-TECHGYM-2-8-A-3
#特徴量エンジニアリング

#インポート
import pandas as pd
import os
import urllib.request

#ファイルがなければダウンロードする
title = "FIFA_data.csv"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
    urllib.request.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

df=pd.read_csv('./FIFA_data.csv')

#文字列データの補完
df['Club'].fillna('No Club', inplace = True)
df['Preferred Foot'].fillna('Right', inplace = True)
df['International Reputation'].fillna(1, inplace = True)
df['Weak Foot'].fillna(3, inplace = True)
df['Work Rate'].fillna('Medium/ Medium', inplace = True)
df['Body Type'].fillna('Normal', inplace = True)
df['Position'].fillna('ST', inplace = True)
df['Jersey Number'].fillna(8, inplace = True)
df['Joined'].fillna('Jul 1, 2018', inplace = True)
df['Loaned From'].fillna('None', inplace = True)
df['Contract Valid Until'].fillna(2019, inplace = True)
df['Height'].fillna("5'11", inplace = True)
df['Weight'].fillna('200lbs', inplace = True)
df['Wage'].fillna('€200K', inplace = True)
df['Release Clause'].fillna('€4.2M', inplace = True)

#数値の平均値での補間
df['Crossing'].fillna(df['Crossing'].mean(), inplace = True)
df['Finishing'].fillna(df['Finishing'].mean(), inplace = True)
df['HeadingAccuracy'].fillna(df['HeadingAccuracy'].mean(), inplace = True)
df['ShortPassing'].fillna(df['ShortPassing'].mean(), inplace = True)
df['Volleys'].fillna(df['Volleys'].mean(), inplace = True)
df['Dribbling'].fillna(df['Dribbling'].mean(), inplace = True)
df['Curve'].fillna(df['Curve'].mean(), inplace = True)
df['FKAccuracy'].fillna(df['FKAccuracy'], inplace = True)
df['LongPassing'].fillna(df['LongPassing'].mean(), inplace = True)
df['BallControl'].fillna(df['BallControl'].mean(), inplace = True)
df['Acceleration'].fillna(df['Acceleration'].mean(), inplace = True)
df['SprintSpeed'].fillna(df['SprintSpeed'].mean(), inplace = True)
df['Agility'].fillna(df['Agility'].mean(), inplace = True)
df['Reactions'].fillna(df['Reactions'].mean(), inplace = True)
df['Balance'].fillna(df['Balance'].mean(), inplace = True)
df['ShotPower'].fillna(df['ShotPower'].mean(), inplace = True)
df['Jumping'].fillna(df['Jumping'].mean(), inplace = True)
df['Stamina'].fillna(df['Stamina'].mean(), inplace = True)
df['Strength'].fillna(df['Strength'].mean(), inplace = True)
df['LongShots'].fillna(df['LongShots'].mean(), inplace = True)
df['Aggression'].fillna(df['Aggression'].mean(), inplace = True)
df['Interceptions'].fillna(df['Interceptions'].mean(), inplace = True)
df['Positioning'].fillna(df['Positioning'].mean(), inplace = True)
df['Vision'].fillna(df['Vision'].mean(), inplace = True)
df['Penalties'].fillna(df['Penalties'].mean(), inplace = True)
df['Composure'].fillna(df['Composure'].mean(), inplace = True)
df['Marking'].fillna(df['Marking'].mean(), inplace = True)
df['StandingTackle'].fillna(df['StandingTackle'].mean(), inplace = True)
df['SlidingTackle'].fillna(df['SlidingTackle'].mean(), inplace = True)
df['GKDiving'].fillna(df['GKDiving'].mean(), inplace = True)
df['GKHandling'].fillna(df['GKHandling'].mean(), inplace = True)
df['GKKicking'].fillna(df['GKKicking'].mean(), inplace = True)
df['GKPositioning'].fillna(df['GKPositioning'].mean(), inplace = True)
df['GKReflexes'].fillna(df['GKReflexes'].mean(), inplace = True)

#中央値での補完
df['Skill Moves'].fillna(df['Skill Moves'].median(), inplace = True)

#その他のNaNは0にする
df.fillna(0, inplace = True)

#不要な行を取り除く
df.drop(['Unnamed: 0','Photo','Flag','Club Logo'],axis=1,inplace=True)

#新しい特徴量を定義
def defending(data):
    return int(round((data[['Marking','StandingTackle','SlidingTackle']].mean()).mean()))

def general(data):
    return int(round((data[['HeadingAccuracy','Dribbling','Curve','BallControl']].mean()).mean()))

def mental(data):
    return int(round((data[['Aggression','Interceptions','Positioning','Vision','Composure']].mean()).mean()))

def passing(data):
    return int(round((data[['Crossing', 'ShortPassing','LongPassing']].mean()).mean()))

def mobility(data):
    return int(round((data[['Acceleration','SprintSpeed','Agility','Reactions']].mean()).mean()))

def power(data):
    return int(round((data[['Balance','Jumping','Stamina','Strength']].mean()).mean()))

def rating(data):
    return int(round((data[['Potential','Overall']].mean()).mean()))

def shooting(data):
    return int(round((data[['Finishing','Volleys','FKAccuracy','ShotPower','LongShots','Penalties']].mean()).mean()))

#すべての行に適用
df['Defending'] = df.apply(defending, axis = 1)
df['General'] = df.apply(general, axis = 1)
df['Mental'] = df.apply(mental, axis = 1)
df['Passing'] = df.apply(passing, axis = 1)
df['Mobility'] = df.apply(mobility, axis = 1)
df['Power'] = df.apply(power, axis = 1)
df['Rating'] = df.apply(rating, axis = 1)
df['Shooting'] = df.apply(shooting, axis = 1)

#CSVに書き出し
df.to_csv('./FIFA_data_pre.csv')

#必要に応じて表示
display(df.head())

#作成した特徴量
df_m = df[['Defending','General','Mental','Passing','Mobility','Power','Rating','Shooting']]

#ヒストグラム
df_m.hist()
plt.tight_layout() # グラフ同士が重ならないようにする
plt.show()
