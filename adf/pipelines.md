# Azure Data Factory Pipelines

## Pipeline 1: ingest_orders_to_raw

### Objective
Ingest order data from source system into Raw layer of Data Lake.

### Source
- Type: CSV file
- Dataset: Orders
- Columns:
  - order_id
  - order_date
  - customer_id
  - region
  - order_amount
  - order_status

### Sink
- Storage: Azure Data Lake Gen2 (simulated locally)
- Layer: Raw
- Path format:
  /data/raw/orders/yyyy/mm/dd/orders.csv

### Activity
- Copy Activity
- No transformation
- Schema drift allowed

### Trigger
- Scheduled (Daily)
