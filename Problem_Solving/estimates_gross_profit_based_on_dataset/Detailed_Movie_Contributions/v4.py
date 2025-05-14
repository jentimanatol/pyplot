import pandas as pd

# Step 1: Load the Dataset
# Replace 'Movie Data Starter Project.xlsx' with your actual file path
df = pd.read_excel('Movie Data Starter Project.xlsx')

# Step 2: Calculate Gross Profit for Each Movie
df['Gross Profit ($)'] = df['Box Office Revenue ($)'] - df['Budget ($)']

# Step 3: Define Contribution Percentages (weight distribution)
# These percentages distribute the gross profit among contributing elements
weight_director = 0.3
weight_genre = 0.3
weight_cast = 0.4

# Step 4: Create a Detailed Breakdown for Each Movie
detailed_contributions = []

for _, row in df.iterrows():
    gross_profit = row['Gross Profit ($)']
    movie_title = row['Movie Title']
    
    # Director's Contribution
    director_contribution = gross_profit * weight_director / len([d for d in [row['Director (1)'], row['Director (2)']] if pd.notna(d)])
    
    # Genre's Contribution
    genre_contribution = gross_profit * weight_genre / len([g for g in [row['Genre (1)'], row['Genre (2)']] if pd.notna(g)])
    
    # Cast Contribution
    cast_contribution = gross_profit * weight_cast / len([c for c in [row['Cast (1)'], row['Cast (2)'], row['Cast (3)'], row['Cast (4)'], row['Cast (5)']] if pd.notna(c)])
    
    # Append Detailed Contributions
    detailed_contributions.append({
        'Movie Title': movie_title,
        'Director Contribution ($)': director_contribution,
        'Genre Contribution ($)': genre_contribution,
        'Cast Contribution ($)': cast_contribution,
        'Gross Profit ($)': gross_profit
    })

# Step 5: Convert to DataFrame
contributions_df = pd.DataFrame(detailed_contributions)

# Step 6: Save the Results to a File
contributions_df.to_csv('Detailed_Movie_Contributions.csv', index=False)

# Step 7: Output Confirmation
print("Detailed contributions by Director, Genre, and Cast have been saved to 'Detailed_Movie_Contributions.csv'.")