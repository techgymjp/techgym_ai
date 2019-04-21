import pandas as pd
import numpy as np

df     = pd.read_csv("pg_data.csv", header=None)
new_df = pd.DataFrame(columns=["row", "vector"])
values = df[0].values

for i, row in enumerate(values):
    vector    = [0] * len(values)
    vector[i] = 1
    tmp_se    = pd.Series([row, vector], index=new_df.columns)
    new_df    = new_df.append(tmp_se, ignore_index=True)

print(new_df)
