import pandas as pd
import numpy as np

class MovieData:
    def __init__(self, file_path):
        """Initialize the MovieData class and load the dataset."""
        self.file_path = file_path
        self.df = self.load_data()

    def load_data(self):
        """Loads the movie data from the CSV file and cleans it."""
        df = pd.read_csv(self.file_path)
        df.columns = df.columns.str.strip()  # Clean column names
        df = df.dropna(subset=["Movie_Title", "Director", "Cast", "Budget", "BoxOfficeRevenue"])  # Drop missing values
        
        # Convert Budget and BoxOfficeRevenue to numeric values
        df["Budget"] = df["Budget"].replace({r'\$': '', ',': ''}, regex=True).astype(float)
        df["BoxOfficeRevenue"] = df["BoxOfficeRevenue"].replace({r'\$': '', ',': ''}, regex=True).astype(float)
        
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
        return self.df[["Budget", "BoxOfficeRevenue"]].describe()

    def save_cleaned_data(self, output_file):
        """Saves the cleaned dataset to a new CSV file."""
        self.df.to_csv(output_file, index=False)

# Example Usage
movie_data = MovieData("Movie_Data_Starter_Project1.csv")
# print(movie_data.summary_statistics())
# print(movie_data.top_profitable_movies())