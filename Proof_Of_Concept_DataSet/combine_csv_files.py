import pandas as pd
import glob

# Get list of CSV files in a directory
csv_files = glob.glob("*.csv")

print(csv_files)

# Load the first CSV to capture column names
combined_df = pd.read_csv(csv_files[0])

# Loop through the rest, skipping their headers
for file in csv_files[1:]:
    df = pd.read_csv(file)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save to a new CSV
combined_df.to_csv("combined_file.csv", index=False)
