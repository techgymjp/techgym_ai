import pandas as pd
import numpy as np

df     = pd.read_csv("pg_data.csv", header=None)
new_df = pd.DataFrame(columns=["row", "vector"])
values = df[0].values

