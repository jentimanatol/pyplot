import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the data
data_file = 'marine-heat-waves_fig-3.csv'
df = pd.read_csv(data_file, skiprows=5)

# Step 2: Reshape the data
df_long = pd.melt(df, id_vars=['Year'], var_name='Region_Intensity', value_name='Percent_Area')
df_long[['Region', 'Intensity']] = df_long['Region_Intensity'].str.split(' ', 1, expand=True)
df_long.drop(columns=['Region_Intensity'], inplace=True)

# Step 3: Visualize the data
sns.set(style="whitegrid")
regions = df_long['Region'].unique()
intensities = df_long['Intensity'].unique()

plt.figure(figsize=(18, 12))
for i, region in enumerate(regions, 1):
    plt.subplot(3, 2, i)
    for intensity in intensities:
        data = df_long[(df_long['Region'] == region) & (df_long['Intensity'] == intensity)]
        plt.plot(data['Year'], data['Percent_Area'], label=intensity)
    plt.title(region)
    plt.xlabel('Year')
    plt.ylabel('Percent Area Affected (%)')
    plt.legend(title='Intensity')
    plt.grid(True)

plt.tight_layout()
plt.show()

# Step 4: Analyze the data
region_impact = df_long.groupby('Region')['Percent_Area'].mean().idxmax()
print(f"Region with the highest average impact: {region_impact}")

west_coast_data = df_long[df_long['Region'] == 'West Coast']
print(west_coast_data.groupby(['Year', 'Intensity'])['Percent_Area'].mean().unstack())