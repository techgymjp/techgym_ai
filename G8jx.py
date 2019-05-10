import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("heart.csv")

df_train, df_test = train_test_split(df, test_size=0.2, random_state=25)

target       = df_train["target"].values
features_one = df_train[["trestbps"]].values
logistic_fit = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(features_one, target)

test_features = df_test[["trestbps"]].values

logi_prediction = logistic_fit.predict(test_features)

patient_id = np.array(df_test.index).astype(int)

logi_solution = pd.DataFrame(logi_prediction, patient_id, columns = ["target"])

logi_solution.to_csv("my_logi_one.csv", index_label = ["patient_id"])
