import time
from song_lists import producers, instagram_usernames, tracks


def process_songs(songs, genius):
    num_producers = len(producers)  # Get the initial number of producers

    # Calculate the estimated total time
    estimated_total_time = len(songs) * 10 * num_producers
    print(f"Estimated total time: {estimated_total_time} seconds")

    start_time = time.time()  # Get the start time

    # Iterate over the songs
    for i, song in enumerate(songs):
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
                print(producer["name"] + " data collected!")

            time.sleep(10)

        # Calculate the elapsed time and estimated remaining time
        elapsed_time = time.time() - start_time
        producers_processed = len(producers) - num_producers
        estimated_remaining_time = (elapsed_time / producers_processed) * (
            len(songs) - i - 1
        )

        print(f"Estimated time remaining: {estimated_remaining_time:.2f} seconds")

    # Do something with the producers, instagram_usernames, and tracks lists
