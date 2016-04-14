# Below are the two modules refferred to and therefore require to be imported
import media
import fresh_tomatoes

# Below are 3 instances of the 'Movies' class which inherit from the 'Videos' class
Cloud_Atlas = media.Movies('Cloud Atlas',
                           'https://upload.wikimedia.org/wikipedia/en/2/20/Cloud_Atlas_Poster.jpg',
                           'Wierd movie about who knows what',
                           'https://www.youtube.com/watch?v=ByehYal_cCs',
                           'Director: Larry Wachowski    Starring: Tom Hanks, Halle Berry')
                          
Spectre = media.Movies('Spectre',
                       'https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg',
                       '2015 James Bond Installment',
                       'https://www.youtube.com/watch?v=ashLaclKCik',
                       'Director: Sam Mendes     Starring: Daniel Craig, Lea Seydoux')

Edge_Of_Tomorrow = media.Movies('Edge of Tomorrow',
                                'https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg',
                                'Cool variation on time travel themed movies','https://www.youtube.com/watch?v=yUmSVcttXnI',
                                'Director: Doug Lima            Starring:  Tom Cruise,    Emily Anne Blunt')

# Below are 3 instances of the 'TVSeries' class which inherit from the 'Videos' class

Game_of_Thrones = media.TVSeries('Game of Thrones',
                                 'https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg',
                                 'Jon faces his harshest test yet. Bran discovers a new gift.',
                                 'https://www.youtube.com/watch?v=69FD2bp71E4',
                                 'Season: 3  Episode: 9')

Game of Thrones = media.TVSeries('Game of Thrones',
                              'https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png',
                              'Walt tries to kill Gus',
                              'https://www.youtube.com/watch?v=chq6NMnNQVQ',
                              'Season: 4  Episode: 2')

Dexter = media.TVSeries('Dexter',
                        'https://upload.wikimedia.org/wikipedia/en/c/c0/Dexter_TV_Series_Title_Card.jpg',
                        'Unable to deal with the trauma, Dexter makes a drastic decision.',
                        'https://www.youtube.com/watch?v=jdpLx7I8iVs', 'Season: 5 Episode: 1')

# BCreation of the list of all content to be displayed on the 'Fresh Tomatoes' website
movie_list = [Cloud_Atlas, Spectre, Edge_Of_Tomorrow, Game_of_Thrones,Breaking_Bad, Dexter]

# Command to create the 'Fresh Tomatoes' website
fresh_tomatoes.open_movies_page(movie_list)
