import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Group by Directors
# Calculate average box office revenue, total box office revenue, and number of movies directed
director_analysis = df.groupby('Director (1)').agg(
    Average_Revenue=('Box Office Revenue ($)', 'mean'),
    Total_Revenue=('Box Office Revenue ($)', 'sum'),
    Movie_Count=('Box Office Revenue ($)', 'count')
).sort_values(by='Total_Revenue', ascending=False)

# Calculate ROI if Budget column is available
if 'Budget ($)' in df.columns:
    df['ROI (%)'] = ((df['Box Office Revenue ($)'] - df['Budget ($)']) / df['Budget ($)']) * 100
    roi_analysis = df.groupby('Director (1)').agg(
        Average_ROI=('ROI (%)', 'mean'),
        Total_ROI=('ROI (%)', 'sum')
    )
    director_analysis = pd.merge(director_analysis, roi_analysis, left_index=True, right_index=True)

# Step 3: Output the Results
print("Detailed Analysis of Directors:")
print(director_analysis.head(10))  # Displaying top 10 directors for analysis

# Step 4: Visualization
# Plot average revenue by directors (Top 10)
plt.figure(figsize=(12, 6))
director_analysis['Average_Revenue'].head(10).plot(kind='bar', color='orange', title='Top 10 Directors by Average Box Office Revenue')
plt.xlabel('Director')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot total revenue by directors (Top 10)
plt.figure(figsize=(12, 6))
director_analysis['Total_Revenue'].head(10).plot(kind='bar', color='blue', title='Top 10 Directors by Total Box Office Revenue')
plt.xlabel('Director')
plt.ylabel('Total Box Office Revenue ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot number of movies directed (Top 10)
plt.figure(figsize=(12, 6))
director_analysis['Movie_Count'].head(10).plot(kind='bar', color='green', title='Top 10 Directors by Number of Movies Directed')
plt.xlabel('Director')
plt.ylabel('Number of Movies Directed')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()