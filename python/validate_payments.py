import pandas as pd
import os

# -------- PATHS --------
ORDERS_PATH = "data/curated/orders/curated_orders.csv"
PAYMENTS_PATH = "data/raw/payments/2026/01/13/payments.csv"

VALID_PATH = "data/curated/payments/valid_payments.csv"
INVALID_PATH = "data/curated/payments/invalid_payments.csv"

# -------- READ --------
orders_df = pd.read_csv(ORDERS_PATH)
payments_df = pd.read_csv(PAYMENTS_PATH)

# -------- BASIC CLEANING --------
payments_df["order_id"] = payments_df["order_id"].astype(int)
orders_df["order_id"] = orders_df["order_id"].astype(int)

payments_df["payment_amount"] = pd.to_numeric(
    payments_df["payment_amount"], errors="coerce"
)

# -------- JOIN --------
df = payments_df.merge(
    orders_df[["order_id", "order_amount", "order_status"]],
    on="order_id",
    how="left",
    indicator=True
)

# -------- VALIDATION RULES --------
df["order_exists"] = df["_merge"] == "both"
df["amount_match"] = df["payment_amount"] == df["order_amount"]
df["payment_success"] = df["payment_status"] == "SUCCESS"

df["record_status"] = df.apply(
    lambda r: "VALID"
    if r["order_exists"]
    and r["payment_success"]
    and r["amount_match"]
    else "INVALID",
    axis=1
)

valid_df = df[df["record_status"] == "VALID"]
invalid_df = df[df["record_status"] == "INVALID"]

# -------- WRITE --------
os.makedirs(os.path.dirname(VALID_PATH), exist_ok=True)

valid_df.to_csv(VALID_PATH, index=False)
invalid_df.to_csv(INVALID_PATH, index=False)

# -------- SUMMARY --------
print("PAYMENT VALIDATION COMPLETED")
print(f"Total payments : {len(payments_df)}")
print(f"Valid payments : {len(valid_df)}")
print(f"Invalid payments : {len(invalid_df)}")
print(f"Valid path : {VALID_PATH}")
print(f"Invalid path : {INVALID_PATH}")
