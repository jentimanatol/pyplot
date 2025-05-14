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

# Debug: Print the DataFrame info
print("\nDataFrame Info:")
print(df.info())

# Debug: Print the first few rows of the DataFrame after type conversion
print("\nFirst few rows of the DataFrame after type conversion:")
print(df.head())

# Define a color map for each location
location_colors = {
    "Olympic Coast National Marine Sanctuary": "blue",
    "Gerry E. Studds/Stellwagen Bank National Marine Sanctuary": "red",
    # Add more locations and colors as needed
}

# Plot the data
plt.figure(figsize=(14, 7))

# Plot each location separately with a unique color
for location, color in location_colors.items():
    location_data = df[df['marine_protected_area'] == location]
    plt.plot(location_data['date_start'], location_data['duration'], 'o', color=color, label=f'{location} - Duration')
    plt.plot(location_data['date_start'], location_data['intensity_mean'], '--', color=color, label=f'{location} - Intensity')

# Customize the plot
plt.title('Marine Heat Wave Intensity and Duration (1982-2023) by Location')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()