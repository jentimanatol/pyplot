import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Debug flag: Set to True to enable debug prints
DEBUG = True

# Read the CSV file, skipping the first 6 rows and using row 7 as the header
data_file = 'marine-heat-waves_fig-3.csv'
df = pd.read_csv(data_file, skiprows=6, header=0)

# Debug: Print the raw data after reading
if DEBUG:
    print("\nRaw Data (First 5 Rows):")
    print(df.head())

# Clean column names (remove leading/trailing spaces and replace spaces with underscores)
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
df.columns = df.columns.str.replace(' ', '_')  # Replace spaces with underscores

# Debug: Print the cleaned column names
if DEBUG:
    print("\nCleaned Column Names:")
    print(df.columns)

# Verify the 'Year' column exists
if 'Year' not in df.columns:
    print("\nError: 'Year' column not found. Actual columns are:")
    print(df.columns)
else:
    # Convert the data to long format
    df_long = pd.melt(df, id_vars=['Year'], var_name='Region_Intensity', value_name='Percent_Area')

    # Debug: Print the reshaped data before splitting
    if DEBUG:
        print("\nReshaped Data (Before Splitting):")
        print(df_long.head())

    # Split the 'Region_Intensity' column into 'Region' and 'Intensity'
    try:
        # Correct usage of str.split()
        df_long[['Region', 'Intensity']] = df_long['Region_Intensity'].str.split('_', n=1, expand=True)
    except Exception as e:
        print("\nError Splitting 'Region_Intensity' Column:")
        print(e)
        print("\nSample of 'Region_Intensity' Column:")
        print(df_long['Region_Intensity'].head())

    # Debug: Print the reshaped data after splitting
    if DEBUG:
        print("\nReshaped Data (After Splitting):")
        print(df_long.head())

    # Drop the original 'Region_Intensity' column
    df_long.drop(columns=['Region_Intensity'], inplace=True)

    # Debug: Print the final reshaped data
    if DEBUG:
        print("\nFinal Reshaped Data:")
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