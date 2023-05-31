import lyricsgenius
import time
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

# Initialize Genius object with API key
genius = lyricsgenius.Genius(api_key)

# Increase the timeout duration to 10 seconds
genius.timeout = 10

# Search for the artist using the 'search_artist' method
artist_name = 'Drake'
artist = genius.search_artist(artist_name, max_songs=3)

# Retrieve the information of the artist
artist_info = genius.artist(artist.id)

# Fetch all songs by the artist
songs = artist.songs

a = []
b = []
c = []
# Iterate over the songs
for song in songs:
    # Retrieve the information of the song
    song_info = genius.song(song.id)

    # Retrieve the producer artists of the song
    producer_artists = song_info["song"]["producer_artists"]

    # Iterate over the producer artists
    for producer in producer_artists:
        # Retrieve the producer's information
        producer_info = genius.artist(producer["id"])

        # Access the producer's Instagram username
        instagram_username = producer_info["artist"]["instagram_name"]
#        print(producer["name"], instagram_username)
        a.append(producer["name"])
        b.append(instagram_username)
        c.append(song.title)

data = {
    "Producer": a,
    "IG": b,
    "Track": c
    }    

df = pd.DataFrame(data)

deduplicated_df = df.drop_duplicates(subset=["Producer", "IG"])
#print("Deduplicated DataFrame:")
print(deduplicated_df)


#print(df)