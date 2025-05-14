import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Group by Directors and Calculate Average Box Office Revenue
director_revenue = df.groupby('Director (1)')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Step 3: Output the Results
print("Top Directors by Average Box Office Revenue:")
print(director_revenue.head(10))  # Displaying the top 10 directors

# Step 4: Visualization
# Plot average revenue by directors (Top 10)
plt.figure(figsize=(12, 6))
director_revenue.head(10).plot(kind='bar', color='orange', title='Top 10 Directors by Average Box Office Revenue')
plt.xlabel('Director')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()