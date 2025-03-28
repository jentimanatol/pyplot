import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Aggregate Contributions
# Calculate average contributions to gross profit by each element
genre_profit = df.groupby('Genre (1)')['Gross Profit ($)'].mean()
secondary_genre_profit = df.groupby('Genre (2)')['Gross Profit ($)'].mean()
director_profit = df.groupby('Director (1)')['Gross Profit ($)'].mean()
cast_profit = df[['Cast (1)', 'Gross Profit ($)']].groupby('Cast (1)').mean()

# Step 4: Merge Contributions into a Single Table
# Convert each into a DataFrame and rename columns for clarity
genre_profit_df = genre_profit.reset_index()
genre_profit_df.columns = ['Element', 'Contribution ($)']
genre_profit_df['Type'] = 'Genre'

secondary_genre_profit_df = secondary_genre_profit.reset_index()
secondary_genre_profit_df.columns = ['Element', 'Contribution ($)']
secondary_genre_profit_df['Type'] = 'Secondary Genre'

director_profit_df = director_profit.reset_index()
director_profit_df.columns = ['Element', 'Contribution ($)']
director_profit_df['Type'] = 'Director'

cast_profit_df = cast_profit.reset_index()
cast_profit_df.columns = ['Element', 'Contribution ($)']
cast_profit_df['Type'] = 'Cast'

# Combine all contributions into one DataFrame
all_contributions = pd.concat([genre_profit_df, secondary_genre_profit_df, director_profit_df, cast_profit_df])

# Step 5: Save All Contributions to CSV
all_contributions.to_csv('All_Contributions_to_Gross_Profit.csv', index=False)

# Step 6: Plot Top 10 Contributors for Each Element
top_10_genres = genre_profit.sort_values(ascending=False).head(10)
top_10_directors = director_profit.sort_values(ascending=False).head(10)
top_10_cast = cast_profit['Gross Profit ($)'].sort_values(ascending=False).head(10)

# Plot Genres
plt.figure(figsize=(15, 10))
plt.barh(top_10_genres.index, top_10_genres.values, color='purple')
plt.title('Top 10 Genres by Average Contribution to Gross Profit', fontsize=16)
plt.xlabel('Average Contribution ($)', fontsize=14)
plt.ylabel('Genres', fontsize=14)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('Top_10_Genres_Contributions.png')
plt.show()

# Plot Directors
plt.figure(figsize=(15, 10))
plt.barh(top_10_directors.index, top_10_directors.values, color='blue')
plt.title('Top 10 Directors by Average Contribution to Gross Profit', fontsize=16)
plt.xlabel('Average Contribution ($)', fontsize=14)
plt.ylabel('Directors', fontsize=14)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('Top_10_Directors_Contributions.png')
plt.show()

# Plot Cast Members
plt.figure(figsize=(15, 10))
plt.barh(top_10_cast.index, top_10_cast.values, color='green')
plt.title('Top 10 Cast Members by Average Contribution to Gross Profit', fontsize=16)
plt.xlabel('Average Contribution ($)', fontsize=14)
plt.ylabel('Cast Members', fontsize=14)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('Top_10_Cast_Contributions.png')
plt.show()

# Step 7: Output Confirmation
print("All contributions have been saved to 'All_Contributions_to_Gross_Profit.csv'.")
print("Plots for genres, directors, and cast contributions have been saved as PNG files.")