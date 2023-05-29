import lyricsgenius
import time

#sleep = time.sleep(2)
# add your Genius API access token here 
genius = lyricsgenius.Genius('')

#genius = lyricsgenius.PublicAPI()

# Search for 10 Drake songs using the 'search_artist' method
artist = genius.search_artist("Drake", max_songs=4, include_features=True) 


# Iterate over the songs
for song in artist.songs:
    # Retrieve the information of the song
    song_info = genius.song(song.id(time.sleep(6))) 
    
    # Iterate over the producer artists of the song
    for artist in song_info["song"]["producer_artists"]:
        print(artist["name"], sep=", ")