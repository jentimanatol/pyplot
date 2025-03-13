import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file (assuming it's in the same directory as the script)
file_path = "sorted_expenses_with_totals.csv"  # Just the file name
df = pd.read_csv(file_path)

# Group by category and calculate the total amount for each category
category_totals = df.groupby('category')['amount'].sum().reset_index()

# Sort the categories by total amount (descending)
category_totals = category_totals.sort_values(by='amount', ascending=False)

# Set up the visualization
plt.figure(figsize=(12, 8))
sns.barplot(x='amount', y='category', data=category_totals, palette='viridis')

# Add labels and title
plt.xlabel('Total Amount ($)', fontsize=14)
plt.ylabel('Category', fontsize=14)
plt.title('Total Expenses by Category', fontsize=16)

# Add value labels on the bars
for index, value in enumerate(category_totals['amount']):
    plt.text(value, index, f'${value:,.2f}', va='center', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()