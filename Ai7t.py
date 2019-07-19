import pandas as pd
import numpy  as np
from sklearn  import svm

train      = pd.read_csv("titanic_train.csv")
test       = pd.read_csv("titanic_test.csv")

# 欠損値の補完
def comp_table(df):
  df["Age"]       = df["Age"].fillna(-0.5)
  # 0 => 値なし, 1 => 16歳以下の子供, 2 => 大人と定義
  df["Age_types"] = pd.cut(df["Age"],[-1, 0, 16, 100],labels=[0, 1, 2])
  df["Embarked"]  = df["Embarked"].fillna("S")
  df["Fare"]      = df["Fare"].fillna(test["Fare"].median())
  return df

train = comp_table(train)
train = train.drop("Cabin", axis=1)
test  = comp_table(test)
test  = test.drop("Cabin", axis=1)


# SVM
# 特徴量の抽出

# 学習
# 学習用のコードをここに記述

# モデル適用

# 出力関数
def output(result, df):
  # PassengerIdを取得
  PassengerId = np.array(df["PassengerId"]).astype(int)
  # my_prediction(予測データ）とPassengerIdをデータフレームへ落とし込む
  my_solution = pd.DataFrame(result, PassengerId, columns = ["Survived"])
  return my_solution

# my_tree_one.csvとして書き出し
output(my_svm_pred, test).to_csv("my_svm_result_1.csv", index_label = ["PassengerId"])
