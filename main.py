import lyricsgenius
import time

# Open the file and read the API key
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

# Delay execution for 2 seconds
time.sleep(2)

# Initialize Genius object with API key
genius = lyricsgenius.Genius(api_key)

# Increase the timeout duration to 10 seconds
genius.timeout = 10

duplicated_list = []
dictionary = dict.fromkeys(duplicated_list)
deduplicated_list = list(dictionary)

#artist_name = input("Tell me rapper name: ")
artist_name = 'Drake'

# Search for the artist using the 'search_artist' method
artist = genius.search_artist(artist_name, max_songs=None)

# Delay execution for 5 seconds
time.sleep(5)

# Iterate over the songs
for song in artist.songs:
    # Retrieve the information of the song
    song_info = genius.song(song.id)

    # Iterate over the producer artists of the song
    for artist in song_info["song"]["producer_artists"]:
        duplicated_list.append(artist["name"])

# Deduplicate the list of artists
deduplicated_list = list(set(duplicated_list))

print(deduplicated_list)
print(len((deduplicated_list)))