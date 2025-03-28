import pandas as pd
import json

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

# Step 5: Define the Function to Save Contributions to a JSON File
def save_movie_contributions_to_json(movie):
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

    # Create a Dictionary for JSON Export
    contribution_data = {
        "Title": movie["Title"],
        "Genre Contribution ($)": round(genre_contribution, 2),
        f"Director ({movie['Director']}) Contribution ($)": round(director_contribution, 2),
        "Cast Contributions ($)": {actor: round(cast_contributions[actor], 2) for actor in cast_contributions},
        "Budget ($)": movie["Budget"],
        "Estimated Gross Profit ($)": round(total_gross_profit, 2)
    }

    return contribution_data

# Step 6: Define Multiple Movie Details
movies = [
    {
        "Title": "Dream On",
        "Genre": "Drama",
        "Director": "Elizabeth Banks",
        "Cast": ["Shailene Woodley", "Amandla Stenberg", "Ashley Greene", "Farrah MacKenzie", "Raviv Ulman"],
        "Budget": 80_000_000
    },
    {
        "Title": "Blood Moon",
        "Genre": "Crime",
        "Genre 2": "Thriller",
        "Director": "Todd Phillips",
        "Cast": ["Emma Watson", "John Boyega", "Terry Crews", "Sela Ward", "Ben McKenzie"],
        "Budget": 80_000_000
    },
    {
        "Title": "Gift Exchange",
        "Genre": "Fantasy",
        "Director": "Ava DuVernay",
        "Cast": ["Mackenzie Foy", "Emily Kinney", "Famke Janssen", "Bailee Madison", "Kiernan Shipka"],
        "Budget": 50_000_000
    },
    {
        "Title": "Unlikely Friends",
        "Genre": "Animation",
        "Director": "Tim Burton",
        "Cast": ["Dusan Brown", "Ming-Na Wen", "Queen Latifah", "Jeremy Irons", "Raymond Ochoa"],
        "Budget": 75_000_000
    },
    {
        "Title": "Puppy Love",
        "Genre": "Comedy",
        "Genre 2": "Romance",
        "Director": "Jennifer Westfeldt",
        "Cast": ["Gabrielle Union", "Sam Claflin", "Adam DeVine", "Gary Cole", "Eva Mendes"],
        "Budget": 40_000_000
    }
]

# Step 7: Save Contributions for Each Movie in JSON File
all_contributions = [save_movie_contributions_to_json(movie) for movie in movies]

# Write to JSON File
with open('Movie_Contributions.json', 'w') as json_file:
    json.dump(all_contributions, json_file, indent=4)

print("All contributions have been saved to 'Movie_Contributions.json'.")