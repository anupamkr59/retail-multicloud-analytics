# Multi-Cloud Retail Analytics Platform
## 1. Project Overview
This project implements a multi-cloud retail analytics platform where data originates from GCP, is processed and governed in Azure, and is consumed using Power BI.

##2. Architecture Flow
GCP Source Systems
-> Azure Data Factory (Orchestration)
-> Azure Data Lake Gen2 (Raw Layer)
-> Python Data Quality Checks
-> Azure Data Lake Gen2 (Curated Layer)
-> Azure Synapse (Semantic Layer)
-> Power Bi Dashboards

##3. Why This Architecture
- GCP hosts source systems
- Azure Data Factory handles orchestration
- ADLS Gen2 provides scalable storage
- Python ensures data quality
- Synapse provides governed SQL access
- Power BI delivers business insights