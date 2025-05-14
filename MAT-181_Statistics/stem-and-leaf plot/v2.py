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
stemplot_data = df.groupby("Stem")["Leaf"].apply(list).reset_index()

# Function to plot stemplot
def plot_stemplot(data):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")
    max_stem = data["Stem"].max()
    for i, row in data.iterrows():
        stem = row["Stem"]
        leaves = sorted(row["Leaf"])
        leaves_str = " ".join(map(str, leaves))
        ax.text(0.1, max_stem - stem, f"{stem} | {leaves_str}", fontsize=12, fontfamily='monospace')
    plt.title("Stemplot of Varsity Football Team Weights")
    plt.xlabel("Stem  |  Leaf")
    plt.legend(["Stem  |  Leaf"], loc="upper right")
    plt.show()

# Plot the stemplot
plot_stemplot(stemplot_data)
