import pandas as pd
import matplotlib.pyplot as plt

# Read the data
data = []
headers = ["event_no", "duration", "date_start", "date_end", "intensity_mean", "severity", "marine_protected_area"]
data_start_line = 8  # Starting from line 8

with open('data.txt', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if i >= data_start_line:
            # Check if the line contains valid data
            values = line.strip().split(',')
            if len(values) == len(headers):
                data.append(values)

# Create a DataFrame
df = pd.DataFrame(data, columns=headers)

# Convert relevant columns to the appropriate data types
df['duration'] = df['duration'].astype(int)
df['date_start'] = pd.to_datetime(df['date_start'])
df['date_end'] = pd.to_datetime(df['date_end'])
df['intensity_mean'] = df['intensity_mean'].astype(float)

# Debug: Print the first few rows of the DataFrame after type conversion
print("\nFirst few rows of DataFrame after type conversion:")
print(df.head())

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(df['date_start'], df['duration'], label='Duration (days)')
plt.plot(df['date_start'], df['intensity_mean'], label='Intensity (degrees F)', linestyle='--')

# Customize the plot
plt.title('Marine Heat Wave Intensity and Duration (1982-2023)')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
