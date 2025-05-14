import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit for Movies in the Dataset
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Prepare Movies Data for Sorting
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
    },
    {
        "Title": "On One Condition",
        "Genre": "Comedy",
        "Director": "Tyler Perry",
        "Cast": ["Donald Glover", "Quvenzhane Wallis", "Joel McHale", "Nia Long", "Keke Palmer"],
        "Budget": 50_000_000
    },
    {
        "Title": "Power of Two",
        "Genre": "Action",
        "Director": "David Koepp",
        "Cast": ["Cameron Boyce", "Veronika Bonell", "Michelle Rodriguez", "Sarah Hyland", "Javier Bardem"],
        "Budget": 125_000_000
    },
    {
        "Title": "Proxima",
        "Genre": "Sci-Fi",
        "Director": "Lana Wachowski",
        "Cast": ["Lupita Nyongo", "Minka Kelly", "Alfred Enoch", "Dichen Lachman", "Don Cheadle"],
        "Budget": 85_000_000
    },
    {
        "Title": "Aftershocks",
        "Genre": "Horror",
        "Director": "James DeMonaco",
        "Cast": ["Dwayne Johnson", "Jennifer Lawrence", "Danny Trejo", "Ian Ziering", "Tara Reid"],
        "Budget": 100_000_000
    },
    {
        "Title": "Undercover Revolutionary",
        "Genre": "Action",
        "Director": "Kathryn Bigelow",
        "Cast": ["Amr Waked", "Jamie Foxx", "Sandra Oh", "Cobie Smulders", "Akin Gazi"],
        "Budget": 90_000_000
    },
]

# Step 4: Calculate Estimated Gross Profit for Each Movie
genre_profit = df.groupby('Genre (1)')['Gross Profit ($)'].mean()
secondary_genre_profit = df.groupby('Genre (2)')['Gross Profit ($)'].mean()
director_profit = df.groupby('Director (1)')['Gross Profit ($)'].mean()
cast_profit = df[['Cast (1)', 'Gross Profit ($)']].groupby('Cast (1)').mean()

def calculate_movie_profit(movie):
    genre_contribution = 0
    if movie['Genre'] in genre_profit.index:
        genre_contribution += genre_profit[movie['Genre']] * 0.3
    if 'Genre 2' in movie and movie['Genre 2'] in secondary_genre_profit.index:
        genre_contribution += secondary_genre_profit[movie['Genre 2']] * 0.3

    director_contribution = 0
    if movie['Director'] in director_profit.index:
        director_contribution += director_profit[movie['Director']] * 0.3

    cast_contribution = 0
    for actor in movie['Cast']:
        if actor in cast_profit.index:
            cast_contribution += cast_profit.loc[actor, 'Gross Profit ($)'] * 0.4 / len(movie['Cast'])

    total_gross_profit = genre_contribution + director_contribution + cast_contribution - movie['Budget']
    return total_gross_profit

# Calculate profit for all movies
movie_profits = [{"Title": movie["Title"], "Estimated Gross Profit ($)": calculate_movie_profit(movie)} for movie in movies]

# Convert to DataFrame for Sorting
movie_profits_df = pd.DataFrame(movie_profits)
sorted_movies = movie_profits_df.sort_values(by="Estimated Gross Profit ($)", ascending=False)

# Step 5: Plot Sorted Movies with Labels
plt.figure(figsize=(14, 8))
bars = plt.barh(sorted_movies['Title'], sorted_movies['Estimated Gross Profit ($)'], color='teal')
plt.title("Movies Sorted by Estimated Gross Profit", fontsize=18)
plt.xlabel("Estimated Gross Profit ($)", fontsize=14)
plt.ylabel("Movie Title", fontsize=14)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest gross profit on top

# Add Text Labels to Bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 2, bar.get_y() + bar.get_height() / 2,
             f"${width:,.0f}", ha='left', va='center', fontsize=10)

plt.tight_layout()

# Save the plot as an image
plt.savefig('Sorted_Movies_By_Gross_Profit_with_Labels.png')
plt.show()

print("The bar plot of sorted movies with labels by estimated gross profit has been saved as 'Sorted_Movies_By_Gross_Profit_with_Labels.png'.")