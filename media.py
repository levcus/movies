import webbrowser


class Movie():
    """This class provides movie related info and opens movie's trailer"""
    def __init__(self, movie_title, movie_storyline, actors, release_date,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.actors = actors
        self.release_date = release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
