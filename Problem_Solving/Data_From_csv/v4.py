from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def optimal_budget_clusters(self):
    """Clusters movies based on Budget and Profit to identify optimal budget ranges."""
    self.df["Profit"] = self.df["BoxOfficeRevenue"] - self.df["Budget"]
    data = self.df[["Budget", "Profit"]].dropna()
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    data["Cluster"] = kmeans.fit_predict(data[["Budget", "Profit"]])
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Budget"], data["Profit"], c=data["Cluster"], cmap="viridis", alpha=0.6)
    plt.xlabel("Budget (in USD)")
    plt.ylabel("Profit (in USD)")
    plt.title("Optimal Budget Clusters")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()