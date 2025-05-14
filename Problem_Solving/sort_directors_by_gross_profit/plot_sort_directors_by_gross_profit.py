import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Group by Directors and Calculate Total Gross Profit
# Using 'Director (1)' column for this analysis
director_gross_profit = df.groupby('Director (1)')['Gross Profit ($)'].sum().sort_values(ascending=False)

# Step 4: Filter Top 50 Directors
top_50_directors = director_gross_profit.head(50)

# Step 5: Plot Total Gross Profit for Top 50 Directors
plt.figure(figsize=(15, 10))
plt.barh(top_50_directors.index, top_50_directors.values, color='green')
plt.title('Top 50 Directors by Total Gross Profit', fontsize=16)
plt.xlabel('Total Gross Profit ($)', fontsize=14)
plt.ylabel('Director', fontsize=14)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest profit at the top
plt.tight_layout()
plt.show()

# Step 6: Save Results to a CSV File
top_50_directors_df = top_50_directors.reset_index()
top_50_directors_df.columns = ['Director', 'Total Gross Profit ($)']
top_50_directors_df.to_csv('Top_50_Directors_Gross_Profit.csv', index=False)

# Step 7: Output Confirmation
print("The plot has been generated, and the sorted list of directors by gross profit has been saved to 'Top_50_Directors_Gross_Profit.csv'.")