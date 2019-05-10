import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree


df = pd.read_csv("heart.csv")

df_train, df_test = train_test_split(df, test_size=0.2, random_state=25)

