import pandas as pd
import numpy as np

df     = pd.read_csv("pg_data.csv", header=None)
new_df = pd.DataFrame(columns=["row", "vector"])
values = df[0].values

necessary_bit = len(bin(len(values)).split("b")[1])

for i, row in enumerate(values):
    vector_str = format(i, "0" + str(necessary_bit) + "b")
    vector     = [0] * necessary_bit
    for j in range(necessary_bit):
       vector[j] = int(vector_str[j])

    tmp_se = pd.Series([row, vector], index=new_df.columns)
    new_df = new_df.append(tmp_se, ignore_index=True)

print(new_df)
