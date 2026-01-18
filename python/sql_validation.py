
import pandas as pd
df = pd.read_csv("data/curated/orders/curated_orders.csv")

total_orders = len(df)
total_revenue = df["order_amount"].sum()

print(total_orders, total_revenue)

df = pd.read_csv("data/curated/payments/curated_payments.csv")
result = df.groupby("payment_status").size()
print(result)

orders = pd.read_csv("data/curated/orders/curated_orders.csv")
payments = pd.read_csv("data/curated/payments/curated_payments.csv")
successful = payments[payments["payment_status"]=="SUCCESSS"]

merged = orders.merge(successful[["order_id"]], on="order_id", how="left", indicator= True)

no_payment_orders = merged[merged["_merge"]== "left_only"]

print(no_payment_orders[["order_id", "order_amount"]])







