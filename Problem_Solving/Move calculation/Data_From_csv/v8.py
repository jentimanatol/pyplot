import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class MovieData:
    def __init__(self, file_path):
        """Initialize the MovieData class and load the dataset."""
        self.file_path = file_path
        self.df = self.load_data()

    def load_data(self):
        """Loads the movie data from the CSV file and cleans it, with detailed debugging information."""
        if not os.path.exists(self.file_path):
            print(f"Error: File '{self.file_path}' does not exist.")
            return pd.DataFrame()
        
        print(f"Reading file: {self.file_path}")
        df = pd.read_csv(self.file_path)
        print(f"File successfully read. Total rows: {len(df)}")
        
        df.columns = df.columns.str.strip()  # Clean column names
        initial_rows = len(df)
        df = df.dropna(subset=["Movie_Title", "Director", "Cast", "Budget", "BoxOfficeRevenue"])  # Drop missing values
        print(f"Rows after dropping missing values: {len(df)} (removed {initial_rows - len(df)})")
        
        # Convert Budget and BoxOfficeRevenue to numeric values
        df["Budget"] = df["Budget"].replace({r'\$': '', ',': ''}, regex=True).astype(float)
        df["BoxOfficeRevenue"] = df["BoxOfficeRevenue"].replace({r'\$': '', ',': ''}, regex=True).astype(float)
        print("Data successfully cleaned and converted.")
        
        return df

    def filter_by_genre(self, genre):
        """Returns movies filtered by genre."""
        return self.df[self.df["Genre"].str.contains(genre, na=False, case=False)]

    def filter_by_director(self, director):
        """Returns movies filtered by director."""
        return self.df[self.df["Director"].str.contains(director, na=False, case=False)]

    def top_profitable_movies(self, top_n=10):
        """Returns the top N most profitable movies."""
        self.df["Profit"] = self.df["BoxOfficeRevenue"] - self.df["Budget"]
        return self.df.sort_values(by="Profit", ascending=False).head(top_n)

    def summary_statistics(self):
        """Returns summary statistics for budget and revenue."""
        return self.df[["Budget", "BoxOfficeRevenue", "Profit"]].describe()

    def most_profitable_genre(self):
        """Finds the genre with the highest median profit."""
        self.df["Profit"] = self.df["BoxOfficeRevenue"] - self.df["Budget"]
        return self.df.groupby("Genre")["Profit"].median().sort_values(ascending=False)

    def save_cleaned_data(self, output_file):
        """Saves the cleaned dataset to a new CSV file."""
        self.df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")

    def plot_median_budget_by_genre(self):
        """Plots the median budget by genre."""
        median_budget = self.df.groupby("Genre")["Budget"].median().sort_values()
        
        plt.figure(figsize=(10, 6))
        median_budget.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.xlabel("Genre")
        plt.ylabel("Median Budget (in USD)")
        plt.title("Median Budget by Genre")
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    def plot_profit_distribution(self):
        """Plots the distribution of movie profits with additional details and annotations."""
        self.df["Profit"] = self.df["BoxOfficeRevenue"] - self.df["Budget"]
        plt.figure(figsize=(10, 6))
        counts, bins, patches = plt.hist(self.df["Profit"], bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
        
        plt.xlabel("Profit (in USD)")
        plt.ylabel("Number of Movies")
        plt.title("Movie Profit Distribution (Box Office Revenue - Budget)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Adding text labels to histogram bars
        for count, bin_patch in zip(counts, patches):
            height = bin_patch.get_height()
            if height > 0:
                plt.text(bin_patch.get_x() + bin_patch.get_width()/2, height, int(height), 
                         ha='center', va='bottom', fontsize=10, color='black')
        
        plt.show()

    def plot_movies_by_actor_and_genre(self):
        """Plots the number of movies by actor for each genre."""
        # Split the Cast column into a list of actors
        self.df['Cast'] = self.df['Cast'].str.split(',')  
        
        # Exploding the 'Cast' column to have one actor per row
        exploded_df = self.df.explode('Cast')
        
        # Remove leading/trailing spaces from actor names
        exploded_df['Cast'] = exploded_df['Cast'].str.strip()
        
        # Group by Genre and Cast to count number of movies for each actor in each genre
        actor_genre_count = exploded_df.groupby(['Genre', 'Cast']).size().reset_index(name='Movie Count')
        
        # Plotting the results
        plt.figure(figsize=(12, 8))
        for genre in actor_genre_count['Genre'].unique():
            genre_data = actor_genre_count[actor_genre_count['Genre'] == genre]
            plt.bar(genre_data['Cast'], genre_data['Movie Count'], label=genre, alpha=0.7)
        
        plt.xlabel("Actor")
        plt.ylabel("Number of Movies")
        plt.title("Number of Movies by Actor and Genre")
        plt.xticks(rotation=90, ha='center')
        plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

# Example Usage
movie_data = MovieData("Movie_Data_Starter_Project.csv")
# To see the most profitable genre
print(movie_data.most_profitable_genre())
# To plot the profit distribution
movie_data.plot_profit_distribution()
# To plot the number of movies by actor and genre
movie_data.plot_movies_by_actor_and_genre()
