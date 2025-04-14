import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Extract Words from Movie Titles
df['Title Words'] = df['Movie Title'].str.split()  # Split titles into individual words

# Step 4: Create Word-Level DataFrame
word_revenue = []
for index, row in df.iterrows():
    for word in row['Title Words']:
        word_revenue.append({'Word': word.lower(), 'Revenue': row['Gross Profit ($)']})

word_revenue_df = pd.DataFrame(word_revenue)

# Step 5: Calculate Total Gross Profit for Each Word
word_gross_profit = word_revenue_df.groupby('Word')['Revenue'].sum().sort_values(ascending=False)

# Step 6: Filter Top 50 Words
top_50_words = word_gross_profit.head(50)

# Step 7: Save the Results to a CSV File
sorted_word_profit_df = word_gross_profit.reset_index()
sorted_word_profit_df.columns = ['Word', 'Total Gross Profit ($)']
sorted_word_profit_df.to_csv('Words_by_Gross_Profit.csv', index=False)

# Step 8: Plot Top 50 Words by Gross Profit
plt.figure(figsize=(15, 10))
plt.barh(top_50_words.index, top_50_words.values, color='orange')
plt.title('Top 50 Words in Movie Titles by Total Gross Profit', fontsize=16)
plt.xlabel('Total Gross Profit ($)', fontsize=14)
plt.ylabel('Words', fontsize=14)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest grossing word at the top
plt.tight_layout()
plt.show()

# Step 9: Output Confirmation
print("The plot has been generated, and the sorted list of words by gross profit has been saved to 'Words_by_Gross_Profit.csv'.")