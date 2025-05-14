import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit for Each Movie
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Combine All Cast Columns
# Combine all cast columns into a single column for easier grouping
df['All Cast'] = df[['Cast (1)', 'Cast (2)', 'Cast (3)', 'Cast (4)', 'Cast (5)']].apply(lambda x: ', '.join(x.dropna()), axis=1)

# Step 4: Explode the Cast Data
# Create a DataFrame where each cast member has their own row
exploded_df = df[['All Cast', 'Gross Profit ($)']].copy()
exploded_df = exploded_df.assign(Cast=exploded_df['All Cast'].str.split(', ')).explode('Cast')

# Step 5: Group by Cast and Calculate Total Gross Profit
cast_gross_profit = exploded_df.groupby('Cast')['Gross Profit ($)'].sum().sort_values(ascending=False)

# Step 6: Save the Results to a CSV File
sorted_cast_profit_df = cast_gross_profit.reset_index()
sorted_cast_profit_df.columns = ['Cast Member', 'Total Gross Profit ($)']
sorted_cast_profit_df.to_csv('Casts_by_Gross_Profit.csv', index=False)

# Step 7: Plot the Top 50 Cast Members by Total Gross Profit
top_50_cast = cast_gross_profit.head(50)
plt.figure(figsize=(15, 10))
plt.barh(top_50_cast.index, top_50_cast.values, color='teal')
plt.title('Top 50 Cast Members by Total Gross Profit', fontsize=16)
plt.xlabel('Total Gross Profit ($)', fontsize=14)
plt.ylabel('Cast Member', fontsize=14)
plt.gca().invert_yaxis()  # Invert y-axis to display the highest earners at the top
plt.tight_layout()
plt.show()

# Step 8: Output Confirmation
print("The plot has been generated, and the sorted list of cast members by gross profit has been saved to 'Casts_by_Gross_Profit.csv'.")