import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file, skipping the first 6 rows and using row 7 as the header
data_file = 'marine-heat-waves_fig-3.csv'
df = pd.read_csv(data_file, skiprows=6, header=0)

# Print the column names to verify
print("Column Names:")
print(df.columns)

# Clean column names (remove leading/trailing spaces and replace spaces with underscores)
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
df.columns = df.columns.str.replace(' ', '_')  # Replace spaces with underscores

# Print the cleaned column names
print("\nCleaned Column Names:")
print(df.columns)

# Verify the 'Year' column exists
if 'Year' not in df.columns:
    print("\nError: 'Year' column not found. Actual columns are:")
    print(df.columns)
else:
    # Convert the data to long format
    df_long = pd.melt(df, id_vars=['Year'], var_name='Region_Intensity', value_name='Percent_Area')

    # Split the 'Region_Intensity' column into 'Region' and 'Intensity'
    df_long[['Region', 'Intensity']] = df_long['Region_Intensity'].str.split('_', 1, expand=True)

    # Drop the original 'Region_Intensity' column
    df_long.drop(columns=['Region_Intensity'], inplace=True)

    # Display the reshaped data
    print("\nReshaped Data:")
    print(df_long.head())

    # Plot the data
    plt.figure(figsize=(18, 12))
    sns.set(style="whitegrid")

    # Create a plot for each region
    regions = df_long['Region'].unique()
    intensities = df_long['Intensity'].unique()

    for i, region in enumerate(regions, 1):
        plt.subplot(3, 2, i)  # 3 rows, 2 columns of subplots
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