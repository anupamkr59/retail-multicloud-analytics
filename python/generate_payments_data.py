import pandas as pd
import random
import os
from datetime import datetime, timedelta

# -------- CONFIG --------
NUM_PAYMENTS = 9000

payment_methods = ["UPI", "CARD", "COD"]
payment_statuses = ["SUCCESS", "FAILED"]

data = []

for i in range(1, NUM_PAYMENTS + 1):
    order_id = random.randint(1, 10000)

    record = {
        "payment_id": f"P{i}",
        "order_id": order_id,
        "payment_method": random.choice(payment_methods),
        "payment_status": random.choice(payment_statuses),
        "payment_amount": random.choice([
            random.randint(500, 5000),
            random.randint(500, 5000),
            -100,     # invalid
            None      # null
        ]),
        "payment_date": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    }

    data.append(record)

df = pd.DataFrame(data)

output_path = "data/raw/payments/2026/01/13/payments.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("Payments dataset generated successfully")
print(f"Records: {len(df)}")
print(f"Path: {output_path}")
