# Azure E-Commerce ETL Pipeline

## Overview
A scalable cloud-based ETL pipeline that processes over 15GB of daily e-commerce data using Azure Data Factory and Databricks. Built with medallion architecture (Bronze → Silver → Gold) to streamline data quality, enrichment, and reporting.

## Tech Stack
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks (PySpark)
- Delta Lake
- Power BI

## Key Features
- Ingests raw transactional data from external sources
- Optimized Spark transformations with partitioning and caching
- Automated daily refresh for business reporting

## Architecture

![image](https://github.com/user-attachments/assets/f2f5eed4-2e6d-4c42-8c3d-54db4cc61297)
