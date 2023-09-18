import lyricsgenius


def genius_auth(api_key):
    # Initialize Genius object with API key
    genius = lyricsgenius.Genius(api_key)
    # Increase the timeout duration to 10 seconds
    genius.timeout = 10
    # Search for the artist using the 'search_artist' method
    return genius


def get_artist_info(artist, genius):
    # Retrieve the information of the artist
    artist_info = genius.artist(artist.id)
    return artist_info


def get_artist_data(artist_name, api_key, max_count):
    # Authenticate to Genius API
    genius = genius_auth(api_key)
    # Search for the artist and retrieve their information
    artist = genius.search_artist(
        artist_name, max_songs=max_count, include_features=True
    )
    # Retrieve the additional information of the artist
    artist_info = get_artist_info(artist, genius)
    # Fetch all songs by the artist
    songs = artist.songs
    # Return the artist, artist_info, and songs as a tuple
    return artist, artist_info, songs
