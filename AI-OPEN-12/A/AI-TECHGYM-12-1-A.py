#techgym-AI-12-1-A

#import
import sys
import pandas as pd
import sqlite3

#データベースの読み込み
conn = sqlite3.connect("./test.db")
df = pd.read_sql_query('SELECT * FROM users', conn)
display(df)

conn.close()
