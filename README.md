# 🛒 Azure E-Commerce ETL Pipeline

A scalable, production-grade ETL pipeline that processes over **15GB** of daily e-commerce data using Azure Data Factory, Databricks, and Delta Lake. Built with the **medallion architecture (Bronze → Silver → Gold)** to enable real-time insights, high data quality, and reliable reporting.

---

## 🚀 Objective

Streamline raw transactional data into meaningful business insights using a cloud-native, cost-efficient architecture on Azure.

---

## 🧰 Tech Stack

| Layer         | Tools/Tech                                                                 |
|---------------|----------------------------------------------------------------------------|
| Ingestion     | Azure Data Factory, Azure Storage Explorer                                 |
| Processing    | Azure Databricks (PySpark), Delta Lake                                     |
| Storage       | Azure Data Lake Storage Gen2 (Bronze → Silver → Gold)                     |
| Orchestration | Azure Data Factory                                                         |
| Reporting     | Power BI                                                                   |
| File Format   | CSV, Delta                                                                 |

---

## 🔑 Key Features

- ✅ Ingests raw transactional data from external vendors (CSV/JSON)
- ⚡ Optimized Spark transformations with partitioning and caching
- 🔁 Daily ETL automation using Azure Data Factory pipelines
- 📊 Delta Lake used for upserts, schema enforcement, and ACID compliance
- 📈 Near-real-time reporting via Power BI dashboards
- 🔎 Built-in data validation module for quality checks

---

## 🧱 Architecture

> 📌 Medallion Architecture (Bronze → Silver → Gold)

![Architecture Diagram](https://github.com/venugagula/azure-ecommerce-etl-pipeline/assets/YOUR_ASSET_ID/diagram.png)

---

## 🗂️ Project Structure

```bash
azure-ecommerce-etl-pipeline/
├── scripts/
│   ├── ingestion.py            # Uploads files to ADLS (Bronze)
│   ├── etl_pipeline.py         # Main PySpark transformation logic
│   ├── delta_lake_utils.py     # Upsert helper functions using Delta
│   └── validation.py           # Data quality checks
├── reports/
│   └── power_bi_dashboard.pbix
├── requirements.txt
├── .gitignore
└── README.md
