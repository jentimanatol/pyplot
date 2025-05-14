import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Combine Genre Columns (If Necessary)
# Handle missing values and combine genres into a single column for simplicity
df['All Genres'] = df[['Genre (1)', 'Genre (2)']].apply(lambda x: ', '.join(x.dropna()), axis=1)

# Step 3: Calculate Average Box Office Revenue by Genre
genre_revenue = df.groupby('All Genres')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Step 4: Filter the Top 50 Genres
top_50_genres = genre_revenue.head(50)

# Step 5: Plot Average Revenue for Top 50 Genres
plt.figure(figsize=(15, 10))
top_50_genres.plot(kind='bar', color='skyblue', title='Top 50 Genres by Average Box Office Revenue')
plt.xlabel('Genre')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=45, fontsize=8, ha='right')
plt.tight_layout()
plt.show()