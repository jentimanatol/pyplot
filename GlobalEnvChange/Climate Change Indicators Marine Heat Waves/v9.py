import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Debug: Print the DataFrame info
print("\nDataFrame Info:")
print(df.info())

# Debug: Print the first few rows of the DataFrame after type conversion
print("\nFirst few rows of the DataFrame after type conversion:")
print(df.head())

# Get unique locations
unique_locations = df['marine_protected_area'].unique()
print("\nUnique Locations:")
print(unique_locations)

# Generate a color map for each location
num_locations = len(unique_locations)
color_map = plt.cm.get_cmap('tab20', num_locations)  # Use a colormap with enough distinct colors

# Plot the data
plt.figure(figsize=(14, 7))

# Plot each location separately with a unique color
for i, location in enumerate(unique_locations):
    location_data = df[df['marine_protected_area'] == location]
    color = color_map(i)  # Assign a unique color from the colormap
    plt.plot(location_data['date_start'], location_data['duration'], 'o', color=color, label=f'{location} - Duration')
    plt.plot(location_data['date_start'], location_data['intensity_mean'], '--', color=color, label=f'{location} - Intensity')

# Customize the plot
plt.title('Marine Heat Wave Intensity and Duration (1982-2023) by Location')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside the plot
plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()