import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT
    orders.order_id,
    customers.customer_name,
    products.product_name,
    line_items.quantity,
    products.price,
    line_items.quantity * products.price AS total
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN line_items
ON orders.order_id = line_items.order_id
JOIN products
ON line_items.product_id = products.product_id;
"""

df = pd.read_sql_query(query, conn)

print(df.head())

summary_df = df.groupby("product_name").agg({
    "quantity": "sum",
    "total": "sum"
})

print("\nGrouped Data:")
print(summary_df)

conn.close()