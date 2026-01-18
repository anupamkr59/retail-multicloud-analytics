import pandas as pd
import os

# -------- PATHS --------
INPUT_PATH = "data/raw/payments/2026/01/13/payments.csv"
OUTPUT_PATH = "data/curated/payments/curated_payments.csv"

# -------- READ --------
df = pd.read_csv(INPUT_PATH)

# -------- CLEANING --------
# Standardize status
df["payment_status"] = df["payment_status"].str.upper()

# Convert amount to numeric
df["payment_amount"] = pd.to_numeric(df["payment_amount"], errors="coerce")

# Keep only positive amounts
df = df[df["payment_amount"].notna()]
df = df[df["payment_amount"] > 0]

# Valid payment dates
df["payment_date"] = pd.to_datetime(df["payment_date"], errors="coerce")
df = df[df["payment_date"].notna()]

# Trim string columns
for col in ["payment_id", "order_id", "payment_method"]:
    df[col] = df[col].astype(str).str.strip()

# -------- WRITE --------
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print("CURATED PAYMENTS BUILD COMPLETED")
print(f"Input records   : {len(pd.read_csv(INPUT_PATH))}")
print(f"Curated records : {len(df)}")
print(f"Output path     : {OUTPUT_PATH}")
