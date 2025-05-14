import csv
from pprint import pprint

def load_movie_data(filename):
    movies = []
    
    with open(filename, mode='r', encoding='utf-8') as file:
        # Read the file as regular CSV to handle empty columns
        csv_reader = csv.reader(file)
        
        # Extract header row and find indices of non-empty columns
        headers = next(csv_reader)
        columns = [i for i, header in enumerate(headers) if header.strip() != '']
        
        # Map column indices to their names
        col_map = {
            'title': columns[0],
            'release_date': columns[1],
            'genre': columns[3],
            'director': columns[5],
            'cast_start': columns[7],
            'budget': columns[12],
            'box_office': columns[13]
        }
        
        for row in csv_reader:
            # Extract cast members (columns 7-11)
            cast = [row[i].strip() for i in range(col_map['cast_start'], col_map['cast_start']+5) if row[i].strip()]
            
            movie = {
                'title': row[col_map['title']].strip(),
                'release_date': row[col_map['release_date']].strip(),
                'genre': row[col_map['genre']].strip(),
                'director': row[col_map['director']].strip(),
                'cast': cast,
                'budget': row[col_map['budget']].strip().replace('$', '').replace(',', ''),
                'box_office': row[col_map['box_office']].strip().replace('$', '').replace(',', '')
            }
            movies.append(movie)
    
    return movies

if __name__ == "__main__":
    try:
        movies = load_movie_data('Movie_Data_Starter_Project1.csv')
        
        print("First 3 movies:")
        for i, movie in enumerate(movies[:3], 1):
            print(f"\nMovie {i}:")
            pprint(movie, sort_dicts=False)
        
        print(f"\nTotal movies loaded: {len(movies)}")
    except Exception as e:
        print(f"Error loading file: {e}")
        print("Please check:")
        print("- File is in the same directory as this script")
        print("- File name is exactly 'Movie_Data_Starter_Project1.csv'")
        print("- File has the expected format with 14 columns")