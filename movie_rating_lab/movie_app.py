from urllib.parse import urlencode, quote_plus
import requests
import os

def get_apikey():
    with open(os.path.join('.', 'omdb-api-key.txt')) as file:
        key = file.read().strip()
    return key

class Movie():
    def __init__(self, movie_data):
        self.omdb_data = movie_data

    def get_movie_title(self):
        return self.omdb_data["Title"]

    def get_movie_rating(self, source="Rotten Tomatoes"):
        for rating in self.omdb_data["Ratings"]:
            if rating["Source"] == source:
                return rating["Value"]

        # raise Exception("Rating for {} was not found".format(source))
        return "Wait - rating for source {} was not found".format(source)

class OMDB():
    def __init__(self, apikey):
        self.apikey = apikey

    def build_url(self, **kwargs):
        # TODO: read up on kwargs # print(kwargs)
        kwargs["apikey"] = self.apikey

        url = "http://www.omdbapi.com/?"
        url += urlencode(kwargs)

        return url

    def call_api(self, **kwargs):
        url = self.build_url(**kwargs) # TODO: read up on flattening kwargs
        response = requests.get(url)
        response_data = response.json()
        return response_data

    def search(self, **kwargs):
        url = self.build_url(**kwargs)
        response = requests.get(url)
        response_data = response.json()
        return response_data["Search"]

# Create a function, print_single_movie_rating, that prints the string you had in lab 1.
def print_single_movie_rating(movie_query):
    """Prints details for the movie with title movie_query"""
    movie_object = return_single_movie_object(movie_query)
    # print("The rating for", movie_object.get_movie_title(), "is", movie_object.get_movie_rating("Rotten Tomatoes"))
    print("The rating for {} is {}".format(movie_object.get_movie_title(), movie_object.get_movie_rating("Rotten Tomatoes")))

# Create a function, print_all_ratings, that takes one argument movie_list.
def print_all_ratings(movie_list):
    """Print each movie title in the movie_list argument"""
    for movie in movie_list:
        movie_object = return_single_movie_object(movie)
        print("The movie", movie_object.get_movie_title(), "has a rating of", movie_object.get_movie_rating())

def list_search_results(movie_query):
    """Prints each movie title in the movie_titles argument"""
    apikey = get_apikey()
    o = OMDB(apikey)
    movie_titles = o.search(s=movie_query)
    for movie in movie_titles:
        print("   ", movie["Title"])

def return_single_movie_object(movie_title):
    """Returns an instance of Movie with the given movie_title and movie_rating"""
    apikey = get_apikey()
    o = OMDB(apikey)
    movie_data = o.call_api(t=movie_title)
    return Movie(movie_data)

def get_movie(movie_query):
    apikey = get_apikey()
    o = OMDB(apikey)
    movie_data = o.call_api(t=movie_query)
    movie = Movie(movie_data)

# Create one main function which will call everything else - subsituting function calls for the print statements.
def main():
    """Main entry point with different output depending on the value of global search_or_ratings"""

    search_or_ratings = int(input("Would you like to search for a movie (1) or find the rating of a specific movie (2)? "))

    while True: # Infinite loop
        if search_or_ratings == 1:
            movie_query = input("Enter the search term: ")
            list_search_results(movie_query)
            break # Stop looping
        elif search_or_ratings == 2:
            movie_query = input("Enter the movie title: ")
            print_single_movie_rating(movie_query)
            break # Stop looping
        else:
            print("Error: your input must be 1 or 2!")
            search_or_ratings = int(input("Would you like to search for a movie (1) or find the rating of a specific movie (2)? "))

if __name__ == '__main__':
    main()
