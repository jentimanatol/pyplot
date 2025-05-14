import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Combine Genre Columns
# Handle missing values and combine genres into a single column
df['Combined Genres'] = df[['Genre (1)', 'Genre (2)']].apply(lambda x: ', '.join(x.dropna()), axis=1)

# Step 3: Group by Combined Genres and Calculate Average Box Office Revenue
genre_revenue = df.groupby('Combined Genres')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Step 4: Output the Results
print("Average Box Office Revenue by Genre:")
print(genre_revenue)

# Step 5: Visualization
# Plot average box office revenue by genre
plt.figure(figsize=(12, 6))
genre_revenue.plot(kind='bar', color='skyblue', title='Average Box Office Revenue by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()