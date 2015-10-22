import webbrowser

class Movie(object):
    """
    Implementation of the Movie type
    
    Attributes:
    title: a string representing the title of the movie
    storyline: a string representing 
    poster_art_url: a string
    trailer_url: a string
    release_date: a date object representing the movie's release date in the U.S.
    running_time: a integer indicating the movie's running time in minutes.
    genre: a string represeting the genre of the movie.
    cast: a list containing the names of the top two billed cast members of the movie according to IMDB.
    director: a list containing the name of the director(s) of the movie.
    """
    def __init__(self, movie_title, movie_storyline, my_description,
                 poster_art_url, youtube_trailer_url,
                 movie_release_date, movie_running_time,
                 movie_genre, movie_cast, movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_art_url = poster_art_url
        self.trailer_url = trailer_youtube_url
        self.running_time = movie_running_time
        
        
    def show_trailer():
        """
        Opens a new browser that plays the trailer for the movie.
        """
        
        webbrowser.open(self.trailer_url)
        
