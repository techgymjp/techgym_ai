import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree


df = pd.read_csv("heart.csv")

df_train, df_test = train_test_split(df, test_size=0.2, random_state=25)

target       = df_train["target"].values
features_one = df_train[["trestbps", "chol", "thalach"]].values
max_depth         = 10
min_samples_split = 5
tree_fit = tree.DecisionTreeClassifier(max_depth = max_depth, min_samples_split = min_samples_split, random_state = 1).fit(features_one, target)

test_features = df_test[["trestbps", "chol", "thalach"]].values

tree_prediction = tree_fit.predict(test_features)

patient_id = np.array(df_test.index).astype(int)

tree_solution = pd.DataFrame(tree_prediction, patient_id, columns = ["target"])

tree_solution.to_csv("my_tree_one.csv", index_label = ["patient_id"])
