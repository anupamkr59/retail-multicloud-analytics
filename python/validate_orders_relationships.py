import pandas as pd
import os

# ---------------- PATH CONFIG ----------------
ORDERS_PATH = "data/raw/orders/2026/01/11/orders.csv"
CUSTOMERS_PATH = "data/raw/customers/2026/01/12/customers.csv"
STORES_PATH = "data/raw/stores/2026/01/12/stores.csv"

OUTPUT_VALID_PATH = "data/curated/orders/valid_orders.csv"
OUTPUT_INVALID_PATH = "data/curated/orders/invalid_orders.csv"

# ---------------- READ DATA ----------------
orders_df = pd.read_csv(ORDERS_PATH)
customers_df = pd.read_csv(CUSTOMERS_PATH)
stores_df = pd.read_csv(STORES_PATH)

# ---------------- BASIC CLEANING ----------------
orders_df["customer_id"] = orders_df["customer_id"].astype(str)
customers_df["customer_id"] = customers_df["customer_id"].astype(str)
stores_df["store_id"] = stores_df["store_id"].astype(str)

# Deduplicate dimension tables on business keys
customers_df = customers_df.drop_duplicates(subset=["customer_id"])
stores_df = stores_df.drop_duplicates(subset=["store_id"])

# ---------------- RELATIONSHIP CHECKS ----------------

# 1️⃣ Orders with missing customers
orders_with_customers = orders_df.merge(
    customers_df[["customer_id"]],
    on="customer_id",
    how="left",
    indicator=True
)

orders_with_customers["customer_valid"] = (
    orders_with_customers["_merge"] == "both"
)

orders_with_customers.drop(columns=["_merge"], inplace=True)

# 2️⃣ Orders with missing stores
orders_with_stores = orders_with_customers.merge(
    stores_df[["store_id"]],
    on="store_id",
    how="left",
    indicator=True
)

orders_with_stores["store_valid"] = (
    orders_with_stores["_merge"] == "both"
)

orders_with_stores.drop(columns=["_merge"], inplace=True)

# ---------------- FINAL CLASSIFICATION ----------------
orders_with_stores["record_status"] = orders_with_stores.apply(
    lambda row: "VALID"
    if row["customer_valid"] and row["store_valid"]
    else "INVALID",
    axis=1
)

valid_orders = orders_with_stores[
    orders_with_stores["record_status"] == "VALID"
]

invalid_orders = orders_with_stores[
    orders_with_stores["record_status"] == "INVALID"
]

# ---------------- WRITE OUTPUT ----------------
os.makedirs(os.path.dirname(OUTPUT_VALID_PATH), exist_ok=True)

valid_orders.to_csv(OUTPUT_VALID_PATH, index=False)
invalid_orders.to_csv(OUTPUT_INVALID_PATH, index=False)

# ---------------- SUMMARY ----------------
print("RELATIONSHIP VALIDATION COMPLETED")
print(f"Total orders       : {len(orders_df)}")
print(f"Valid orders       : {len(valid_orders)}")
print(f"Invalid orders     : {len(invalid_orders)}")
print(f"Valid output path  : {OUTPUT_VALID_PATH}")
print(f"Invalid output path: {OUTPUT_INVALID_PATH}")
