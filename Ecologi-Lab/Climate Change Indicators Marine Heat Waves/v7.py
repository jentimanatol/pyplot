import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data_file = 'marine-heat-waves_fig-4.csv'
df = pd.read_csv(data_file, skiprows=7, header=None)

# Manually set the column headers
df.columns = ["event_no", "duration", "date_start", "date_end", "intensity_mean", "severity", "marine_protected_area"]

# Convert relevant columns to the appropriate data types
df['duration'] = df['duration'].astype(int)
df['date_start'] = pd.to_datetime(df['date_start'])
df['date_end'] = pd.to_datetime(df['date_end'])
df['intensity_mean'] = df['intensity_mean'].astype(float)

# Verify data loading
print(f"Total rows in the DataFrame: {len(df)}")

# Check for missing values
print("\nMissing values:")
print(df[['date_start', 'duration', 'intensity_mean']].isnull().sum())

# Check data ranges
print("\nData ranges:")
print(f"Date range: {df['date_start'].min()} to {df['date_start'].max()}")
print(f"Duration range: {df['duration'].min()} to {df['duration'].max()}")
print(f"Intensity range: {df['intensity_mean'].min()} to {df['intensity_mean'].max()}")

# Compare plot data with DataFrame
duration_points = len(df['date_start'].unique())
intensity_points = len(df['date_start'].unique())
print(f"\nNumber of duration data points in the plot: {duration_points}")
print(f"Number of intensity data points in the plot: {intensity_points}")

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