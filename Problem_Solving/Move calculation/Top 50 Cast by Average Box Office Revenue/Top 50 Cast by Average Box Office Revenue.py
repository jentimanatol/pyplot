import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Combine Cast Columns
# Combine all cast columns into a single list for analysis
df['All Cast'] = df[['Cast (1)', 'Cast (2)', 'Cast (3)', 'Cast (4)', 'Cast (5)']].apply(lambda x: ', '.join(x.dropna()), axis=1)

# Step 3: Explode the DataFrame to Have One Actor per Row
exploded_df = df[['All Cast', 'Box Office Revenue ($)']].copy()
exploded_df = exploded_df.assign(Cast=exploded_df['All Cast'].str.split(', ')).explode('Cast')

# Step 4: Group by Cast and Calculate Average Revenue
cast_revenue = exploded_df.groupby('Cast')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Step 5: Filter Top 50 Cast Members
top_50_cast = cast_revenue.head(50)

# Step 6: Plot Average Revenue for Top 50 Cast Members
plt.figure(figsize=(15, 10))
top_50_cast.plot(kind='bar', color='purple', title='Top 50 Cast Members by Average Box Office Revenue')
plt.xlabel('Cast Member')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=45, fontsize=8, ha='right')
plt.tight_layout()
plt.show()

# Step 7: Display Top 50 Cast Members
print("Top 50 Cast Members by Average Box Office Revenue:")
print(top_50_cast)