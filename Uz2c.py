import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

df = pd.read_csv("heart.csv")

df_train, df_test = train_test_split(df, test_size=0.2, random_state=25)

true_set = df_test["target"]

logi_pred_set = pd.read_csv("my_logi_one.csv")
tree_pred_set = pd.read_csv("my_tree_one.csv")

