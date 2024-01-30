
import pandas as pd

# Assuming your DataFrame is named 'df'
# Replace 'df' with your actual DataFrame name

# Get the actual column names from the 0th index
actual_column_names = df.iloc[0].tolist()

# Replace the column names with the actual ones
df.columns = actual_column_names

# Drop the row with the unwanted column names
df = df.drop(0)

# If you want to reset the index after dropping the row
df = df.reset_index(drop=True)

# Save the updated DataFrame to the existing dataset file
df.to_csv(r'D:\IBSS-with-mlflow\artifacts\data_ingestion\default_credit.csv', index=False)
