import pandas as pd
from log_manager import api_key, user_name, password, genius
from genius import get_artist_data
from song_lists import (
    instagram_usernames,
    data,
    email_public,
    bio_list,
)
from song_processing import process_songs
from instagram_scraper import scrape_instagram_usernames
from email_verif import email_check


# Prompt the user for their favorite rapper's name
artist_name = input("Who's your target placement? ")
if artist_name.lower() == "qq":
    exit()  # Exit the program if 'qq' is entered
# Validate and retrieve the maximum number of songs to process
while True:
    max_count = input("How many songs are we going to drill? ")
    if max_count.isdigit():
        max_count = int(max_count)
        break
    else:
        print("Invalid input. Please enter a valid number.")


# Fetch information about the artist
artist, artist_info, songs = get_artist_data(artist_name, api_key, max_count)

# Process the fetched songs using custom processing functions
process_songs(songs, genius)

# Scrape Instagram usernames' public email and bio information
scrape_instagram_usernames(
    user_name, password, instagram_usernames, email_public, bio_list
)

# Call the email_check function to perform email verification
email_check()

df = pd.DataFrame(data)

df.to_csv(f"{artist_name}_{max_count}_tracks.csv", index=False)

print(df)
