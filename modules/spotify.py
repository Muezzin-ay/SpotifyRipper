
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from modules.song import Song



class SpotifyApi(Spotify):
    def __init__(self, client_id, secret_id, sp_user_name) -> None:
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=secret_id)
        super().__init__(client_credentials_manager=client_credentials_manager)

        self.sp_user_name = sp_user_name
        self.playlist_attributes_list = ["artist", "album", "track_name", "track_id", "danceability", "energy", "key", "loudness",
                                "mode", "speechiness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms",
                                "time_signature"]

    def get_songs_from_playlist(self, playlist_id, song_queue):
        playlist = self.user_playlist_tracks(self.sp_user_name, playlist_id)["items"]
        for song_data in playlist :
            song = Song(song_data['tracks'])
            song_queue.put(song)
    

    def search_for_song(self, search_words, song_queue) :
        song_data = self.search(search_words, type='track', limit=1)['tracks']['items'][0]
        song = Song(song_data)
        song_queue.put(song)