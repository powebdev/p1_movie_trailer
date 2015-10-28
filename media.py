import webbrowser


class Movie(object):
    """
    Implementation of the Movie type

    Attributes:
    title: a string representing the title of the movie
    storyline: a string representing
    poster_art_url: a string
    trailer_url: a string
    running_time: a integer indicating the movie's running time in minutes.
    director: a list containing the name of the director(s) of the movie.
    """
    def __init__(self, movie_title, movie_storyline, poster_art_url,
                 youtube_trailer_url, movie_running_time):
        """
        Initialize Movie objects

        Args:
            movie_title(str): Movie's name.
            movie_storyline(str): Brief description of the movie.
            poster_art_url(str): URL for the movie poster.
            youtube_trailer_url(str): URL for the movie trialer on youtube.
            movie_running_time(int): Movie's running time in minutes.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_art_url = poster_art_url
        self.trailer_url = youtube_trailer_url
        self.running_time = movie_running_time

    def show_trailer(self):
        """
        Open a modal that plays the trailer for the movie.
        """

        webbrowser.open(self.trailer_url)
