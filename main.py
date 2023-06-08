import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
#Genius credentials
api_key = os.getenv("api_key")
#IG credentials
user_name = os.getenv("user_name")
password = os.getenv("password")

artist_name = 'Drake'

max_count = 1

from genius import genius_auth, get_artist, get_artist_info, get_songs

genius = genius_auth(api_key)
artist = get_artist(artist_name, genius, max_count)
artist_info = get_artist_info(artist, genius)
songs = get_songs(artist)

from song_lists import producers, instagram_usernames, tracks, data, email_public
from song_processing import process_songs
process_songs(songs, genius)

from instagram_scraper import scrape_instagram_usernames
ig = scrape_instagram_usernames(user_name, password, instagram_usernames, email_public)

df = pd.DataFrame(data)

print(df)