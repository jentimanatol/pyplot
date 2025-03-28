import pandas as pd

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Combine Cast Columns
# Combine all cast columns into a single list for analysis
df['All Cast'] = df[['Cast (1)', 'Cast (2)', 'Cast (3)', 'Cast (4)', 'Cast (5)']].apply(lambda x: ', '.join(x.dropna()), axis=1)

# Step 3: Explode the DataFrame to Have One Actor per Row
exploded_df = df[['All Cast', 'Box Office Revenue ($)']].copy()
exploded_df = exploded_df.assign(Cast=exploded_df['All Cast'].str.split(', ')).explode('Cast')

# Step 4: Group by Cast and Calculate Average Revenue
cast_revenue = exploded_df.groupby('Cast')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Step 5: Save the Results to a CSV File
sorted_cast_df = cast_revenue.reset_index()
sorted_cast_df.columns = ['Cast Member', 'Average Box Office Revenue ($)']
sorted_cast_df.to_csv('Sorted_Cast_Revenue.csv', index=False)

# Step 6: Output the Top 50 for Reference (Optional)
print("Top 50 Cast Members by Average Box Office Revenue:")
print(sorted_cast_df.head(50))