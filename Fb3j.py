#Tech-Gym-11-11
#アンサンブル学習：ランダムフォレスト、勾配ブースティング

# データやモデルを構築するためのライブラリ等のインポート
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split

#性能評価
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# データを読み込み
cancer = load_breast_cancer()

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(
                                                    cancer.data, cancer.target, test_size=0.5, random_state=66)

models = {
    'RandomForest': RandomForestClassifier(random_state=0,n_estimators=1000),
    'GradientBoost': GradientBoostingClassifier(random_state=0)
}

scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    scores[(model_name, 'train_score')] = model.score(X_train, y_train)
    scores[(model_name, 'test_score')] = model.score(X_test, y_test)
    
    #性能評価
    y_pred = model.predict(X_test)
    scores[(model_name, 'accuracy_score')] = accuracy_score(y_test, y_pred)
    scores[(model_name, 'precision_score')] = precision_score(y_test, y_pred)
    scores[(model_name, 'recall_score')] = recall_score(y_test, y_pred)
    scores[(model_name, 'f1_score')] = f1_score(y_test, y_pred)

#表示
display(pd.Series(scores).unstack())

