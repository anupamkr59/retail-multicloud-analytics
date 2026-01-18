import pandas as pd
import random
import os

# ---------------- CONFIGURATION ----------------
NUM_CUSTOMERS = 8000

customer_types = ["Retail", "Wholesale", None]
loyalty_tiers = ["Gold", "Silver", "Bronze", "GOLD", "silver", None]
cities = ["Delhi", "Mumbai", "Bangalore", "Kolkata", None]
states = ["Delhi", "Maharashtra", "Karnataka", "West Bengal"]

# ---------------- DATA GENERATION ----------------
data = []

for i in range(1, NUM_CUSTOMERS + 1):
    customer_id = f"C{random.randint(1, 6000)}"  # duplicates by design

    record = {
        "customer_id": customer_id,
        "customer_name": f"Customer_{customer_id}",
        "customer_type": random.choice(customer_types),
        "city": random.choice(cities),
        "state": random.choice(states),
        "loyalty_tier": random.choice(loyalty_tiers)
    }

    data.append(record)

df = pd.DataFrame(data)

# ---------------- WRITE TO RAW LAYER ----------------
output_path = "data/raw/customers/2026/01/12/customers.csv"

# Create directories if they don't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

df.to_csv(output_path, index=False)

print("SCRIPT STARTED")
print(f"Customers dataset generated with {len(df)} records")
print(f"File written at: {output_path}")
print("SCRIPT EXECUTED SUCCESSFULLY")
