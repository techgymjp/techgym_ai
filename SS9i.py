#AI-TECHGYM-2-5-A-3
#特徴量エンジニアリング

#インポート
import pandas as pd
import scipy.stats as sp
from sklearn.preprocessing import RobustScaler
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#行列
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

#標準化
rs = RobustScaler()
rs.fit(matrix)
matrix_rs = rs.transform(matrix)
df_matrix_rs = pd.DataFrame(matrix_rs)
display(df_matrix_rs)

#検算
display(df_matrix_rs.describe())

#ロジスティック回帰
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify = cancer.target, random_state=0)

model = LogisticRegression(random_state=0,solver='liblinear')
model.fit(X_train,y_train)

print("標準化前")
print('正解率(train):{:.3f}'.format(model.score(X_train, y_train)))
print('正解率(test):{:.3f}'.format(model.score(X_test, y_test)))

#ロバスト
rs.fit(X_train)
X_train_std = rs.transform(X_train)
X_test_std = rs.transform(X_test)

model = LogisticRegression(random_state=0,solver='liblinear')
model.fit(X_train_std,y_train)

print("標準化後")
print('正解率(train):{:.3f}'.format(model.score(X_train_std, y_train)))
print('正解率(test):{:.3f}'.format(model.score(X_test_std, y_test)))

score_up_train = model.score(X_train_std, y_train) - model.score(X_train, y_train)
score_up_test = model.score(X_test_std, y_test) - model.score(X_test, y_test)

print("差分")
print('正解率(train):{:.3f}'.format(score_up_train))
print('正解率(test):{:.3f}'.format(score_up_test))
