import pandas as pd
import numpy as np

# 1. LOAD THE DATA
# Replace with your local CSV path or API pulling function
df = pd.read_csv("data/raw_data.csv")

# 2. INSPECT THE DAMAGE
print("--- DATA SUMMARY ---")
print(df.info())
print("\n--- MISSING VALUES PER COLUMN ---")
print(df.isnull().sum())

# 3. CLEANING OPERATIONS (Uncomment and modify what you need)
df_clean = df.copy()

# A. Drop rows where critical target columns are missing
# df_clean = df_clean.dropna(subset=["YOUR_TARGET_COLUMN"])

# B. Handle missing values in predictor columns (Imputation)
# df_clean["PREDICTOR_COLUMN"] = df_clean["PREDICTOR_COLUMN"].fillna(value=0)

# C. Convert columns to correct data types (e.g., text to numeric or date)
# df_clean["NUMERIC_COLUMN"] = pd.to_numeric(df_clean["NUMERIC_COLUMN"])

# 4. EXPORT FOR THURSDAY EDA
df_clean.to_csv("data/cleaned_data.csv", index=False)
print("\n Success! Cleaned dataset saved to data/cleaned_data.csv")
