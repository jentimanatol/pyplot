import pandas as pd

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit for Movies in the Dataset
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Aggregate Historical Averages for Genres, Directors, and Cast
genre_profit = df.groupby('Genre (1)')['Gross Profit ($)'].mean()
secondary_genre_profit = df.groupby('Genre (2)')['Gross Profit ($)'].mean()
director_profit = df.groupby('Director (1)')['Gross Profit ($)'].mean()
cast_profit = df[['Cast (1)', 'Gross Profit ($)']].groupby('Cast (1)').mean()

# Step 4: Define the Function to Estimate Profit for Each Movie
def estimate_movie_profit(movie_details):
    genre = movie_details['Genre']
    secondary_genre = movie_details.get('Genre 2', None)
    director = movie_details['Director']
    cast = movie_details['Cast']
    budget = movie_details['Budget']
    
    estimated_profit = 0

    # Add profit contribution from genres
    if genre in genre_profit.index:
        estimated_profit += genre_profit[genre]
    if secondary_genre and secondary_genre in secondary_genre_profit.index:
        estimated_profit += secondary_genre_profit[secondary_genre]

    # Add profit contribution from the director
    if director in director_profit.index:
        estimated_profit += director_profit[director]

    # Add profit contribution from the cast
    for actor in cast:
        if actor in cast_profit.index:
            estimated_profit += cast_profit.loc[actor, 'Gross Profit ($)']

    # Subtract the budget to estimate total profit
    gross_profit = estimated_profit - budget
    return gross_profit

# Step 5: Define Multiple Movie Details
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

# Step 6: Estimate Profits for Each Movie
for movie in movies:
    profit = estimate_movie_profit(movie)
    print(f"Estimated Gross Profit for '{movie['Title']}': ${profit:,.2f}")