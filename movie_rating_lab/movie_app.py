class Movie():
    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_movie_title(self):
        return self.movie_data["title"]

    def get_movie_rating(self, source="Hard coded"):
        for rating in self.movie_data["rating"]:
            if rating["Source"] == source:
                return rating["Value"]

        # raise Exception("Rating for {} was not found".format(source))
        return "Wait - rating for source {} was not found".format(source)

# Create a variable called title_or_ratings, set to 1.
# You should be able to change this between 1, 2, and 3 to change what your program prints.
search_or_ratings = 17

# Create a function, print_single_movie_rating, that prints the string you had in lab 1.
def print_single_movie_rating(movie_query):
    """Prints details for the movie with title movie_query"""
    movie_object = return_single_movie_object(movie_query, 7)
    # print("The rating for", movie_object.get_movie_title(), "is", movie_object.get_movie_rating("Rotten Tomatoes"))
    print("The rating for {} is {}".format(movie_object.get_movie_title(), movie_object.get_movie_rating("Rotten Tomatoes")))

# Create a function, print_all_ratings, that takes one argument movie_list.
def print_all_ratings(movie_list):
    """Print each movie title in the movie_list argument"""
    for movie in movie_list:
        movie_object = return_single_movie_object(movie, 4)
        print("The movie", movie_object.get_movie_title(), "has a rating of", movie_object.get_movie_rating())

def list_search_results(movie_titles):
    """Prints each movie title in the movie_titles argument"""
    for movie in movie_titles:
        print("   ", movie)

def return_single_movie_object(movie_title, movie_rating):
    """Returns an instance of Movie with the given movie_title and movie_rating"""
    rating_list = [{"Source": "Hard coded", "Value": movie_rating}] # TODO: More ratings here
    return Movie({"title": movie_title, "rating": rating_list})

# Create one main function which will call everything else - subsituting function calls for the print statements.
def main():
    """Main entry point with different output depending on the value of global search_or_ratings"""
    # Inside the main function, create a default_movie_list with "Back to the Future", "Blade", and "Spirited Away"
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]

    # Inside the main function, call the print_all_ratings function and pass it the default_movie_list as a parameter
    print_all_ratings(default_movie_list)

    search_or_ratings = int(input("Enter 1 or 2: "))

    while True: # Infinite loop
        if search_or_ratings == 1:
            list_search_results(default_movie_list)
            break # Stop looping
        elif search_or_ratings == 2:
            print_single_movie_rating("Moana")
            break # Stop looping
        else:
            print("Error: your input must be 1 or 2!")
            search_or_ratings = int(input("Enter 1 or 2: "))

if __name__ == '__main__':
    main()
