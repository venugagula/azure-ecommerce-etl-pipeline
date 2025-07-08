# etl_pipeline.py
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable
from scripts.delta_lake_utils import merge_delta
import pyspark.sql.functions as F

builder = SparkSession.builder.appName("EcommerceETL") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

def run_etl():
    bronze_path = "abfss://bronze@yourstorageaccount.dfs.core.windows.net/sales/"
    silver_path = "abfss://silver@yourstorageaccount.dfs.core.windows.net/sales/"
    gold_path = "abfss://gold@yourstorageaccount.dfs.core.windows.net/sales_agg/"

    df = spark.read.format("csv").option("header", "true").load(bronze_path)

    # Clean & transform
    df_cleaned = df.dropna(subset=["order_id", "amount"]) \
                   .withColumn("amount", F.col("amount").cast("double"))

    # Write to silver
    df_cleaned.write.format("delta").mode("overwrite").save(silver_path)

    # Aggregate & write to gold
    df_agg = df_cleaned.groupBy("product_id").agg(F.sum("amount").alias("total_sales"))
    df_agg.write.format("delta").mode("overwrite").save(gold_path)

    print("ETL pipeline completed.")

if __name__ == "__main__":
    run_etl()

