import time
import lyricsgenius


def genius_auth(api_key):
    # Initialize Genius object with API key
    genius = lyricsgenius.Genius(api_key)

    time.sleep(1)
    # Increase the timeout duration to 10 seconds
    genius.timeout = 10
    # Search for the artist using the 'search_artist' method
    return genius


def get_artist(artist_name, genius, max_count):
    artist = genius.search_artist(
        artist_name, max_songs=max_count, include_features=True
    )
    return artist


def get_artist_info(artist, genius):
    # Retrieve the information of the artist
    artist_info = genius.artist(artist.id)
    return artist_info


def get_songs(artist):
    # Fetch all songs by the artist
    songs = artist.songs
    return songs
