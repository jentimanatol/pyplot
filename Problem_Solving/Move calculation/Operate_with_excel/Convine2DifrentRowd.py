
import pandas as pd

# Load the dataset (replace 'Movie Data Starter Project.xlsx' with your actual file path)
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Preview the first few rows
#print(df.head())
# Grouping by Director
director_revenue = df.groupby('Director (1)')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Displaying the top 10 directors
print("Top 10 Directors by Average Box Office Revenue:")
print(director_revenue.head(10))


# Grouping by Genre
#genre_revenue = df.groupby('Genre')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Displaying the top 10 genres


# Combine genres into a single column
df['All Genres'] = df[['Genre (1)', 'Genre (2)']].apply(lambda x: ', '.join(x.dropna()), axis=1)