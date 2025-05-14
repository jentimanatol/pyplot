import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit for Movies in the Dataset
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Aggregate Historical Averages for Genres, Directors, and Cast Contributions
genre_profit = df.groupby('Genre (1)')['Gross Profit ($)'].mean()
secondary_genre_profit = df.groupby('Genre (2)')['Gross Profit ($)'].mean()
director_profit = df.groupby('Director (1)')['Gross Profit ($)'].mean()
cast_profit = df[['Cast (1)', 'Gross Profit ($)']].groupby('Cast (1)').mean()

# Step 4: Define Weight Percentages for Contribution Distribution
weight_director = 0.3
weight_genre = 0.3
weight_cast = 0.4

# Step 5: Define the Function to Visualize Detailed Contributions for Each Movie
def visualize_movie_contributions(movie):
    # Initialize contributions
    genre_contribution = 0
    director_contribution = 0
    cast_contributions = {}  # Separate contributions for each cast member

    # Calculate Genre Contributions
    if movie['Genre'] in genre_profit.index:
        genre_contribution += genre_profit[movie['Genre']] * weight_genre
    if 'Genre 2' in movie and movie['Genre 2'] in secondary_genre_profit.index:
        genre_contribution += secondary_genre_profit[movie['Genre 2']] * weight_genre

    # Calculate Director Contribution
    if movie['Director'] in director_profit.index:
        director_contribution += director_profit[movie['Director']] * weight_director

    # Calculate Cast Contributions (Individual)
    for actor in movie['Cast']:
        if actor in cast_profit.index:
            cast_contributions[actor] = cast_profit.loc[actor, 'Gross Profit ($)'] * weight_cast / len(movie['Cast'])
        else:
            cast_contributions[actor] = 0  # If no data available, contribution is 0

    # Calculate Total Gross Profit
    total_gross_profit = genre_contribution + director_contribution + sum(cast_contributions.values()) - movie['Budget']

    # Create a DataFrame for Plotting
    contributions = {
        'Genre Contribution': genre_contribution,
        'Director Contribution': director_contribution,
        **cast_contributions,  # Individual cast member contributions
        'Budget': movie['Budget'],
        'Estimated Gross Profit': total_gross_profit
    }

    # Plot Contributions
    plt.figure(figsize=(14, 8))
    bars = plt.bar(contributions.keys(), contributions.values(), color=['purple', 'blue', 'green'] + ['orange'] * len(movie['Cast']) + ['red'])
    plt.title(f"Contribution Breakdown for '{movie['Title']}'", fontsize=18)
    plt.xlabel("Contribution Elements", fontsize=14)
    plt.ylabel("Value ($)", fontsize=14)
    plt.xticks(rotation=45)

    # Add Text Labels for Each Bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f"${yval:,.0f}", ha='center', va='bottom', fontsize=10)

    plt.tight_layout()

    # Save the plot as an image
    filename = f"{movie['Title'].replace(' ', '_')}_Contributions.png"
    plt.savefig(filename)
    plt.close()

    print(f"Plot saved for '{movie['Title']}' as '{filename}'.")

# Step 6: Define Multiple Movie Details







# Step 7: Generate Plots for Each Movie
for movie in movies:
    visualize_movie_contributions(movie)