import media
import fresh_tomatoes

the_martian = media.Movie("The Martian",
                          "The world watches as NASA tries to bring "
                          "Matt Damon back from Mars.",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI",
                          141)

scott_pilgrim = media.Movie("Scott Pilgrim vs the World",
                            "Scott Pilgrim must defeat his new "
                            "girlfriend's seven evil exes in order "
                            "to win her heart",
                            "https://upload.wikimedia.org/wikipedia/"
                            "en/1/14/Scott_Pilgrim_vs._the_World_teaser.jpg",
                            "https://www.youtube.com/watch?v=8NUBVcit5VM",
                            112)

wreck_it_ralph = media.Movie("Wreck it Ralph",
                             "A video game villain wants to be a hero and "
                             "sets out to fulfill his dream, but his quest "
                             "brings havoc to the whole arcade where he "
                             "lives.",
                             "https://upload.wikimedia.org/wikipedia/en/"
                             "1/15/Wreckitralphposter.jpeg",
                             "https://www.youtube.com/watch?v=87E6N7ToCxs",
                             101)

robots_vs_monsters = media.Movie("Pacific Rim",
                                 "As a war between humankind and monstrous "
                                 "sea creatures wages on, a former pilot and "
                                 "a trainee are paired up to drive a "
                                 "seemingly obsolete special weapon in a "
                                 "desperate effort to save the world from the "
                                 "apocalypse.",
                                 "https://upload.wikimedia.org/wikipedia/en/"
                                 "f/f3/Pacific_Rim_FilmPoster.jpeg",
                                 "https://www.youtube.com/watch?v=5guMumPFBag",
                                 131)

terminator_two = media.Movie("Terminator 2: Judgment Day",
                             "A cyborg, identical to the one who failed to "
                             "kill Sarah Connor, must now protect her young "
                             "son, John Connor, from a more advanced cyborg, "
                             "made out of liquid metal.",
                             "https://upload.wikimedia.org/wikipedia/en/8/85/"
                             "Terminator2poster.jpg",
                             "https://www.youtube.com/watch?v=lwSysg9o7wE",
                             137)

firefly_season_one_point_five = media.Movie("Serenity",
                                            "The crew of the ship Serenity "
                                            "tries to evade an assassin sent "
                                            "to recapture one of their number "
                                            "who is telepathic.",
                                            "https://upload.wikimedia.org/"
                                            "wikipedia/en/9/9e/Serenity_One"
                                            "_Sheet.jpg",
                                            "https://www.youtube.com/watch?v="
                                            "6nEAlpTb4tk",
                                            119)


star_wars_four = media.Movie("Star Wars: Episode IV - A New Hope",
                             "Luke Skywalker joins forces with a Jedi Knight, "
                             "a cocky pilot, a wookiee and two droids to save "
                             "the universe from the Empire's world-destroying "
                             "battle-station, while also attempting to rescue "
                             "Princess Leia from the evil Darth Vader.",
                             "https://upload.wikimedia.org/wikipedia/en/"
                             "8/87/StarWarsMoviePoster1977.jpg",
                             "https://www.youtube.com/watch?v=vZ734NWnAHA",
                             121)

star_wars_five = media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                             "After the rebels have been brutally overpowered "
                             "by the Empire on their newly established base, "
                             "Luke Skywalker takes advanced Jedi training "
                             "with Master Yoda, while his friends are pursued "
                             "by Darth Vader as part of his plan to capture "
                             "Luke.",
                             "https://upload.wikimedia.org/wikipedia/en/3/3c/"
                             "SW_-_Empire_Strikes_Back.jpg",
                             "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                             124)

star_wars_two = media.Movie("Star Wars: Episode II - Attack of the Clones",
                            "Ten years after initially meeting, Anakin "
                            "Skywalker shares a forbidden romance with Padme, "
                            "while Obi-Wan investigates an assassination "
                            "attempt on the Senator and discovers a secret "
                            "clone army crafted for the Jedi.",
                            "https://upload.wikimedia.org/wikipedia/en/3/32/"
                            "Star_Wars_-_Episode_II_Attack_of_the_Clones_%28"
                            "movie_poster%29.jpg",
                            "https://www.youtube.com/watch?v=gYbW1F_c9eM",
                            142)

star_wars_three = media.Movie("Star Wars: Episode III - Revenge of the Sith",
                              "As the Clone Wars near an end, the Sith Lord "
                              "Darth Sidious steps out of the shadows, at "
                              "which time Anakin succumbs to his emotions, "
                              "becoming Darth Vader and putting his "
                              "relationships with Obi-Wan and Padme at "
                              "risk.",
                              "https://upload.wikimedia.org/wikipedia/en/9/93"
                              "/Star_Wars_Episode_III_Revenge_of_the_Sith_"
                              "poster.jpg",
                              "https://www.youtube.com/watch?v=5UnjrG_N8hU",
                              140)

star_wars_six = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                            "After rescuing Han Solo from the palace of Jabba "
                            "the Hutt, the rebels attempt to destroy the "
                            "second Death Star, while Luke struggles to make "
                            "Vader return from the dark side of the Force.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b2/"
                            "ReturnOfTheJediPoster1983.jpg",
                            "https://www.youtube.com/watch?v=16YLjTkK5jE",
                            134)


fresh_tomatoes.open_movies_page([the_martian, scott_pilgrim, wreck_it_ralph,
                                 firefly_season_one_point_five,
                                 robots_vs_monsters, terminator_two,
                                 star_wars_four, star_wars_five, star_wars_two,
                                 star_wars_three, star_wars_six])
