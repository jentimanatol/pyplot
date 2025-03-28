import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Extract Words from Movie Titles
# Split movie titles into individual words
df['Movie Title Words'] = df['Movie Title'].str.split()

# Create a list of all words across movie titles
all_words = [word.lower() for title in df['Movie Title Words'] for word in title]

# Count the frequency of each word
word_counts = Counter(all_words)

# Step 3: Map Each Movie Title to Its Words
# Create a DataFrame associating words with box office revenue
word_revenue = []
for index, row in df.iterrows():
    for word in row['Movie Title Words']:
        word_revenue.append({'Word': word.lower(), 'Revenue': row['Box Office Revenue ($)']})

word_revenue_df = pd.DataFrame(word_revenue)

# Step 4: Calculate Average Revenue for Each Word
avg_word_revenue = word_revenue_df.groupby('Word')['Revenue'].mean().sort_values(ascending=False)

# Step 5: Save Results to a CSV File
avg_word_revenue_df = avg_word_revenue.reset_index()
avg_word_revenue_df.columns = ['Word', 'Average Box Office Revenue ($)']
avg_word_revenue_df.to_csv('Word_Revenue_Analysis.csv', index=False)

# Step 6: Plot Top 50 Words by Average Revenue
top_50_words = avg_word_revenue.head(50)

plt.figure(figsize=(15, 10))
top_50_words.plot(kind='bar', color='green', title='Top 50 Words by Average Box Office Revenue')
plt.xlabel('Word')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=45, fontsize=8, ha='right')
plt.tight_layout()
plt.show()

# Step 7: Output Confirmation
print("Analysis complete! Results saved in 'Word_Revenue_Analysis.csv'.")