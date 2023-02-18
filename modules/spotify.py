import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

class SpotifyApi():
    def __init__(self) -> None:
        self.client_id = 'cca7c68ca72e45639fe08e29cadcb7ed'
        self.secret_id = 'b3870732e7fd4ecbae544d23db5dd5d1'
    

    def log_into_spotify_api(self):
            client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.secret_id)
            sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
            