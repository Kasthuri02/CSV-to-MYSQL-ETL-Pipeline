import pandas as pd
import mysql.connector
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)



print("MySQL connection successful!")

# Read cleaned CSV
df = pd.read_csv("ETL_project/data/cleaned_orders.csv")

print(df.head())

cursor = connection.cursor()

sql = """
INSERT INTO orders
(order_id, customer_id, customer_name, product, quantity, price, order_date, city, total_amount)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    values = (
        row["order_id"],
        row["customer_id"],
        row["customer_name"],
        row["product"],
        row["quantity"],
        row["price"],
        row["order_date"],
        row["city"],
        row["total_amount"]
    )

    cursor.execute(sql, values)

connection.commit()

print("Data loaded successfully!")