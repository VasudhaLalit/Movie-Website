import movie_trailer
import media

# ---- List of movies for trailer website and their associated values ---- #
# ---- are set here------------------------------------------------------- #
# -------------------------------------------------------------------------#

toy_story = media.Movie("Toy Story (1995)",
                        "A cowboy doll is profoundly threatened and jealous "
                        "when a new space man figure supplants him as top toy"
                        " in a boy's room.",
                        r"..\images\Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar (2009)",
                     "A paraplegic marine dispatched to the moon Pandora on a"
                     " unique mission becomes torn between following his"
                     " orders and protecting the world he feels is his home",
                     r"..\images\Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")


You_ve_Got_Mail = media.Movie("You've Got Mail (1998)",
                              "Two business rivals who despise each other in "
                              "real life unwittingly fall in love over the "
                              "Internet.",
                              r"..\images\You've_Got_Mail.jpg",
                              "https://www.youtube.com/watch?v=znESQTt3L80")

zootopia = media.Movie("Zootopia (2016)",
                       "In a city of anthropomorphic animals, a rookie bunny"
                       "cop and a cynical con artist fox must work together to"
                       " uncover a conspiracy.",
                       r"..\images\Zootopia.jpg",
                       "https://www.youtube.com/watch?v=CzvH6_e2a-U")

the_jungle_book = media.Movie("The Jungle Book (2016)",
                              "After a threat from the tiger Shere Khan forces"
                              " him to flee the jungle, a man-cub named Mowgli"
                              " embarks on a journey of self discovery with"
                              " the help of panther, Bagheera, and free"
                              " spirited bear, Baloo.",
                              r"..\images\jungle_book.jpg",
                              "https://www.youtube.com/watch?v=C4qgAaxB_pc")

catch_me_if_you_can = media.Movie("Catch Me If You Can (2002)",
                                  "The story of Frank Abagnale Jr., before his"
                                  " 19th birthday, successfully forged"
                                  " millions of dollars' worth of checks while"
                                  " posing as a Pan Am pilot, a doctor, and"
                                  " legal prosecutor as a seasoned and"
                                  " dedicated FBI agent pursues him. ",
                                  r"..\images\catch_me_if_you_can.jpg",
                                  "https://www.youtube.com/watch?v=71rDQ7z4eFg")

movies = [toy_story, avatar, You_ve_Got_Mail, zootopia,
          the_jungle_book, catch_me_if_you_can]

# ----movie_trailer.py file generates the web page for movie trailers ----#
# ----for all the movies listed above ----------------------------------- #

movie_trailer.open_movies_page(movies)
