import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data_file = 'marine-heat-waves_fig-4.csv'
df = pd.read_csv(data_file, skiprows=7, header=None)  # Skip the first 7 rows of informational data and read without headers

# Manually set the column headers
df.columns = ["event_no", "duration", "date_start", "date_end", "intensity_mean", "severity", "marine_protected_area"]

# Debug: Print the first few rows of the raw DataFrame
print("First few rows of the raw DataFrame:")
print(df.head())

# Convert relevant columns to the appropriate data types
df['duration'] = df['duration'].astype(int)
df['date_start'] = pd.to_datetime(df['date_start'])
df['date_end'] = pd.to_datetime(df['date_end'])
df['intensity_mean'] = df['intensity_mean'].astype(float)

# Debug: Print the DataFrame info
print("\nDataFrame Info:")
print(df.info())

# Debug: Print the first few rows of the DataFrame after type conversion
print("\nFirst few rows of the DataFrame after type conversion:")
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
