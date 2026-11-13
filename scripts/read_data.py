
import pandas as pd
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent
input_file = BASE_DIR / "data" / "orders.csv"
output_file = BASE_DIR / "data" / "cleaned_orders.csv"

# 1. Read raw CSV
df = pd.read_csv(input_file)

print("Original row count:", len(df))
print(df.head())

# 2. Basic information
df.info()

# 3. Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 4. Check and remove exact duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# 5. Handle missing values
df["quantity"] = df["quantity"].fillna(1)
df["price"] = df["price"].fillna(800)

# Handle missing text fields
for col in ["customer_name", "product", "city"]:
    df[col] = df[col].fillna("Unknown")

# 6. Convert numeric columns
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# 7. Remove invalid quantities and prices
df = df.dropna(subset=["quantity", "price"])
df = df[(df["quantity"] > 0) & (df["price"] >= 0)]

# 8. Check duplicate order IDs
print("\nDuplicate order IDs:", df["order_id"].duplicated().sum())

# Keep the first record for each order ID
df = df.drop_duplicates(subset=["order_id"], keep="first")

# 9. Convert dates; handle mixed formats
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce", format="mixed", dayfirst=True
)

# Remove records with invalid dates or missing order IDs
df = df.dropna(subset=["order_id", "order_date"])

# 10. Calculate total amount
df["total_amount"] = (df["quantity"] * df["price"]).round(2)

# 11. Final validation
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal row count:", len(df))
print("Remaining duplicate rows:", df.duplicated().sum())

# 12. Save cleaned data
df.to_csv(output_file, index=False)
print("Duplicate order IDs after cleaning:", df["order_id"].duplicated().sum())

print("\nCleaned data saved successfully!")
print("Output file:", output_file)
