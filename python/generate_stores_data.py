import pandas as pd
import random
import os

# ---------------- CONFIG ----------------
NUM_STORES = 500

store_types = ["Online", "Physical", "online", None]
regions = ["North", "South", "East", "West", None]



# ---------------- DATA ----------------
data = []

for i in range(1, NUM_STORES + 1):
    record = {
        "store_id": f"S{i}",
        "store_type": random.choice(store_types),
        "region": random.choice(regions),
        "manager_id": f"M{random.randint(1, 50)}",
        
    }
    data.append(record)

df = pd.DataFrame(data)

# ---------------- WRITE ----------------
output_path = "data/raw/stores/2026/01/12/stores.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

df.to_csv(output_path, index=False)

print("SCRIPT STARTED")
print(f"Stores dataset generated with {len(df)} records")
print(f"File written at: {output_path}")
print("SCRIPT EXECUTED SUCCESSFULLY")
