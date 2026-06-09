import sqlite3
import pandas as pd

conn = sqlite3.connect("capstone.db")

# Change this filename if your CSV has a different name
df = pd.read_csv("csv/customers.csv")

df.to_sql("books", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")