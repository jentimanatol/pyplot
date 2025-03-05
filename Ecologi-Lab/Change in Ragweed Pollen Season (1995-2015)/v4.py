import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Sample data (replace this with the full dataset)
data = [
    # Add the full dataset here
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert date columns to datetime
df['date_start'] = pd.to_datetime(df['date_start'], format='%m/%d/%Y')
df['date_end'] = pd.to_datetime(df['date_end'], format='%m/%d/%Y')

# Calculate the year for each event
df['year'] = df['date_start'].dt.year

# Plotting
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")

# Create a scatter plot with intensity and duration
scatter = sns.scatterplot(
    x='duration', 
    y='intensity_mean', 
    hue='marine_protected_area', 
    size='severity', 
    sizes=(50, 200), 
    alpha=0.7, 
    data=df, 
    palette='viridis'
)

# Add labels and title
plt.title("Figure 4. Marine Heat Wave Intensity and Duration at Five Marine Protected Areas, 1982-2023", fontsize=16, pad=20)
plt.xlabel("Duration (days)", fontsize=14)
plt.ylabel("Intensity (degrees F)", fontsize=14)

# Add a legend
plt.legend(title='Marine Protected Area', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add source and data information
plt.figtext(0.5, 0.01, "Source: EPA's Climate Change Indicators in the United States: www.epa.gov/climate-indicators", ha="center", fontsize=10)
plt.figtext(0.5, -0.03, "Data source: NOAA, 2024", ha="center", fontsize=10)
plt.figtext(0.5, -0.05, "Web update: June 2024", ha="center", fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()