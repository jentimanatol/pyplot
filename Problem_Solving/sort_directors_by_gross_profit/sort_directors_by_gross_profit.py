import pandas as pd

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Group by Directors and Calculate Total Gross Profit
# Only considering 'Director (1)' for now
director_gross_profit = df.groupby('Director (1)')['Gross Profit ($)'].sum().sort_values(ascending=False)

# Step 4: Save the Results to a CSV File
sorted_director_profit_df = director_gross_profit.reset_index()
sorted_director_profit_df.columns = ['Director', 'Total Gross Profit ($)']
sorted_director_profit_df.to_csv('Directors_by_Gross_Profit.csv', index=False)

# Step 5: Output Confirmation
print("The sorted list of directors by total gross profit has been saved to 'Directors_by_Gross_Profit.csv'.")