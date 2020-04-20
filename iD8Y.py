#AI-TECHGYM-4-10-A
#実践ビジネスデータ分析

#インポート
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

# 警告(worning)の非表示化
import warnings
warnings.filterwarnings('ignore')

#利用履歴
log_df = pd.read_csv('log.csv')

#作成した顧客データ
customer = pd.read_csv('customer_join.csv')

#年月ごと顧客ごとに集計する
log_df["usedate"] = pd.to_datetime(log_df["usedate"])
log_df["年月"] = log_df["usedate"].dt.strftime("%Y%m")
uselog_months = log_df.groupby(["年月","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]

#過去6ヶ月の利用データを集計する
year_months = list(uselog_months["年月"].unique())
predict_data = pd.DataFrame()
for i in range(6, 11):
    tmp = uselog_months.loc[uselog_months["年月"]==year_months[i]]
    tmp.rename(columns={"count":"count_pred"}, inplace=True)
    for j in range(1, 7):
        tmp_before = uselog_months.loc[uselog_months["年月"]==year_months[i-j]]
        del tmp_before["年月"]
        tmp_before.rename(columns={"count":"count_{}".format(j-1)}, inplace=True)
        tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
    predict_data = pd.concat([predict_data, tmp], ignore_index=True)

#退会してしまったユーザーは欠損値になる
predict_data = predict_data.dropna()
predict_data = predict_data.reset_index(drop=True)


#特徴量として会員期間を付与する
predict_data = pd.merge(predict_data, customer[["customer_id","start_date"]], on="customer_id", how="left")
predict_data["now_date"] = pd.to_datetime(predict_data["年月"], format="%Y%m")
predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
from dateutil.relativedelta import relativedelta
predict_data["period"] = None
for i in range(len(predict_data)):
    delta = relativedelta(predict_data["now_date"][i], predict_data["start_date"][i])
    predict_data["period"][i] = delta.years*12 + delta.months

######

#新規ユーザーにしぼる
predict_data = predict_data.loc[predict_data["start_date"]>=pd.to_datetime("20180401")]

#モデル作成
from sklearn import linear_model
import sklearn.model_selection

#モデル
model = linear_model.LinearRegression()

#目的変数と説明変数
X = predict_data[["count_0","count_1","count_2","count_3","count_4","count_5","period"]]
y = predict_data["count_pred"]

#データ分割
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)
model.fit(X_train, y_train)

#精度検証
print("正解率(train)",model.score(X_train, y_train))
print("正解率(test)",model.score(X_test, y_test))

#モデルに寄与している変数(回帰係数)
coef = pd.DataFrame({"feature_names":X.columns, "coefficient":model.coef_})
display(coef)
print("過去にさかのぼるほど寄与率が低くなっている、前月の利用回数が最も影響がる")

#新しい顧客の利用回数
x1 = [3, 4, 4, 6, 8, 7, 8]
x2 = [2, 2, 3, 3, 4, 6, 8]
x_pred = [x1, x2]

#モデルで予測する
print("新しいユーザーの予測利用回数",model.predict(x_pred))

#作成したデータを保存する
uselog_months.to_csv("use_log_months.csv",index=False)
