import pandas as pd
import os

# -------- PATHS --------
INPUT_PATH = "data/raw/customers/2026/01/12/customers.csv"
OUTPUT_PATH = "data/curated/customers/curated_customers.csv"

# -------- READ --------
df = pd.read_csv(INPUT_PATH)

# -------- CLEANING --------

# customer_id must exist
df = df[df["customer_id"].notna()]

# standardize customer_type
df["customer_type"] = (
    df["customer_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# standardize loyalty_tier
df["loyalty_tier"] = (
    df["loyalty_tier"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# standardize city and state
df["city"] = df["city"].astype(str).str.strip().str.title()
df["state"] = df["state"].astype(str).str.strip().str.title()

# remove duplicates (keep latest record per customer)
df = df.drop_duplicates(subset=["customer_id"], keep="last")

# -------- WRITE --------
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print("CURATED CUSTOMERS BUILD COMPLETED")
print(f"Input records   : {len(pd.read_csv(INPUT_PATH))}")
print(f"Curated records : {len(df)}")
print(f"Output path     : {OUTPUT_PATH}")
