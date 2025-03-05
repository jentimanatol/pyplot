import pandas as pd

# Read the CSV file, skipping the first 6 rows
data_file = 'marine-heat-waves_fig-3.csv'
df = pd.read_csv(data_file, skiprows=6)

# Print the column names to verify
print("Original Column Names:")
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