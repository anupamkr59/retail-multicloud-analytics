print("SCRIPT STARTED")
import pandas as pd
import random
from datetime import datetime, timedelta

#configuration
NUM_RECORDS = 10000
START_DATE = datetime(2025,1,1)

regions = ["North", "South", "East", "West"]
statuses = ["Approved", "Pending", "Cancelled", "approved", "PENDING", None]
store_ids = [f"S{i}" for i in range(1, 600)] + [None]

data = []

for i in range(1, NUM_RECORDS + 1):
    order_date = START_DATE + timedelta(days=random.randint(0,365))

    record = {
        "order_id": i if random.random() > 0.02 else i - 1, #duplicates
        "order_date": order_date.strftime("%Y-%m-%d") if random.random() > 0.03 else "invalid_date",
        "customer_id": f"C{random.randint(1, 3000)}",
        "store_id": random.choice(store_ids),
        "region": random.choice(regions + [None]),
        "order_amount": random.choice([
            random.randint(500, 5000),
            -100,          #invalid
            None           #null
        ]),
        "order_status": random.choice(statuses)
    }
    data.append(record)

df = pd.DataFrame(data)

output_path = "data/raw/orders/2026/01/11/orders.csv"
df.to_csv(output_path, index=False)

print(f"Generated {len(df)} records at {output_path}")

print("SCRIPT EXECUTED SUCCESSFULLY")

if __name__ == "__main__":
    print("MAIN EXECUTION STARTED")
