class Band():
    number_of_bands = 0
    known_genres = ['rock', 'pop', 'classical']
    def __init__(self, band_name, genre, albums_released=0):
        self.band_name = band_name
        self.albums_released = albums_released
        self.genre = genre
        Band.number_of_bands += 1

    def print_stats(self):
        print("The", self.genre, "band", self.band_name, "has", self.albums_released, "albums.")
        if self.genre not in Band.known_genres:
            print("This isn't a genre I know.")

slint = Band('Slint', 'rock', 2)
