import matplotlib.pyplot as plt
import pandas as pd

# List of weights
weights = [144, 152, 142, 151, 160, 152, 131, 164, 141, 153, 140, 144, 175, 156, 147, 133, 172, 159, 135, 159, 148, 171]

# Create a pandas DataFrame
df = pd.DataFrame(weights, columns=["Weight"])

# Extract stems and leaves
df["Stem"] = df["Weight"] // 10
df["Leaf"] = df["Weight"] % 10

# Group by Stem and collect leaves
stemplot_data = df.groupby("Stem")["Leaf"].apply(lambda x: sorted(x)).reset_index()

# Function to plot stemplot
def plot_stemplot(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Stemplot of Varsity Football Team Weights", fontsize=16)
    
    # Hide axes
    ax.axis("off")
    
    # Plot stems and leaves
    for i, row in data.iterrows():
        stem = row["Stem"]
        leaves = " ".join(map(str, row["Leaf"]))  # Convert leaves to a space-separated string
        ax.text(0.1, i, f"{stem} | {leaves}", fontsize=12, fontfamily='monospace', verticalalignment='center')
    
    # Adjust y-axis limits to ensure all rows are visible
    ax.set_ylim(len(data), -1)
    
    # Add original data as a label
    original_data = "Original Data: " + ", ".join(map(str, weights))
    ax.text(0.5, -1.5, original_data, fontsize=12, fontfamily='monospace', ha='center')
    
    plt.show()

# Plot the stemplot
plot_stemplot(stemplot_data)