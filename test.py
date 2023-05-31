import lyricsgenius
import time

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

# Initialize Genius object with API key
genius = lyricsgenius.Genius(api_key)

# Increase the timeout duration to 10 seconds
genius.timeout = 10

artist = genius.search_artist("Drake", max_songs=1)

# Retrieve the information of the artist
artist_info = genius.artist(artist.id)

# Access the "instagram_name" key in the artist's information
instagram_username = artist_info["artist"]["instagram_name"]
print(instagram_username)
