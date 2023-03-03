
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from pandas import DataFrame, concat

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
        playlist_df = DataFrame(columns=self.playlist_attributes_list)
        playlist = self.user_playlist_tracks(self.sp_user_name, playlist_id)["items"]
        for track in playlist:
            playlist_features = {}
            playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
            playlist_features["album"] = track["track"]["album"]["name"]
            playlist_features["track_name"] = track["track"]["name"]
            playlist_features["track_id"] = track["track"]["id"]

            audio_features = self.audio_features(playlist_features["track_id"])[0]
            for feature in self.playlist_attributes_list[4:]:
                playlist_features[feature] = audio_features[feature]

            track_df = DataFrame(playlist_features, index=[0])
            playlist_df = concat([playlist_df, track_df], ignore_index=True)
            self.playlist_df = playlist_df

        self.format_output(song_queue)

    def format_output(self, song_queue):
        for counter in range(len(self.playlist_df)):
            artist_name = self.playlist_df["artist"][counter]
            song_name = self.playlist_df["track_name"][counter]
            song_duration = int(self.playlist_df["duration_ms"][counter]/1000)

            track_id = self.playlist_df["track_id"][counter]
            track_data = self.track(track_id)
            cover_url = track_data['album']['images'][0]['url']

            song = Song(artist_name, song_name, song_duration, cover_url)
            song_queue.put(song)
    

    def search_for_song(self, search_words, song_queue) :
        search_res = self.search(search_words, type='track', limit=1)['tracks']['items'][0]
        song_name = search_res['name']
        cover_url = search_res['album']['images'][0]['url']
        artist_name = search_res['album']['artists'][0]['name']
        song_duration = int(search_res['duration_ms'] / 1000)

        song = Song(artist_name, song_name, song_duration, cover_url)
        song_queue.put(song)