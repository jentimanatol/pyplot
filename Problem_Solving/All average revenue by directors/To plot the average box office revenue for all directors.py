import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Average Box Office Revenue by Director
director_revenue = df.groupby('Director (1)')['Box Office Revenue ($)'].mean().sort_values(ascending=False)

# Step 3: Plot Average Revenue for All Directors
plt.figure(figsize=(15, 10))
director_revenue.plot(kind='bar', color='skyblue', title='Average Box Office Revenue by Director')
plt.xlabel('Director')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.show()