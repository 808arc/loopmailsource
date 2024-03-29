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

# Prompt the user for their favorite rapper's name
artist_name = input("Who's your favorite rapper atm? ")

# Validate and retrieve the maximum number of songs to process
while True:
    max_count = input("How many songs are we going to check? ")
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

# Create a DataFrame using the collected data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(f"{artist_name}_{max_count}_tracks.csv", index=False)

# Print the DataFrame
print(df)
