import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
dates = pd.date_range(start='1/1/2024', periods=365)
temperature = np.random.normal(loc=15, scale=10, size=len(dates))  # Random temperature data
air_quality = np.random.normal(loc=50, scale=10, size=len(dates))  # Random air quality data

# Create a DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Temperature': temperature,
    'Air_Quality_Index': air_quality
})

# Plotting
fig, ax1 = plt.subplots()

# Plot Temperature
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)', color='tab:red')
ax1.plot(data['Date'], data['Temperature'], color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a twin Axes sharing the xaxis
ax2 = ax1.twinx()
ax2.set_ylabel('Air Quality Index', color='tab:blue')
ax2.plot(data['Date'], data['Air_Quality_Index'], color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Title and Show plot
plt.title('Air Quality and Temperature in 2024')
fig.tight_layout()
plt.show()
