import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


df = pd.read_csv("titanic_train.csv")

train, true = train_test_split(df, test_size=0.2, random_state=25)
result = pd.read_csv("my_svm_result_2.csv")

# 結果と正解データをソートする
result = result.sort_values(by=["PassengerId"])
true   = true.sort_values(by=["PassengerId"]).loc[:,['PassengerId','Survived']]

print("ライブラリバージョン")
print("accuracy", accuracy_score(true["Survived"], result["Survived"]))
print("precision", precision_score(true["Survived"], result["Survived"]))
print("recall", recall_score(true["Survived"], result["Survived"]))


labels   = ["TN", "FP", "FN", "TP"]
validate = pd.merge(true, result, how="left", on="PassengerId")

labels_count  = {"TN" : 0, "FN" : 0, "FP" : 0, "TP" : 0}

# ラベルを追加
for index, row in validate.iterrows():
  x = row["Survived_x"]
  y = row["Survived_y"]
  # ラベルからTP, TN, FN, FPの数をカウント
  labels_count[labels[int(str(x)+str(y), 2)]] = labels_count[labels[int(str(x)+str(y), 2)]] + 1


accuracy  = (labels_count["TP"] + labels_count["TN"])/(labels_count["TP"] + labels_count["FP"] + labels_count["TN"] + labels_count["FN"]) 
precision = labels_count["TP"] / (labels_count["TP"] + labels_count["FP"])
recall    = labels_count["TP"] / (labels_count["TP"] + labels_count["FN"])
print("オリジナルバージョン")
print("accuracy", accuracy)
print("precision", precision)
print("recall", recall)
