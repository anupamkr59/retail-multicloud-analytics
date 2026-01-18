import pandas as pd
import os

# -------- PATHS --------
INPUT_PATH = "data/raw/stores/2026/01/12/stores.csv"
OUTPUT_PATH = "data/curated/stores/curated_stores.csv"

# -------- READ --------
df = pd.read_csv(INPUT_PATH)

# -------- CLEANING --------

# store_id must exist
df = df[df["store_id"].notna()]

# standardize store_type
df["store_type"] = (
    df["store_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# standardize region
df["region"] = (
    df["region"]
    .astype(str)
    .str.strip()
    .str.title()
)

# remove duplicates
df = df.drop_duplicates(subset=["store_id"])

# -------- WRITE --------
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

print("CURATED STORES BUILD COMPLETED")
print(f"Input records   : {len(pd.read_csv(INPUT_PATH))}")
print(f"Curated records : {len(df)}")
print(f"Output path     : {OUTPUT_PATH}")
