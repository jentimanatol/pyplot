import pandas as pd

# Read the first few lines of the CSV file to analyze its structure
file_path = 'data-3_6_2025-5_14 PM.csv'
with open(file_path, 'r') as file:
    for _ in range(5):
        line = file.readline()
        print(line.strip())

# Read the CSV file starting from the 6th line (actual data)
data = pd.read_csv(file_path, skiprows=5)

# Display the first few rows of the dataframe to verify column names and data
print(data.head())
