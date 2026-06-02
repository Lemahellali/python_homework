import sqlite3
import pandas as pd

data = {
    "line_item_id": [1, 2, 3, 4, 5],
    "quantity": [2, 1, 4, 3, 2],
    "product_id": [101, 102, 101, 103, 102],
    "product_name": ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse"],
    "price": [1000, 50, 1000, 80, 50]
}

df = pd.DataFrame(data)

print(df.head())

df["total"] = df["quantity"] * df["price"]

print("\nDataFrame with total column:")
print(df.head())


summary_df = df.groupby("product_id").agg({
    "line_item_id": "count",
    "total": "sum",
    "product_name": "first"
})

print("\nGrouped Data:")
print(summary_df.head())


summary_df = summary_df.sort_values("product_name")

print("\nSorted Data:")
print(summary_df)


summary_df.to_csv("order_summary.csv")

print("\nCSV file created successfully.")