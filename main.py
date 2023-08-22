# Import necessary libraries
import pandas as pd
from dotenv import load_dotenv
import os
from genius import genius_auth, get_artist, get_artist_info, get_songs
from song_lists import (
    instagram_usernames,
    data,
    email_public,
    bio_list,
)
from song_processing import process_songs
from instagram_scraper import scrape_instagram_usernames

# Load environment variables from a .env file
load_dotenv()

# Retrieve Genius API and Instagram credentials from environment variables
api_key = os.getenv("api_key")  # Genius API key
user_name = os.getenv("user_name")  # Instagram username
password = os.getenv("password")    # Instagram password

# Prompt the user for their favorite rapper's name
artist_name = input("Whos your favorite rapper? ")

# Validate and retrieve the maximum number of songs to process
while True:
    max_count = input("How many songs are we going to drill? ")
    if max_count.isdigit():
        max_count = int(max_count)
        break
    else:
        print("Invalid input. Please enter a valid number.")

# Authenticate with the Genius API using the provided API key
genius = genius_auth(api_key)
print("login genius")

# Fetch information about the artist
artist = get_artist(artist_name, genius, max_count)
artist_info = get_artist_info(artist, genius)

# Retrieve the list of songs by the artist
songs = get_songs(artist)

# Process the fetched songs using custom processing functions
process_songs(songs, genius)

# Scrape Instagram usernames' public email and bio information
scrape_instagram_usernames(
    user_name, password, instagram_usernames, email_public, bio_list
)

# Create a DataFrame using the collected data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel(f"{artist_name}_{max_count}_tracks.xlsx", sheet_name="Sheet1", index=False)

# Print the DataFrame
print(df)
