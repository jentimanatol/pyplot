import pandas as pd

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit for Each Movie in the Dataset
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

# Step 5: Define the Function to Estimate Contributions for Each Movie
def estimate_movie_contributions(movie):
    gross_profit_contributions = {'Title': movie['Title'], 'Gross Profit ($)': 0}
    genre_contribution = 0
    director_contribution = 0
    cast_contribution = 0

    # Add Genre Contributions
    if movie['Genre'] in genre_profit.index:
        genre_contribution += genre_profit[movie['Genre']] * weight_genre
    if 'Genre 2' in movie and movie['Genre 2'] in secondary_genre_profit.index:
        genre_contribution += secondary_genre_profit[movie['Genre 2']] * weight_genre

    # Add Director Contribution
    if movie['Director'] in director_profit.index:
        director_contribution += director_profit[movie['Director']] * weight_director

    # Add Cast Contribution
    for actor in movie['Cast']:
        if actor in cast_profit.index:
            cast_contribution += cast_profit.loc[actor, 'Gross Profit ($)'] * weight_cast / len(movie['Cast'])

    # Total Contributions
    gross_profit_contributions['Genre Contribution ($)'] = genre_contribution
    gross_profit_contributions['Director Contribution ($)'] = director_contribution
    gross_profit_contributions['Cast Contribution ($)'] = cast_contribution
    gross_profit_contributions['Gross Profit ($)'] = genre_contribution + director_contribution + cast_contribution - movie['Budget']
    
    return gross_profit_contributions

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
        "Cast": ["Dwayne Johnson", "Alicia Vikander", "Danny Trejo", "Ian Ziering", "Tara Reid"],
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

# Step 7: Calculate Contributions for Each Movie
results = [estimate_movie_contributions(movie) for movie in movies]

# Step 8: Sort Results by Gross Profit
sorted_results = sorted(results, key=lambda x: x['Gross Profit ($)'], reverse=True)

# Step 9: Save to CSV File
sorted_results_df = pd.DataFrame(sorted_results)
sorted_results_df.to_csv('Sorted_Movie_Contributions.csv', index=False)

# Step 10: Output Confirmation
print("Sorted contributions for each movie have been saved to 'Sorted_Movie_Contributions.csv'.")