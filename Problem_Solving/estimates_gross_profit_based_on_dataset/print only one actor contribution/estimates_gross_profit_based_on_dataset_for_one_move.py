import pandas as pd

# Step 1: Load the dataset
# Replace 'Movie Data Starter Project.xlsx' with the actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit for Movies in the Dataset
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Define the Function to Estimate Movie Profit
def estimate_profit(movie_name, genre, director, cast, budget):
    # Aggregate average gross profit by genre
    genre_profit = df.groupby('Genre (1)')['Gross Profit ($)'].mean()
    secondary_genre_profit = df.groupby('Genre (2)')['Gross Profit ($)'].mean()
    
    # Aggregate average gross profit by director
    director_profit = df.groupby('Director (1)')['Gross Profit ($)'].mean()

    # Aggregate average gross profit by cast
    cast_profit = df[['Cast (1)', 'Gross Profit ($)']].groupby('Cast (1)').mean()

    # Start with 0 profit estimate
    estimated_profit = 0

    # Add profit contribution from genres
    if genre in genre_profit.index:
        estimated_profit += genre_profit[genre]
    if genre in secondary_genre_profit.index:  # In case it's a secondary genre
        estimated_profit += secondary_genre_profit[genre]

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

# Step 4: Define Input Details for the New Movie
new_movie_name = "Dream On"
new_movie_genre = "Drama"
new_movie_director = "Elizabeth Banks"
new_movie_cast = ["Shailene Woodley", "Amandla Stenberg", "Ashley Greene", "Farrah MacKenzie", "Raviv Ulman"]
new_movie_budget = 80_000_000  # Budget in dollars



# Step 5: Estimate Profit
estimated_gross_profit = estimate_profit(new_movie_name, new_movie_genre, new_movie_director, new_movie_cast, new_movie_budget)
print(f"Estimated Gross Profit for '{new_movie_name}': ${estimated_gross_profit:,.2f}")