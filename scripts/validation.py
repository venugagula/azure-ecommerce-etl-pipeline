# validation.py
def validate_data(df):
    null_counts = {col: df.filter(df[col].isNull()).count() for col in df.columns}
    for col, count in null_counts.items():
        print(f"Column '{col}' has {count} null values")

    if df.count() == 0:
        raise ValueError("DataFrame is empty!")

    print("Basic validation passed.")

