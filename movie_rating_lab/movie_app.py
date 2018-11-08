# Create a variable called title_or_ratings, set to 1.
# You should be able to change this between 1, 2, and 3 to change what your program prints.
search_or_ratings = 1

# Create a variable `movie_title` and set it to "Back to the Future".
movie_title = "Back to the Future"

# Create a variable `movie rating` to hold the rating and set it to `8`.
movie_rating = 8

# Create a function, print_movie_title, that prints the movie title.
def print_movie_title():
    print(movie_title)

# Create a function, print_movie_rating, that prints the movie rating.
def print_movie_rating():
    print(movie_rating)

# Create a function, print_single_movie_rating, that prints the string you had in lab 1.
def print_single_movie_rating():
    print("The rating for", movie_title, "is", movie_rating)

# Create a function, print_all_ratings, that takes one argument movie_list.
def print_all_ratings(movie_list):
    for movie in movie_list:
        print("The movie", movie, "has a great rating!")

def list_search_results(movie_titles):
    for movie in movie_titles:
        print("   ", movie)

# Create one main function which will call everything else - subsituting function calls for the print statements.
def main():
    # Inside the main function, create a default_movie_list with "Back to the Future", "Blade", and "Spirited Away"
    default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]

    # Inside the main function, call the print_all_ratings function and pass it the default_movie_list as a parameter
    print_all_ratings(default_movie_list)
    if search_or_ratings == 1:
        list_search_results(default_movie_list)
    elif search_or_ratings == 2:
        print_movie_rating()
    else:
        print_single_movie_rating()


if __name__ == '__main__':
    main()
