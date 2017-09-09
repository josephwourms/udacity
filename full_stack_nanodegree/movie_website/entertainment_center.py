from ud036_StarterCode import fresh_tomatoes
import media

def main():
    # create movie objects
    # Movie(title, duration, storyline, poster_img, trailer_youtube)
    o_brother = media.Movie("O Brother, Where Art Thou?",
                           "107mins",
                            "An American Oddessy",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/5/5b/O_brother_where_art_thou_ver1.jpg/220px-O_brother_where_art_thou_ver1.jpg",
                           "https://www.youtube.com/watch?v=vndkDwrZHCA")
    
    a_man_for_all_seasons = media.Movie("A Man For All Seasons",
                                       "120mins",
                                       "A man is killed for his beliefs",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/c/cb/A_Man_for_All_Seasons_%281966_movie_poster%29.gif/220px-A_Man_for_All_Seasons_%281966_movie_poster%29.gif",
                                       "https://www.youtube.com/watch?v=05mUUFO5Gx0")
    
    shawshank_redemption = media.Movie("The Shawshank Redemption",
                                      "142mins",
                                      "A man escapes from prison",
                                      "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                      "https://www.youtube.com/watch?v=6hB3S9bIaco")
    
    # add movie objects to a movie array
    movies = [o_brother, a_man_for_all_seasons, shawshank_redemption]
    
    # pass the movie array the website creation script
    fresh_tomatoes.open_movies_page(movies)
    
if __name__ == "__main__":
    # call this function if this file is run as a script and not imported as a module.
    main()