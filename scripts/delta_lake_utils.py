# delta_lake_utils.py
from delta.tables import DeltaTable

def merge_delta(spark, new_df, delta_path, key_column):
    delta_table = DeltaTable.forPath(spark, delta_path)
    (
        delta_table.alias("old")
        .merge(
            new_df.alias("new"),
            f"old.{key_column} = new.{key_column}"
        )
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )

