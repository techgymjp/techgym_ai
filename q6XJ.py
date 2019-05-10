import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("heart.csv")

df_train, df_test = train_test_split(df, test_size=0.2, random_state=25)

print("train : ", df_train.shape)
print("test : ", df_test.shape)
