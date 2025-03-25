
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Average Box Office Revenue by Director
director_revenue = df.groupby('Director (1)')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Step 3: Filter Top 50 Directors
top_50_directors = director_revenue.head(50)

# Step 4: Plot Average Revenue for Top 50 Directors
plt.figure(figsize=(15, 10))
top_50_directors.plot(kind='bar', color='skyblue', title='Top 50 Directors by Average Box Office Revenue')
plt.xlabel('Director')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.show()