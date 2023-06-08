import time
from song_lists import producers, instagram_usernames, tracks

def process_songs(songs, genius):
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

            # Check if producer already exists in the list
            if producer["name"] not in producers:
                producers.append(producer["name"])
                instagram_usernames.append(instagram_username)
                tracks.append(song.title)

            time.sleep(10)

    # Do something with the producers, instagram_usernames, and tracks lists
    # ...
