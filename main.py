import lyricsgenius
import time

# Open the file and read the API key
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

sleep = time.sleep(2)
# add your Genius API access token here 
#genius = lyricsgenius.Genius('rtdnYUhhPhGP6VbV_aTmh18fqd_m1W1EiMNrSF-FuEI5vu9Zt5ArDmDncLaJnBKA')
genius = lyricsgenius.Genius(api_key)


# Increase the timeout duration to 10 seconds
genius.timeout = 10

# Search for 10 Drake songs using the 'search_artist' method
artist = genius.search_artist("Drake", max_songs=1)
time.sleep(6) 

# Iterate over the songs
for song in artist.songs:
    # Retrieve the information of the song
    song_info = genius.song(song.id)

    # Iterate over the producer artists of the song
    for artist in song_info["song"]["producer_artists"]:
        print(artist["name"], sep=", ")
