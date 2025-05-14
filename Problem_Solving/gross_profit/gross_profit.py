import pandas as pd

# Step 1: Load the Updated Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Select Relevant Columns (Movie Title and Gross Profit)
profit_df = df[['Movie Title', 'Gross Profit ($)']]

# Step 4: Sort by Gross Profit in Descending Order
sorted_profit_df = profit_df.sort_values(by='Gross Profit ($)', ascending=False)

# Step 5: Save the Results to a New CSV File
sorted_profit_df.to_csv('Sorted_Movie_Profits.csv', index=False)

# Step 6: Output Confirmation
print("The updated list of movies by gross profit has been saved to 'Sorted_Movie_Profits.csv'.")