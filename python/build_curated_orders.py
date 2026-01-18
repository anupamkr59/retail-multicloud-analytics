import pandas as pd
import os

# -------- PATHS --------
INPUT_PATH = "data/curated/orders/valid_orders.csv"
OUTPUT_PATH = "data/curated/orders/curated_orders.csv"

# -------- READ --------
df = pd.read_csv(INPUT_PATH)

# -------- CLEAN & STANDARDIZE --------
# Order status
df["order_status"] = df["order_status"].str.upper()

# Order amount (keep only positive)
df = df[df["order_amount"].notna()]
df = df[df["order_amount"] > 0]

# Dates
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df = df[df["order_date"].notna()]

# Trim strings
for col in ["customer_id", "store_id", "region"]:
    df[col] = df[col].astype(str).str.strip()

# -------- WRITE --------
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print("CURATED LAYER BUILD COMPLETED")
print(f"Input records : {len(pd.read_csv(INPUT_PATH))}")
print(f"Curated records: {len(df)}")
print(f"Output path   : {OUTPUT_PATH}")
