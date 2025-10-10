import os 
import json 

FILE_NAME = "movies.json"

#loading data from JSON file is an interestin skill 

def load_movies():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILE_NAME, 'w', encoding="utf-8") as f:
        json.dump(movies, f, indent=2)
    
def add_movies(movies):
    title = input("Enter the movie name: ").strip().lower()

    if any(movie["title"].lower() == title for movie in movies):
        print("Movie already exists.")
        return 
    genre = input("Genre: ").strip().lower()
    try:
        rating = float(input("Enter rating 0-10"))
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Please enter a valid number.")
        return 
    
    movies.append({"title": title, "genre": genre, "rating": rating})
    save_movies(movies)
    print("Movie added!")

def search_movies(movies):
    movie_search = input("Which movie do you wish to search for? ").lower()
    for movie in movies:
        if movie["title"].lower() == movie_search:
            print(f"Name: {movie['title']} \nGenre: {movie['genre']} \nRating: {movie['rating']}")
            return  # stop after finding the first match
    print("Movie not found.")

def run_movie_db():
    movies = load_movies()

    while True:
        print("\n MOVIE DB ")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit.")

        try:
            choice = int(input("Enter your choice 1-4"))
            match choice:
                case 1:
                    add_movies(movies)
                case 2:
                    if not movies:
                        print("No movies found.")
                    else:
                        for movie in movies:
                            print(f"Name: {movie['title']} | Genre: {movie['genre']} | Rating: {movie['rating']}")

                case 3: 
                    search_movies(movies)
                case 4:
                    break
                case _:
                    print("Kindly enter a value within 1-4")
        except ValueError:
            print("Kindly Enter a valid Choice.")

if __name__ == "__main__":
    run_movie_db()