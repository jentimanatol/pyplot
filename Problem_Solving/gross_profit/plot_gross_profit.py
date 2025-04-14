import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Select Relevant Columns (Movie Title and Gross Profit)
profit_df = df[['Movie Title', 'Gross Profit ($)']]

# Step 4: Sort by Gross Profit in Descending Order
sorted_profit_df = profit_df.sort_values(by='Gross Profit ($)', ascending=False)

# Step 5: Save the Results to a CSV File
sorted_profit_df.to_csv('Sorted_Movie_Profits.csv', index=False)

# Step 6: Plot Top 50 Movies by Gross Profit
top_50_movies = sorted_profit_df.head(50)
plt.figure(figsize=(15, 10))
plt.barh(top_50_movies['Movie Title'], top_50_movies['Gross Profit ($)'], color='blue')
plt.title('Top 50 Movies by Gross Profit', fontsize=16)
plt.xlabel('Gross Profit ($)', fontsize=14)
plt.ylabel('Movie Title', fontsize=14)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest grossing movie on top
plt.tight_layout()
plt.show()

# Step 7: Output Confirmation
print("The sorted list of movies by gross profit has been saved to 'Sorted_Movie_Profits.csv'.")