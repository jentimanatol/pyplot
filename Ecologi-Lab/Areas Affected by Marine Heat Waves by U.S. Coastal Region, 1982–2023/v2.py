import pandas as pd

# Read the CSV file
data_file = 'marine-heat-waves_fig-3.csv'
df = pd.read_csv(data_file, skiprows=5)

# Print the column names
print("Original Column Names:")
print(df.columns)

# Clean column names
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
df.columns = df.columns.str.replace(' ', '_')  # Replace spaces with underscores

# Print the cleaned column names
print("\nCleaned Column Names:")
print(df.columns)

# Rename the year column if necessary
df.rename(columns={'year': 'Year'}, inplace=True)  # Replace 'year' with the actual column name

# Convert the data to long format
df_long = pd.melt(df, id_vars=['Year'], var_name='Region_Intensity', value_name='Percent_Area')

# Split the 'Region_Intensity' column into 'Region' and 'Intensity'
df_long[['Region', 'Intensity']] = df_long['Region_Intensity'].str.split('_', 1, expand=True)

# Drop the original 'Region_Intensity' column
df_long.drop(columns=['Region_Intensity'], inplace=True)

# Display the reshaped data
print("\nReshaped Data:")
print(df_long.head())