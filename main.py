import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

artist_name = 'Drake'

max_count = 3

from genius import genius_auth
from genius import get_artist
from genius import get_artist_info
from genius import get_songs

genius = genius_auth(api_key)
artist = get_artist(artist_name, genius, max_count)
artist_info = get_artist_info(artist, genius)
songs = get_songs(artist)

from song_lists import producers, instagram_usernames, tracks, data
from song_processing import process_songs
process_songs(songs, genius)

df = pd.DataFrame(data)
print(df)