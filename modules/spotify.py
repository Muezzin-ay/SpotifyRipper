import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from modules.song import Song

class SpotifyApi():
    def __init__(self, client_id, secret_id) -> None:
        self.client_id = client_id
        self.secret_id = secret_id

        self.playlist_attributes_list = ["artist", "album", "track_name", "track_id", "danceability", "energy", "key", "loudness",
                              "mode", "speechiness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms",
                              "time_signature"]
        
    

    def get_songs_from_playlist(self,playlist_artist,playlist_id):
            client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.secret_id)
            sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
            playlist_df = pd.DataFrame(columns=self.playlist_attributes_list)
            playlist = sp.user_playlist_tracks(playlist_artist, playlist_id)["items"]
            for track in playlist:
                playlist_features = {}
                playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
                playlist_features["album"] = track["track"]["album"]["name"]
                playlist_features["track_name"] = track["track"]["name"]
                playlist_features["track_id"] = track["track"]["id"]

                audio_features = sp.audio_features(playlist_features["track_id"])[0]
                for feature in self.playlist_attributes_list[4:]:
                    playlist_features[feature] = audio_features[feature]

                track_df = pd.DataFrame(playlist_features, index=[0])
                playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)
            self.playlist_df = playlist_df

    def format_output(self):
        youtube_search_strings = []
        song_objects = []
        for counter in range(len(self.playlist_df)):
            artist_name = self.playlist_df["artist"][counter]
            song_name = self.playlist_df["track_name"][counter]
            song_duration = int(self.playlist_df["duration_ms"][counter]/1000)
            youtube_search_strings.append(f'{artist_name} {song_name}')

            song_objects.append(Song(artist_name,song_name,song_duration))

        return song_objects
    