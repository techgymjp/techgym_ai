#AI-TECHGYM-2-10-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

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
    
selected_columns = ['Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value',
                    'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot',
                    'Skill Moves', 'Work Rate', 'Body Type', 'Position', 'Height', 'Weight',
                    'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                    'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                    'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                    'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                    'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                    'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                    'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']
#データフレーム
data_selected = pd.DataFrame(df, columns = selected_columns)

#相関係数のヒートマップ
plt.figure(figsize = (20,20))
sns.heatmap(data_selected.corr(),linewidths=0.1,linecolor='black',square=True,cmap='summer')
plt.title('Histogram of the Dataset', fontsize = 15)
plt.show()

#年齢とレーティングの関係
plt.figure(figsize = (15,5))
sns.lineplot(df['Age'], df['Rating'], palette = 'Wistia')
plt.title('Age vs Rating', fontsize = 20)
plt.show()

#上位9ヶ国の選手の体重の分布
some_countries = ['England','Germany','Spain','Argentina','France','Brazil','Italy','Columbia','Japan']
data_countries = df.loc[df['Nationality'].isin(some_countries)
plt.figure(figsize = (15,5))
ax = sns.violinplot(x = data_countries['Nationality'], y = data_countries['Weight'], palette = 'Blues')
ax.set_xlabel(xlabel = 'Countries', fontsize = 16)
ax.set_ylabel(ylabel = 'Weight in lbs', fontsize = 16)
ax.set_title(label = 'Distribution of Weight of players from different countries', fontsize = 20)
plt.show()

#クラブ別の総合値の分布
some_clubs = ('CD Leganés', 'Southampton', 'RC Celta', 'Empoli', 'Fortuna Düsseldorf', 'Manchestar City',
             'Tottenham Hotspur', 'FC Barcelona', 'Valencia CF', 'Chelsea', 'Real Madrid')

data_clubs = df.loc[df['Club'].isin(some_clubs) & df['Overall']]

plt.figure(figsize = (15,5))
ax = sns.boxplot(x = data_clubs['Club'], y = data_clubs['Overall'], palette = 'inferno')
ax.set_xlabel(xlabel = 'Some Popular Clubs', fontsize = 16)
ax.set_ylabel(ylabel = 'Overall Score', fontsize = 16)
ax.set_title(label = 'Distribution of Overall Score in Different popular Clubs', fontsize = 20)
plt.xticks(rotation = 90)
plt.tick_params(labelsize = 16)
plt.show()

#年齢とポテンシャルの分布
sns.jointplot(x = df['Age'],y = df['Potential'],
              joint_kws = {'alpha':0.1,'s':5,'color':'green'},
              marginal_kws = {'color':'green'},height=8)
plt.show()
