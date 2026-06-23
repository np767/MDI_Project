library(tidyverse)

# 1. LOAD THE DATA
# Replace with your local CSV path
df <- read_csv("data/raw_data.csv")

# 2. INSPECT THE DAMAGE
print("--- DATA SUMMARY ---")
glimpse(df)
print("\n--- MISSING VALUES PER COLUMN ---")
colSums(is.na(df))

# 3. CLEANING OPERATIONS (Uncomment and modify what you need)
df_clean <- df %>%
  # A. Drop rows where critical target columns are missing (na.rm alternative)
  # filter(!is.na(YOUR_TARGET_COLUMN)) %>%
  
  # B. Handle missing values in predictor columns (Imputation)
  # mutate(PREDICTOR_COLUMN = replace_na(PREDICTOR_COLUMN, 0)) %>%
  
  # C. Convert columns to correct data types
  # mutate(NUMERIC_COLUMN = as.numeric(NUMERIC_COLUMN))
  identity() # Keeps the pipe from breaking if everything else is commented out

# 4. EXPORT FOR THURSDAY EDA
write_csv(df_clean, "data/cleaned_data.csv")
print("\n Success! Cleaned dataset saved to data/cleaned_data.csv")
