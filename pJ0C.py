#AI-TECHGYM-2-5-A-2
#特徴量エンジニアリング

#インポート
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify = cancer.target, random_state=0)

model = LogisticRegression(random_state=0,solver='liblinear')
model.fit(X_train,y_train)

print("標準化前")
print('正解率(train):{:.3f}'.format(model.score(X_train, y_train)))
print('正解率(test):{:.3f}'.format(model.score(X_test, y_test)))

#標準化
sc = MinMaxScaler()
sc.fit(X_train)
X_train_mms = sc.transform(X_train)
X_test_mms = sc.transform(X_test)

model_mms = LogisticRegression(random_state=0,solver='liblinear')
model_mms.fit(X_train_mms,y_train)

print("標準化後")
print('正解率(train):{:.3f}'.format(model_mms.score(X_train_mms, y_train)))
print('正解率(test):{:.3f}'.format(model_mms.score(X_test_mms, y_test)))

score_up_train = model_mms.score(X_train_mms, y_train) - model.score(X_train, y_train)
score_up_test = model_mms.score(X_test_mms, y_test) - model.score(X_test, y_test)

print("差分")
print('正解率(train):{:.3f}'.format(score_up_train))
print('正解率(test):{:.3f}'.format(score_up_test))
