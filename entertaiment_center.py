import fresh_tomatoes
import media


# List of movies created using the Movie class from media module
the_peanuts_movie = media.Movie("The Peanuts Movie", "Snoopy embarks upon his"
                                " greatest mission as he and his team take to"
                                " the skies to pursue their arch-nemesis, whi"
                                "le his best pal Charlie Brown begins his own"
                                " epic quest back home.", "Noah Schnapp, Bill"
                                " Melendez, Hadley Belle Miller, Francesca Ca"
                                "paldi", "November 6", "http://ia.media-imdb."
                                "com/images/M/MV5BMTU1MzAxOTY2MV5BMl5BanBnXkF"
                                "tZTgwNzYzMzM5NTE@._V1_UY209_CR0,0,140,209_AL"
                                "_.jpg", "https://www.youtube.com/watch?v=fVR"
                                "4E6Q6u5g")

spotlight = media.Movie("Spotlight", "The true story of how the Boston Globe "
                        "uncovered the massive scandal of child molestation a"
                        "nd cover-up within the local Catholic Archdiocese, s"
                        "haking the entire Catholic Church to its core.", "Ma"
                        "rk Buffalo, Michael Keaton, Rachel McAdams, Liev Sch"
                        "reiber", "November 6", "http://ia.media-imdb.com/ima"
                        "ges/M/MV5BMjIyOTM5OTIzNV5BMl5BanBnXkFtZTgwMDkzODE2Nj"
                        "E@._V1_UY209_CR0,0,140,209_AL_.jpg", "https://www.yo"
                        "utube.com/watch?v=EwdCIpbTN5g")

brooklyn = media.Movie("Brooklyn", "An Irish immigrant lands in 1950s Brookly"
                       "n, where she quickly falls into a new romance. When h"
                       "er past catches up with her, however, she must choose"
                       " between two countries and the lives that exist withi"
                       "n.", "Saoirse Ronan, Emory Cohen, Domhnall Gleeson, J"
                       "im Broadbent", "November 4", "http://ia.media-imdb.co"
                       "m/images/M/MV5BMzE4MDk5NzEyOV5BMl5BanBnXkFtZTgwNDM4ND"
                       "A3NjE@._V1_UY209_CR0,0,140,209_AL_.jpg", "https://www"
                       ".youtube.com/watch?v=4IM1XhTxPAE")

trumbo = media.Movie("Trumbo", "In 1947, Dalton Trumbo was Hollywood's top sc"
                     "reenwriter until he and other artists were jailed and b"
                     "lack listed for their political beliefs.", "Bryan Crast"
                     "on, Diane Lane, Helen Mirren, Louis C.K.", "November 6",
                     "http://ia.media-imdb.com/images/M/MV5BMjM1MDc2OTQ3NV5BM"
                     "l5BanBnXkFtZTgwNzQ0NjQ1NjE@._V1_UY209_CR0,0,140,209_AL_"
                     ".jpg", "https://www.youtube.com/watch?v=n0dZ_2ICpJE")

spectre = media.Movie("Spectre", "A cryptic message from Bond's past sends hi"
                      "m on a trail to uncover a sinister organization. While"
                      " M battles political forces to keep the secret service"
                      " alive, Bond peels back the layers of deceit to reveal"
                      " the terrible truth behind SPECTRE.", "Daniel Craig, C"
                      "hristoph Waltz, Lea Seydoux, Ralph Fiennes", "November"
                      " 6", "http://ia.media-imdb.com/images/M/MV5BMjM2Nzg4Mz"
                      "kwOF5BMl5BanBnXkFtZTgwNzA0OTE3NjE@._V1_UY209_CR0,0,140"
                      ",209_AL_.jpg", "https://www.youtube.com/watch?v=z4UDNz"
                      "XD3qA")

miss_you_already = media.Movie("Miss You Already", "The friendship between tw"
                               "o life-long girlfriends is put to the test wh"
                               "en one starts a family and the other falls il"
                               "l.", "Drew Barrymore, Toni Collette, Dominic "
                               "Cooper, Paddy Considine", "November 6", "http"
                               "://ia.media-imdb.com/images/M/MV5BMjQzNDE1OTM"
                               "5M15BMl5BanBnXkFtZTgwMTQwMTAwNzE@._V1_UY209_C"
                               "R0,0,140,209_AL_.jpg", "https://www.youtube.c"
                               "om/watch?v=QtdVWsA3ctI")

movies = [the_peanuts_movie, spotlight, brooklyn, trumbo, spectre,
          miss_you_already]

# Web page created using the open_movies_page function from module fresh_tomat
# oes
fresh_tomatoes.open_movies_page(movies)
