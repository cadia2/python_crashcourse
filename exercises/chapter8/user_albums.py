def make_album(artist_name, album, songs = None):
    '''We will return a dictionary of artist, album'''
    if songs:
        artist_album = {
            'artist_name': artist_name.title(),
            'album': album.title(),
            'songs':int(songs)
        }
        return artist_album

    else:    
        artist_album = {
            'artist_name': artist_name.title(),
            'album': album.title(),
        }
        return artist_album

while True:
    print('\nTime to share with us your favorite artist and title!')
    print("You can always press 'q' to exit the program") 

    f_artist = input("Who is your favorite artist?")
    if f_artist == 'q': 
        break

    f_album = input("What is your favorite album?")
    if f_album == 'q': 
        break

    favorite = make_album(f_artist, f_album)
    print(favorite)

    
    
