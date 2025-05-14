import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Group by Genre and Calculate Total Gross Profit
# Combining Genre (1) and Genre (2) into a single column for analysis
df['All Genres'] = df[['Genre (1)', 'Genre (2)']].apply(lambda x: ', '.join(x.dropna()), axis=1)
genre_gross_profit = df.groupby('All Genres')['Gross Profit ($)'].sum().sort_values(ascending=False)

# Step 4: Save the Results to a CSV File
sorted_genre_profit_df = genre_gross_profit.reset_index()
sorted_genre_profit_df.columns = ['Genre', 'Total Gross Profit ($)']
sorted_genre_profit_df.to_csv('Genres_by_Gross_Profit.csv', index=False)


print("The sorted list of genres by total gross profit has been saved to 'Genres_by_Gross_Profit.csv'.")