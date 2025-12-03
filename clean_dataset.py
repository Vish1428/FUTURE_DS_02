import pandas as pd

df = pd.read_csv('dataset.csv')

# Drop Null Values
df_clean = df.dropna().copy()

# Calucated Columns
df_clean['CTR'] = df_clean['clicks'] / df_clean['impressions']
df_clean['CPC'] = df_clean.apply(lambda row : row['spent'] / row['clicks'] if row['clicks'] > 0 else 0, axis=1)
df_clean['CPM'] = (df_clean['spent'] / df_clean['impressions']) * 1000
df_clean['conversion_rate'] = df_clean.apply(lambda row: row['total_conversion']/ row['clicks'] if row['clicks'] > 0 else 0, axis=1)

df_clean.to_csv('cleaned_dataset.csv', index=False)

# Create Summary file
summary = "TASK 2 CLEANED DATA SUMMARY"
summary += f"Total Rows: {len(df_clean)}\n\n"
summary += f"Columns:\n {list(df_clean.columns)}\n\n"
summary += 'Sample Rows: \n'
summary += df_clean.head(15).to_string()

with open ('task2_summary.txt', 'w') as f:
    f.write(summary)

print("Data cleaning complete. Cleaned data saved to 'cleaned dataset.csv' and summary to 'task2_summary.txt'.")