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

album1 = make_album("artist","album1")
print(album1)
album2 = make_album("artist","album2")
print(album2)
album3 = make_album("artist","album3")
print(album3)
album4 = make_album("artist","album4","4")
print(album4)
